# Import libraries
import glob
import random
import re

# Initialize constants
KMER = 6

# Iterate all files
for file in glob.glob('formatted/*.fna'):
	file = file[file.find('/')+1:len(file)]
	print(file)
	in_file = open('formatted/' + str(file), 'r')
	out_file_train = open('sampled_kmers_train/' + str(file), 'w')
	out_file_test = open('sampled_kmers_test/' + str(file), 'w')
	buf = ''
	line = in_file.readline()
	# Read line by line
	while line:
		buf += line
		if len(buf) >= 512*KMER:
			rand_len = random.randint(5, 512)
			sample = buf[0:rand_len*KMER]
			buf = buf[rand_len*KMER:len(buf)]
			sample = ' '.join(re.findall('.'*KMER, sample))
			# Test 30 percent
			if random.random() >= 0.7:
				out_file_test.write(str(sample) + '\n')
			# Train 70 percent
			else:
				out_file_train.write(str(sample) + '\n')
		line = in_file.readline()
	# MISS SOME INFORMATION AT END
	# LETS ACCEPT THAT FIRST TO STAY SIMPLE
	in_file.close()
	out_file_train.close()
	out_file_test.close()
