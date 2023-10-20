# Import Libraries
print("import  libraries. . .")
import torch
from transformers import RobertaConfig
from transformers import RobertaForMaskedLM
from tqdm.auto import tqdm
import sys
from datasets import load_from_disk
import wandb

# Initialize variables
home = '/usr/users/nigel.hartman/'
model_type = ""
if len(sys.argv) >= 2:
	model_type = str(sys.argv[1])
if model_type != "plants" and model_type != "other":
	sys.exit("ERROR! Set a model type parameter eg. plants or other")

# Load mapped dataset
dataset = load_from_disk(home + 'data/'+ model_type +'/mapped_dataset')

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
	# track hyperparameters and run metadata
	config={
	"learning_rate": 0.04,
	"architecture": "BERT",
	"dataset": "plantbert",
	"epochs": 50
	}
)

# Train the model
print("Training . . .")
model.train() # activate training mode
optim = torch.optim.AdamW(model.parameters(), lr=1e-4) # init optimizer
epochs = 50
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
		# process
		outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
		# extract loss
		loss = outputs.loss
		# calculate loss for every parameter that needs grad update
		loss.sum().backward()
		# update parameters
		optim.step()
		# print relevant info to progress bar
		loop.set_description(f'Epoch {epoch}')
		loop.set_postfix(loss=loss.sum().item())
		# log metrics to wandb
		wandb.log({"loss": loss.sum().item()})
model.module.save_pretrained(home+'data/'+model_type+'/model')
