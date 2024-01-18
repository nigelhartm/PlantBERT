print("import libraries")
import torch
from transformers import PreTrainedTokenizerFast
from transformers import AutoTokenizer
import sys
from datasets import load_dataset

print("init variables")
home = '/usr/users/nigel.hartman/'
model_type = "plants"

print("Load unprocessed dataset")
dataset = load_dataset("text", data_files={"train": [home + 'data/'+ model_type +'/all_sample_'+model_type+'.fna']})

print("load tokenizer")
tokenizer = PreTrainedTokenizerFast.from_pretrained("zhihan1996/DNABERT-2-117M", trust_remote_code=True)
#tokenizer = PreTrainedTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary_final', max_len=128)#, special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
#tokenizer.add_special_tokens({'pad_token': '<pad>'})

print("map dataset")
m_dataset = dataset.map(lambda examples: tokenizer(examples["text"], return_tensors="pt", max_length = 128, padding = 'max_length', truncation = True), batched=True)

print("add labels column")
m_dataset = m_dataset["train"].add_column("labels", m_dataset["train"]["input_ids"])

print("format all columns")
m_dataset.set_format("pt", columns=["attention_mask", "input_ids", "labels"], output_all_columns=True)

def mask_input_ids(example):
	buf = example['input_ids'].unsqueeze(0)
	rand = torch.rand(buf.shape)
	mask_arr = (rand < .15) * (buf != 1) * (buf != 0) * (buf != 2)
	for i in range(buf.shape[0]):
		selection = torch.flatten(mask_arr[i].nonzero()).tolist()
		buf[i, selection] = 4
	return {"input_ids": buf.squeeze(0)}

print("run masking")
m_dataset = m_dataset.map(mask_input_ids)

print("save to disk")
m_dataset.save_to_disk(home + 'data/'+ model_type +'/mapped_dataset_dnabert2')
