# Import Libraries
import glob
import sys
import random

# Declare variables
folder = None

# Check for parameters
if len(sys.argv) > 2:
	folder = str(sys.argv[1])
else
	sys.exit("Error: Mistake during call of 02_put_together.py. Expected parameters not provided. [1] = data folder;")

# Open Filestreams
in_files = []
out_file = open('/usr/users/nigel.hartman/data/' + folder + '/all_sample_' + folder + '.fna', 'w')

# Loop over all files
for file in glob.glob('/usr/users/nigel.hartman/data/' + folder + '/sample_*.fna'):
	in_files.append(open(file, 'r'))
	while len(in_files) >= 1:
		file = random.randint(0, len(in_files)-1)
		line = in_files[file].readline()
		if line:
			out_file.write(line)
		else:
			print('File finished.')
			in_files.pop(file)
