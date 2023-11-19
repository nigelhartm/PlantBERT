from tokenizers import ByteLevelBPETokenizer
import os
import sys

home = '/usr/users/nigel.hartman/'

folder = ""

if len(sys.argv) >= 2:
        folder = str(sys.argv[1])
if folder != 'plants' and folder !=  'other':
        sys.exit("ERROR: use parameter plants or other")

tokenizer = ByteLevelBPETokenizer(add_prefix_space=True) # add prefix space because dont wano have different words cause of leerzeichen
tokenizer.train(files=[home + 'data/' + folder + '/all_sample_' + folder + '.fna'], vocab_size=4096, min_frequency=2,special_tokens=['<s>', '<pad>', '</s>', '<unk>', '<mask>'])
os.mkdir(home + 'data/' + folder + '/vocabulary')
tokenizer.save_model(home + 'data/' + folder + '/vocabulary')
