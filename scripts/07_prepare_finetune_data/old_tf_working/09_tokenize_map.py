print("combine merges")
file_00 = open("/usr/users/nigel.hartman/data/finetune/00_arabidopsis/merged.csv", "r")
file_01 = open("/usr/users/nigel.hartman/data/finetune/01_oryza/merged.csv", "r")
# hier eine effizientere methode mit list einbauen
file_out = open("/usr/users/nigel.hartman/data/plants/finetune_tf.tsv", "w")
line = file_00.readline()
while line:
	file_out.write(line)
	line = file_00.readline()
line = file_01.readline()
while line:
        file_out.write(line)
        line = file_01.readline()
file_00.close()
file_01.close()
file_out.close()

print("ipmort libs")
import datasets as ds

print("load data")
column_names = ['text', 'labels']
dataset = ds.load_dataset("csv", data_files={"train": ['/usr/users/nigel.hartman/data/plants/finetune_tf.tsv']}, delimiter="\t", column_names=column_names)

print(dataset)

dataset_train_devtest = dataset["train"].train_test_split(test_size=0.3)
#dataset_devtest = dataset_train_devtest["test"].train_test_split(test_size=0.5)

dataset_splits = ds.DatasetDict({
	"train": dataset_train_devtest["train"],
#	"valid": dataset_devtest["train"],
	"test": dataset_train_devtest["test"]
})

print(dataset_splits)
from transformers import PreTrainedTokenizerFast
tokenizer = PreTrainedTokenizerFast.from_pretrained("/usr/users/nigel.hartman/data/plants/vocabulary_final", max_len=128) # special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
tokenizer.add_special_tokens({'pad_token': '<pad>'})

m_dataset = dataset_splits.map(lambda examples: tokenizer(examples["text"], return_tensors="pt", max_length = 128, padding = 'max_length', truncation = True), batched=True)

print(m_dataset)
m_dataset.save_to_disk("/usr/users/nigel.hartman/data/plants/mapped_dataset_finetune")
