print("import  libraries. . .")
import torch
import transformers
from tqdm.auto import tqdm
import sys
from datasets import load_from_disk
import random

home = '/usr/users/nigel.hartman/'
model_type = "plants"

dataset = load_from_disk(home + 'data/'+ model_type +'/mapped_dataset_dnabert2')

loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True) # 512 + 128

if torch.cuda.is_available():
	device = torch.device('cuda:0')
print(device)

# load config first or use pip install trasnformers==4.28.0
#config = BertConfig.from_pretrained("zhihan1996/DNABERT-2-117M")
#model = AutoModel.from_config(config)
model = transformers.AutoModelForMaskedLM.from_pretrained("zhihan1996/DNABERT-2-117M", trust_remote_code=True)
model.to(device)
print(str(model.num_parameters()) + " total parameters")

epochs = 1
N=1
correct=0
for epoch in range(epochs):
	loop = tqdm(loader, leave=True)
	for batch in loop:
		input_ids = batch['input_ids'].to(device)
		attention_mask = batch['attention_mask'].to(device)
		labels = batch['labels'].to(device)
		outputs = model(input_ids, labels=labels)
		max_logits_pre = torch.argmax(outputs.logits, -1)
		for k in range(0, len(max_logits_pre)-1):
                        max_logits = max_logits_pre[k]
                        masked_ids = torch.where(input_ids[k] == 4)
                        for i in range(0, len(masked_ids[0])):
                                N += 1
                                ind = masked_ids[0][i].item()
                                if(max_logits[ind].item() == labels[k][ind].item()):
                                        correct += 1
		print("acc = " + str(correct/N))

