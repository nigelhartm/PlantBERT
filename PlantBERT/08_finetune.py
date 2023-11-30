

print("import datasets")
import datasets as ds

print("import torch")
import torch
print("GPU test:")
print(torch.cuda.is_available())
print(torch.cuda.device_count())
from transformers import AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer
import numpy as np
import evaluate

print("load datasets")
dataset = ds.load_from_disk("/usr/users/nigel.hartman/data/plants/mapped_dataset_finetune")
dataset.set_format("torch")
#print(dataset)

train_dataset = dataset["train"]
eval_dataset = dataset["test"]

#print("Build Dataloader . . .")
#train_dataloader = torch.utils.data.DataLoader(dataset["train"], batch_size=128, shuffle=True) # 512 + 128
#test_dataloader = torch.utils.data.DataLoader(dataset["test"], batch_size=128, shuffle=True)

print("load model")
model = AutoModelForSequenceClassification.from_pretrained("/usr/users/nigel.hartman/data/plants/model_final", num_labels=2)

training_args = TrainingArguments(
	output_dir="/usr/users/nigel.hartman/data/plants/TrainingArguments_finetune",          # output directory
	evaluation_strategy="epoch",
	num_train_epochs=25,              # total number of training epochs
	per_device_train_batch_size=128,  # batch size per device during training
	per_device_eval_batch_size=32,   # batch size for evaluation
	warmup_steps=32,                # number of warmup steps for learning rate scheduler
	weight_decay=0.01,               # strength of weight decay
	logging_dir='/usr/users/nigel.hartman/data/logs',            # directory for storing logs
	logging_steps=10,
)

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
	logits, labels = eval_pred
	predictions = np.argmax(logits, axis=-1)
	return metric.compute(predictions=predictions, references=labels)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()
# maybe here you can upload to huggingface automatically?
trainer.save_model("/usr/users/nigel.hartman/data/plants/model_finetuned_tf")
















"""
import wandb


wandb.init(
        # set the wandb project where this run will be logged
        project="plantbert_finetune",
        name="plantbert_finetune_v1",
        # track hyperparameters and run metadata
        config={
        "learning_rate": 1e-5,
        "architecture": "BERT",
        "dataset": "plantbert",
        "epochs": 100
        }
)

print("load optimizer")
from torch.optim import AdamW
optimizer = AdamW(model.parameters(), lr=5e-5)

print("scheduler")
from transformers import get_scheduler
num_epochs = 100
num_training_steps = num_epochs * len(train_dataloader)
lr_scheduler = get_scheduler(
    name="linear", optimizer=optimizer, num_warmup_steps=0, num_training_steps=num_training_steps
)

print("to cuda device")
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model.to(device)

#print("start train mode")
model.train()

from tqdm import tqdm

print("train loop")
for epoch in range(num_epochs):
	loop = tqdm(train_dataloader, leave=True)
	for batch in loop:
		optimizer.zero_grad()
		input_ids = batch["input_ids"].to(device)
		token_type_ids = batch["token_type_ids"].to(device)
		attention_mask = batch["attention_mask"].to(device)
		labels = batch["labels"].to(device)
		outputs = model(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask, labels=labels)
		loss = outputs.loss
		loss.backward()
		optimizer.step()
		loop.set_description(f'Epoch {epoch}')
		loop.set_postfix(loss=loss.item())
		wandb.log({"loss": loss.item()})
"""
