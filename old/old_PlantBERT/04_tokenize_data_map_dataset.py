# Import Libraries
print("import libraries")
import torch
from transformers import RobertaTokenizerFast
import sys
from datasets import load_dataset

# Initialize variables
print("init variables")
home = '/usr/users/nigel.hartman/'
model_type = ""
if len(sys.argv) >= 2:
	model_type = str(sys.argv[1])
if model_type != "plants" and model_type != "other":
	sys.exit("ERROR! Set a model type parameter eg. plants or other")

# Load tokenizer
print("load tokenizer")
tokenizer = RobertaTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary', max_len=512)

# Load unprocessed dataset
print("Load unprocessed dataset")
dataset = load_dataset("text", data_files={"train": [home + 'data/'+ model_type +'/all_sample_'+model_type+'.fna']})

# map dataset (.cache/huggingface)
print("map dataset")
dataset = dataset.map(lambda examples: tokenizer(examples["text"], return_tensors="pt", max_length = 512, padding = 'max_length', truncation = False), batched=True)

# add labels column
print("add labels column")
dataset = dataset["train"].add_column("labels", dataset["train"]["input_ids"])

# format all columns except string to - > tensor (pt)
print("format all columns")
dataset.set_format("pt", columns=["attention_mask", "input_ids", "labels"], output_all_columns=True)

# map function to mask input_ids
def mask_input_ids(example):
	buf = example['input_ids'].unsqueeze(0)
	rand = torch.rand(buf.shape)
	mask_arr = (rand < .15) * (buf != 1) * (buf != 0) * (buf != 2)
	for i in range(buf.shape[0]):
		selection = torch.flatten(mask_arr[i].nonzero()).tolist()
		buf[i, selection] = 4
	return {"input_ids": buf.squeeze(0)}

# run the masking
print("run masking")
dataset = dataset.map(mask_input_ids)

# save to disk
print("save to disk")
dataset.save_to_disk(home + 'data/'+ model_type +'/mapped_dataset')
