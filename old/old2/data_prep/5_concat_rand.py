# Import libraries
import glob
import sys
import random

# Predefine variables
data_src = None
out_file = None
in_files = []

# Read parameters from command line
try:
	data_src = str(sys.argv[1])
	if data_src != 'train' and data_src != 'test':
		raise Exception()
	out_file = open(str(sys.argv[2]), 'w')
except:
	exit('ERROR: Wrong arguments\n[1] = train | test\n[2] = dst_file_name.fna\n')

for file in glob.glob('sampled_kmers_' + str(data_src) + "/*.fna"):
	in_files.append(open(file, 'r'))

while len(in_files) >= 1:
	file = random.randint(0, len(in_files)-1)
	line = in_files[file].readline()
	if line:
		out_file.write(line)
	else:
		print('File empty')
		in_files.pop(file)
