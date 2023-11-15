print("Load Libraries")
from tokenizers import ByteLevelBPETokenizer
from transformers import BertTokenizerFast
from datasets import load_dataset # big data
import os
import sys

home = '/usr/users/nigel.hartman/'

folder = ""

if len(sys.argv) >= 2:
        folder = str(sys.argv[1])
if folder != 'plants' and folder !=  'other':
        sys.exit("ERROR: use parameter plants or other")

print("count lines")
cnt = 0
f = open(home + 'data/' + folder + '/all_sample_' + folder + '.fna', "r")
line = f.readline()
while line:
	cnt+=1
	line = f.readline()

print("Load Dataset")
dataset = load_dataset("text", data_files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'], streaming=True)#, split="train")
dataset = dataset["train"]
tokenizer = ByteLevelBPETokenizer() # old because no kmer anymore add_prefix_space=True) # add prefix space because dont wano have different words cause of leerzeichen
#trainer = trainers.BpeTrainer(vocab_size=4096, special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'], min_frequency=2)

print("Train")
#iterable_dataset = iter(iterable_dataset["train"])

def batch_iterator(batch_size=1000):
	for i in dataset:
		yield i["text"]

tokenizer.train_from_iterator(batch_iterator(), length=cnt, vocab_size=4096, min_frequency=2,special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'], show_progress=True)
#tokenizer.train(files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'], vocab_size=4096, min_frequency=2,special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
os.mkdir(home + 'data/' + folder + '/vocabulary')
tokenizer.save_model(home + 'data/' + folder + '/vocabulary')
