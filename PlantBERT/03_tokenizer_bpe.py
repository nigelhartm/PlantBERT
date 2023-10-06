from tokenizers import ByteLevelBPETokenizer
import os

home = '/usr/users/nigel.hartman/'

for folder in ['plants', 'other']:
	tokenizer = ByteLevelBPETokenizer(add_prefix_space=True) # add prefix space because dont wano have different words cause of leerzeichen
	tokenizer.train(files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'], vocab_size=30_522, min_frequency=2,special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
	os.mkdir(home + 'data/' + folder + '/vocabulary')
	tokenizer.save_model(home + 'data/' + folder + '/vocabulary')
