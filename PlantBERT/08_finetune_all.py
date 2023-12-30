print("import libraries")
import os
os.environ["WANDB_PROJECT"] = "plantbert_finetune_all"

import datasets as ds
import torch
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
import evaluate

print("load metrics")
metric = evaluate.load("accuracy")
def compute_metrics(eval_pred):
        logits, labels = eval_pred
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

print("load datasets")
dataset = ds.load_from_disk("/usr/users/nigel.hartman/data/plants/mapped_dataset_finetune_all")
dataset.set_format("torch")

print("load model")
model = AutoModelForSequenceClassification.from_pretrained("/usr/users/nigel.hartman/data/plants/model_final", num_labels=2)

training_args = TrainingArguments(
	output_dir="/usr/users/nigel.hartman/data/plants/TrainingArguments_finetune_all",          # output directory
	overwrite_output_dir = True,
	evaluation_strategy="steps",
	eval_steps=3,
	num_train_epochs=2,              # total number of training epochs
	per_device_train_batch_size=64,  # batch size per device during training
	per_device_eval_batch_size=64,   # batch size for evaluation
	warmup_steps=0,                # number of warmup steps for learning rate scheduler
	weight_decay=0.005,               # strength of weight decay
	logging_dir='/usr/users/nigel.hartman/data/logs'            # directory for storing logs
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.save_model("/usr/users/nigel.hartman/data/plants/model_finetune_all")

# acc on test plants
test_predictions = trainer.predict(dataset["test"])
test_predictions_argmax = np.argmax(test_predictions[0], axis=1)
test_references = np.array(dataset["test"]["labels"])
acc = metric.compute(predictions=test_predictions_argmax, references=test_references)
print("Acc on test data plants " + str(acc))

# acc on test gue
gue_dataset = ds.load_from_disk("/usr/users/nigel.hartman/data/plants/mapped_dataset_finetune_all_gue")
gue_dataset.set_format("torch")
gue_test_predictions = trainer.predict(gue_dataset["test"])
gue_test_predictions_argmax = np.argmax(gue_test_predictions[0], axis=1)
gue_test_references = np.array(gue_dataset["test"]["labels"])
gue_acc = metric.compute(predictions=gue_test_predictions_argmax, references=gue_test_references)
print("Acc on test data GUE " + str(gue_acc))

