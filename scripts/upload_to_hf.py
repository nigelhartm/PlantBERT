# first you need to login via token with huggingface-cli login
import transformers
import torch
model = transformers.BertForMaskedLM.from_pretrained("/usr/users/nigel.hartman/data/plants/model_final")
tokenizer = transformers.PreTrainedTokenizerFast.from_pretrained("/usr/users/nigel.hartman/data/plants/vocabulary_final", max_len=128)
model.push_to_hub("plantbert")
tokenizer.push_to_hub("plantbert")
