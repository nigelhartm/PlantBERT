# Import Libraries
print("import torch . . .")
import torch
print("import transformers . . . ")
from transformers import RobertaTokenizerFast
from transformers import RobertaConfig
from transformers import RobertaForMaskedLM
print("import tqdm")
from tqdm.auto import tqdm
print("import sys")
import sys

# Initialize variables
home = '/usr/users/nigel.hartman/'
model_type = ""
if len(sys.argv) >= 2:
	model_type = str(sys.argv[1])
if model_type != "plants" and model_type != "other":
	print("ERROR! Set a model type parameter eg. plants or other")
	print("Correction, fixed automatic to plants!")
	model_type = "plants"

# Load and encode file
tokenizer = RobertaTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary', max_len=512)
print('Encoding . . .')
print("\tOpen file . . .")
in_file = open(home + 'data/'+ model_type +'/all_sample_'+model_type+'.fna', 'r')
print("\tRead lines . . .")
lines = in_file.read().split('\n')
print("\tTokenize lines. . .")
from datetime import datetime
print(datetime.now().strftime("%H:%M:%S"))
batch = tokenizer(lines[0:500000], max_length = 512, padding = 'max_length', truncation = True)
print(datetime.now().strftime("%H:%M:%S"))

# Prepare input_ids, attention_mask, labels
print("Prepare data tensors and random masking . . .")
labels = torch.tensor([batch['input_ids']]).squeeze(0)
mask = torch.tensor([batch['attention_mask']]).squeeze(0)
input_ids = labels.detach().clone()
# create random array of floats with equal dims to input_ids
rand = torch.rand(input_ids.shape)
# mask random 15% where token is not 1 [PAD], 0 [CLS], or 2 [SEP]
mask_arr = (rand < .15) * (input_ids != 1) * (input_ids != 0) * (input_ids != 2)
# loop through each row in input_ids tensor (cannot do in parallel)
for i in range(input_ids.shape[0]):
	# get indices of mask positions from mask array
	selection = torch.flatten(mask_arr[i].nonzero()).tolist()
	# mask input_ids
	input_ids[i, selection] = 4 # our custom [MASK] token is 4!

# Building dataLoader
print("Build Dataloader . . .")
encodings = {'input_ids': input_ids, 'attention_mask': mask, 'labels': labels}
class Dataset(torch.utils.data.Dataset):
	def __init__(self, encodings):
		# store encodings internally
		self.encodings = encodings
	def __len__(self):
		# return the number of samples
		return self.encodings['input_ids'].shape[0]
	def __getitem__(self, i):
		# return dictionary of input_ids, attention_mask, and labels for index i
		return {key: tensor[i] for key, tensor in self.encodings.items()}
dataset = Dataset(encodings)
loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True)

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
	print("\tUsing GPU!")
else:
	device = torch.device('cpu')
	sys.exit("\tUsing CPU! ERROR!")
model.to(device)

model = torch.nn.DataParallel(model, range(0, torch.cuda.device_count())) ############## DataParallel#####################################

# Train the model
print("Training . . .")
model.train() # activate training mode
optim = torch.optim.AdamW(model.parameters(), lr=1e-4) # init optimizer
epochs = 50
for epoch in range(epochs):
	for j in range(0, torch.cuda.device_count()):
		print("GPU("+str(j)+"):"+str(torch.cuda.memory_allocated(j)/1000000000)+" / "+str(torch.cuda.get_device_properties(j).total_memory/1000000000))
	#setup loop with TQDM and dataloader
	loop = tqdm(loader, leave=True)
	for batch in loop:
		# initialize calculated gradients (from prev step)
		optim.zero_grad()
		# pull all tensor batches required for training
		input_ids = batch['input_ids'].to(device)
		attention_mask = batch['attention_mask'].to(device)
		labels = batch['labels'].to(device)
		for j in range(0, torch.cuda.device_count()):
                	print("GPU("+str(j)+"):"+str(torch.cuda.memory_allocated(j)/1000000000)+" / "+str(torch.cuda.get_device_properties(j).total_memory/1000000000))
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
model.module.save_pretrained(home+'data/'+model_type+'/model')
