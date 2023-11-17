# Import Libraries
print("import libraries")
#import torch
from transformers import PreTrainedTokenizerFast
import sys
from datasets import load_dataset
from datetime import datetime

# Initialize variables
print("init variables")
home = '/usr/users/nigel.hartman/'
model_type = ""

if len(sys.argv) >= 2:
	model_type = str(sys.argv[1])
if model_type != "plants" and model_type != "other":
	sys.exit("ERROR! Set a model type parameter eg. plants or other")

# Load tokenizer
#print("load tokenizer")
#tokenizer = PreTrainedTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary/')#vocab.json', home+'data/'+model_type+'/vocabulary/merges.txt')#,max_len=512)
#tokenizer = BertTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary', max_len=512)

# Load unprocessed dataset
print("Load unprocessed dataset")
dataset = load_dataset("text", data_files={"train": [home + 'data/'+ model_type +'/all_sample_'+model_type+'.fna']})
dataset = dataset["train"]

stats_file = open(home+'data/'+model_type+'/04_evaluate.csv', 'w')
stats_file.write("tokenizer_lines,unk_cnt,token_cnt,max_token_line,min_token_line,lines_smaller_eq_128_token,lines_bigger_eq_64_token,eval_duration\n")

for sample in range(100000, 1500000+1, 100000):
	print("Evaluiere tokenizer_"+str(sample))
	#
	begin_time = datetime.now()
	print("load tokenizer")
	tokenizer = PreTrainedTokenizerFast.from_pretrained(home+'data/'+model_type+'/vocabulary_'+str(sample) + '/')
	#
	unk_cnt = 0
	token_cnt = 0
	max_token_line = 0
	lines_smaller_eq_128_token = 0
	lines_bigger_eq_64_token = 0
	min_token_line = 10000000
	for i in range(0, len(dataset)):
		if i%100000==0:
			print("|", end="")
		data = dataset[i]["text"]
		enc_data = tokenizer.encode(data)
		token_cnt += len(enc_data)
		if(len(enc_data)>max_token_line):
			max_token_line = len(enc_data)
		if(len(enc_data)<min_token_line):
			min_token_line = len(enc_data)
		if(len(enc_data)<=128):
			lines_smaller_eq_128_token += 1
		if(len(enc_data)>=64):
			lines_bigger_eq_64_token += 1
		for j in range(0, len(enc_data)):
			if(enc_data[j] == 3):
				unk_cnt += 1
	print("Finished.")
	end_time=datetime.now()
	duration = end_time-begin_time
	stats_file.write(str(sample) + "," + str(unk_cnt) + "," + str(token_cnt) + "," + str(max_token_line) + "," + str(min_token_line) + "," + str(lines_smaller_eq_128_token) + "," + str(lines_bigger_eq_64_token) + "," + str(duration) + "\n")
	stats_file.flush()
stats_file.close()
