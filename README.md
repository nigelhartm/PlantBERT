# PlantBERT

![alt_text](img/logo_small.jpeg)

## Abstract
The impact of transformer architecture on natural language processing has inspired innovative applications in various domains. There are already various large language models for biological data, such as DNABERT2, majorly focussing on human and animal data. However, the model for plants does not exist. Therefore we developed a specialized model, PlantBERT, uniquely designed for the plant genome. By utilizing cutting-edge methods, the model showed promising results in the pre-training phase, with high accuracy, compared to DNABERT2. Further fine-tuning both models for a binary classification task was focused on plant promoter detection, demonstrating the models efficiency in addressing domain-specific challenges. With just half the model size, PlantBERT yielded results in this task that were similar to those of DNABERT2. This shows the necessity for the model tailored to the plant genome. This study not only shows the practicality of constructing PlantBERT but also establishes a robust foundation for future research. The accomplishment expands the plant genomics research and emphasizes the potential of tailored language models in specialized scientific domains. PlantBERT provides advancements in our understanding of plant genomic sequences and establishes a foundation for continuous innovation in the field.

## Huggingface
Our model is available at hugging-face https://huggingface.co/nigelhartm/PlantBERT/

## How to use?
The training and evaluation of the model was succesful. This repository still needs some make-over, until then I recommend to directly download my pre-trained model from hugging-face for fine-tuning. The enviroment.yml is overloaded as well, in the usual case you will have not many dependencies. Installing the transformers library should be enough, to load the model.

```
# Import libraries
from transformers import AutoTokenizer, AutoModelForMaskedLM

# load pre-trained model
tokenizer = AutoTokenizer.from_pretrained("nigelhartm/PlantBERT")
model = AutoModelForMaskedLM.from_pretrained("nigelhartm/PlantBERT")

# tokenize a sequence
dna = "ACGTAGCATCGGATCTATCTATCGACACTTGGTTATCGATCTACGAGCATCTCGTTAGC"
inputs = tokenizer(dna, return_tensors = 'pt')["input_ids"]

# mask some input 4 = "<mask>" . . . 5 is the position we mask
inputs_masked = inputs.clone().detach()
inputs_masked[0][5] = 4

# get the logit outputs
logits = model(inputs_masked).logits
```
More examples how to use the model and finetune it can be found in the fine_tuning.py script.

## More information
I performed the training of this model during my Masterthesis in Bioinformatics. I tried to make it similar to DNABERT2, for evaluation. In the end we got a model with half of the DNABERT2 parameter number. It performed significantly better in the token prediction challenge after pre-training on a plant genome dataset (30% vs 5% acc). We fine-tuned our model to predict, plant promoter regions. Our model performed similar, to DNABERT2 (with just half of the size).
