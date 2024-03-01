# Import Libraries
import sys
import os
import random

# Status: Start
print('* Started 01_... python script.')

# Declare variables
folder = None
file_name = None

# Check for parameters
if len(sys.argv) > 2:
        folder = str(sys.argv[1])
        file_name = str(sys.argv[2])
else:
        sys.exit("")

in_file = open(folder + file_name, 'r')
out_file = open(folder + 'sample_' + str(file_name), 'w')

#file_stats = os.stat(folder + file)

#ratio = (1 / (int(file_stats.st_size) / 150000000))
buf = ''
kmer = 6
rand_len = 512 # dont use random length anymore flash attention 2 has no padding random.randrange(6, 513, kmer)
line = in_file.readline()
while line:
        if not line.startswith('>'):
                buf += line
                buf = buf.upper()
                buf = buf.replace('N', '')
                buf = buf.replace('.', '')
                buf = buf.replace('\n', '')
                buf = buf.replace(' ', '')
        else:
                buf = ''
        if len(buf) >= rand_len:
                # dont trim down the data ... if(random.random() < ratio):
                #for j in range(0, rand_len, kmer):
                #        out_file.write(buf[j:j+kmer] + "") # dont use kmer !!!??? # wrong length per line with kmer because 512/6 is not even
                out_file.write(buf[0:rand_len] + "\n")
		#out_file.write("\n")
                #out_file.write(buf[0:rand_len] + "\n")
                buf = buf[rand_len:len(buf)]
                #rand_len = random.randrange(6, 513, kmer)
        line = in_file.readline()
in_file.close()
out_file.close()

# Status: End
print('finished script. * * *')