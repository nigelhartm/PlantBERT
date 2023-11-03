# Import Libraries
print("import  libraries. . .")
import torch
from transformers import RobertaConfig
from transformers import RobertaForMaskedLM
from tqdm.auto import tqdm
import sys
from datasets import load_from_disk
import wandb
import random

#fp16
scaler = torch.cuda.amp.GradScaler()

# Initialize variables
home = '/usr/users/nigel.hartman/'
model_type = "plants"
if len(sys.argv) >= 2:
	model_type = str(sys.argv[1])
else:
	print("model_type preset to plants . . .")
if model_type != "plants" and model_type != "other":
	sys.exit("ERROR! Set a model type parameter eg. plants or other")

# Load mapped dataset
dataset = load_from_disk(home + 'data/'+ model_type +'/mapped_dataset')

#trim dataset (debug)
dataset = dataset.select((i for i in range(len(dataset)) if i < 500000)) # 500k for testing
print("dataset trimmed to " + str(len(dataset)))

# Building dataLoader
print("Build Dataloader . . .")
loader = torch.utils.data.DataLoader(dataset, batch_size=256, shuffle=True)

# Initialize Model
print("Init model . . .")
config = RobertaConfig(
    vocab_size=4096,  # we align this to the tokenizer vocab_size (DNABERT2 says 4096)
    max_position_embeddings=514,
    hidden_size=768,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1
)
model = RobertaForMaskedLM(config)

if torch.cuda.is_available():
	device = torch.device('cuda')
else:
	sys.exit("\tNO GPU ERROR!")
model.to(device)

model = torch.nn.DataParallel(model, range(0, torch.cuda.device_count())) ############## DataParallel#####################################

# start a new wandb run to track this script
wandb.init(
	# set the wandb project where this run will be logged
	project="plantbert",
	name="plantbert_run_000",
	# track hyperparameters and run metadata
	config={
	"learning_rate": 0.04,
	"architecture": "BERT",
	"dataset": "plantbert",
	"epochs": 10
	}
)

# Train the model
print("Training . . .")
model.train() # activate training mode
optim = torch.optim.AdamW(model.parameters(), lr=1e-5) # init optimizer
epochs = 250
cnt = 0
ACC_LOG_STEP = 100
for epoch in range(epochs):
	#setup loop with TQDM and dataloader
	loop = tqdm(loader, leave=True)
	for batch in loop:# loader: #loop:
		# initialize calculated gradients (from prev step)
		optim.zero_grad()
		# pull all tensor batches required for training
		input_ids = batch['input_ids'].to(device)
		attention_mask = batch['attention_mask'].to(device)
		labels = batch['labels'].to(device)
		# mybe set all labels which not to predict=-100 here?
		# fp16
		with torch.cuda.amp.autocast():
			# process
			outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
		# extract loss
		loss = outputs.loss
		# calculate loss for every parameter that needs grad update
		#loss.sum().backward()
		#fp16
		scaler.scale(loss.sum()).backward()
		# update parameters
		#optim.step()
		#fp16
		scaler.step(optim)
		scaler.update()
		# print relevant info to progress bar
		loop.set_description(f'Epoch {epoch}')
		loop.set_postfix(loss=loss.sum().item())
		if(cnt >= ACC_LOG_STEP):
			cnt = 0
			N = 0
			correct = 0
			rnd_correct = 0
			max_logits_pre = torch.argmax(outputs.logits, -1)
			for k in range(0, len(max_logits_pre)-1): # here was a error- index not accesible because i used constant 64 before  ### or not because now just every 100 ... (change to something smaller batch size maybe half or something
				max_logits = max_logits_pre[k]
				masked_ids = torch.where(input_ids[k] == 4)
				for i in range(0, len(masked_ids[0])):
					N += 1
					ind = masked_ids[0][i].item()
					if(max_logits[ind].item() == labels[k][ind].item()):
						correct += 1
					if(random.randint(5, 4095) == labels[k][ind].item()): # random inside Vocabulary size
						rnd_correct += 1
			acc = 0.0
			rnd_acc = 0.0
			if N > 0:
				acc = correct / N
				rnd_acc = rnd_correct / N
			#acc = (torch.argmax(outputs.logits, -1) == labels).float().mean()
			# log metrics to wandb
			wandb.log({"loss": loss.sum().item(), "acc": acc, "random acc": rnd_acc})
		else:
			cnt += 1
			wandb.log({"loss": loss.sum().item()})
	# save later first try outmodel.module.save_pretrained(home+'data/'+model_type+'/model/epoch_'+str(epoch))
