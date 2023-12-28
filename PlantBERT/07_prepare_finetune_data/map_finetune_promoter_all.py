print("ipmort libs")
import datasets as ds
from transformers import PreTrainedTokenizerFast

print("load data")
column_names = ['text', 'labels']
dataset = ds.load_dataset("csv", data_files={"train": ['/usr/users/nigel.hartman/data/plants/finetune_all.tsv']}, delimiter="\t", column_names=column_names)

print(dataset)

dataset_train_devtest = dataset["train"].train_test_split(test_size=0.3)

dataset_splits = ds.DatasetDict({
        "train": dataset_train_devtest["train"],
        "test": dataset_train_devtest["test"]
})

print(dataset_splits)

tokenizer = PreTrainedTokenizerFast.from_pretrained("/usr/users/nigel.hartman/data/plants/vocabulary_final", max_len=128) # special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
tokenizer.add_special_tokens({'pad_token': '<pad>'})

m_dataset = dataset_splits.map(lambda examples: tokenizer(examples["text"], return_tensors="pt", max_length = 128, padding = 'max_length', truncation = True), batched=True)

print(m_dataset)
m_dataset.save_to_disk("/usr/users/nigel.hartman/data/plants/mapped_dataset_finetune_promoter_all")

