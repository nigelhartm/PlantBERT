# Load Libraries
print("Load Libraries")
from tokenizers import ByteLevelBPETokenizer
from transformers import BertTokenizerFast
from datasets import load_dataset # big data
import sys
import os
from transformers import PreTrainedTokenizerFast
from datetime import datetime
import wandb

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="plantbert_tokenizer",
    
    # track hyperparameters and run metadata
    config={
    }
)

# Initialize basic vars
home = '/usr/users/nigel.hartman/'
folder = ""
if len(sys.argv) >= 2:
        folder = str(sys.argv[1])
if folder != 'plants' and folder !=  'other':
        sys.exit("ERROR: use parameter plants or other")

# define functions (iterator)
def batch_iterator(ds, batch_size=8192): # 2^13
        for i in ds:
                yield i["text"]

# Load the raw Dataset
print("Load Dataset")
dataset = load_dataset("text", data_files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'])#, streaming=True)#, split="train")
dataset = dataset["train"]
print("dataset_length=", str(len(dataset)))

setup_file = open(home + 'data/' + folder + '/03_setup.txt', "w")
setup_file.write("The 03_train_tokenizers_stats.csv was running on a subset of the big dataset with " + str(len(dataset)) + "lines and 512 nucleotides per line.\n")
setup_file.close()

stats_file = open(home + 'data/' + folder + '/03_train_tokenizers_stats.csv', "w")
stats_file.write("tokenizer_lines,start_time,end_time,duration\n")

# train different tokenizers on different number of lines
print("Train tokenizers on " + str(folder) + "model from 100k to 1M lines")
for sample in range(100000, 1500000+1, 100000):
	wandb.log({"sample": sample})
	begin_time = datetime.now()
	print("Start train tokenizer lines " + str(sample) + " at time " + str(begin_time))
	# Trim dataset
	sub_dataset = dataset.select((i for i in range(len(dataset)) if i < sample)) # 100k for testing
	print("dataset trimmed to " + str(len(sub_dataset)))
	
	# Create Tokenizer
	tokenizer = ByteLevelBPETokenizer() # old because no kmer anymore add_prefix_space=True) # add prefix space because dont wano have different words cause of leerzeichen
	tokenizer.train_from_iterator(batch_iterator(sub_dataset), length=len(sub_dataset), vocab_size=4096, min_frequency=2,special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'], show_progress=True)	

	end_time = datetime.now()
	stats_file.write(str(sample) +","+ str(begin_time) +","+ str(end_time) + "," + str(end_time-begin_time)+"\n")
	stats_file.flush()
	print("Training finished at " + str(end_time))
	# safe tokenizer
	os.mkdir(home + 'data/' + folder + '/vocabulary_'+str(sample))
	fast_tokenizer = PreTrainedTokenizerFast(tokenizer_object=tokenizer)
	fast_tokenizer.save_pretrained(home + 'data/' + folder + '/vocabulary_'+str(sample))
	print("Saved tokenizer lines " + str(sample))
stats_file.close()
wandb.finish()
