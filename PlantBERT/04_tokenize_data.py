# homefolder
home = '/usr/users/nigel.hartman/'

from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained(home+'data/plants/vocabulary', max_len=512)

## Do some encoding test
#print("\nTest encoding\n")
#tokens = tokenizer('AAAAAA CCCCCC GGGGGG')
#print('tokens')
#print(tokens)
#print('tokens.input_ids')
#print(tokens.input_ids)

## encoding
print('\nstart encoding..\n')
print("Open file")
in_file = open(home + 'data/plants/all_sample_plants.fna', 'r')
print("read lines")
lines = in_file.read().split('\n')
print("tokenize")
batch = tokenizer(lines[0:10000], max_length = 512, padding = 'max_length', truncation = True)
print("len(batch) = " + str(len(batch['input_ids'])))
#print(batch['input_ids'])
#print(batch['attention_mask'])

## Prepare input_ids, attention_mask, labels
print("prepare")
import torch
labels = torch.tensor([batch['input_ids']])
mask = torch.tensor([batch['attention_mask']])

# make copy of labels tensor, this will be input_ids
input_ids = labels.detach().clone()

# create random array of floats with equal dims to input_ids
rand = torch.rand(input_ids.shape)

# mask random 15% where token is not 0 [PAD], 1 [CLS], or 2 [SEP]
mask_arr = (rand < .15) * (input_ids != 0) * (input_ids != 1) * (input_ids != 3)

# loop through each row in input_ids tensor (cannot do in parallel)
for i in range(input_ids.shape[1]):
	# get indices of mask positions from mask array
	selection = torch.flatten(mask_arr[0][i].nonzero()).tolist()
	# mask input_ids
	input_ids[0][i, selection] = 4  ############# our custom [MASK] token is 4!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#print(input_ids.shape)
#print(input_ids[0][1][:200])
print("\tDONE")

#### building dataLoader
print("Build Dataloader:")

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
loader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

print("\tDONE")

print("Init model:")

from transformers import RobertaConfig

config = RobertaConfig(
    vocab_size=30_522,  # we align this to the tokenizer vocab_size
    max_position_embeddings=514,
    hidden_size=768,
    num_attention_heads=12,
    num_hidden_layers=6,
    type_vocab_size=1
)

from transformers import RobertaForMaskedLM

model = RobertaForMaskedLM(config)

print("\tDONE.")

print("Training preparation")

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# and move our model over to the selected device
model.to(device)

#from transformers import AdamW

# activate training mode
model.train()
# initialize optimizer
optim = torch.optim.AdamW(model.parameters(), lr=1e-4)

print("\tDONE.")

print("Training.")
import tqdm
epochs = 2

for epoch in range(epochs):
	#setup loop with TQDM and dataloader
	loop = tqdm(loader, leave=True)
	for batch in loop:
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
		loss.backward()
		# update parameters
		optim.step()
		# print relevant info to progress bar
		loop.set_description(f'Epoch {epoch}')
		loop.set_postfix(loss=loss.item())

print("\tDONE.")
