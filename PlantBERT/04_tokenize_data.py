home = '/usr/users/nigel.hartman/'

from transformers import RobertaTokenizer

tokenizer = RobertaTokenizer.from_pretrained(home+'data/plants/vocabulary', max_len=512)

## Do some encoding test
print("\nTest encoding\n")

tokens = tokenizer('AAAAAA CCCCCC GGGGGG')

print('tokens')
print(tokens)
print('tokens.input_ids')
print(tokens.input_ids)

## encoding
print('\nstart encoding..\n')
print("read file")
in_file = open(home + 'data/plants/all_sample_plants.fna', 'r')
print("take lines")
lines = in_file.read().split('\n')
print("tokenize")
batch = tokenizer(lines, max_length = 512, padding = 'max_length', truncation = True)
print("len(batch)=" + str(len(batch)))

