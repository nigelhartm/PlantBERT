import glob
import sys
import random

for folder in ['plants', 'other']:
        in_files = []
        out_file = open('/usr/users/nigel.hartman/data/' + folder + '/all_sample_' + folder + '.fna', 'w')
        for file in glob.glob('/usr/users/nigel.hartman/data/' + folder + '/sample_*.fna'):
                in_files.append(open(file, 'r'))
        while len(in_files) >= 1:
                file = random.randint(0, len(in_files)-1)
                line = in_files[file].readline()
                if line:
                        out_file.write(line)
                else:
                        print('File finished')
                        in_files.pop(file)
