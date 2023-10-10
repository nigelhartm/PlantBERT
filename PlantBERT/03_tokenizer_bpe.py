from tokenizers import ByteLevelBPETokenizer
import os

home = '/usr/users/nigel.hartman/'

for folder in ['plants', 'other']:
	tokenizer = ByteLevelBPETokenizer(add_prefix_space=True) # add prefix space because dont wano have different words cause of leerzeichen
	tokenizer.train(files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'], vocab_size=4096, min_frequency=2,special_tokens=['[UNK]', '[CLS]', '[SEP]', '[PAD]', '[MASK]'])
	os.mkdir(home + 'data/' + folder + '/vocabulary')
	tokenizer.save_model(home + 'data/' + folder + '/vocabulary')
