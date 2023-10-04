import sys
import os
import random

print('* * * Started 01_... python script.')
folder = str(sys.argv[1])
file = str(sys.argv[2])
in_file = open(folder + file, 'r')
out_file = open(folder + 'sample_' + str(file), 'w')

file_stats = os.stat(folder + file)

ratio = (1 / (int(file_stats.st_size) / 150000000))
buf = ''
kmer = 6
rand_len = random.randrange(6, 513, kmer)
line = in_file.readline()
while line:
        if not line.startswith('>'):
                buf += line
                buf = buf.upper()
                buf = buf.replace('N', '')
                buf = buf.replace('.', '')
                buf = buf.replace('\n', '')
                buf = buf.replace(' ', '')
        if len(buf) >= rand_len:
                if(random.random() < ratio):
                        for j in range(0, rand_len, kmer):
                                out_file.write(buf[j:j+kmer] + " ")
                        out_file.write("\n")
                        #out_file.write(buf[0:rand_len] + "\n")
                buf = buf[rand_len:len(buf)]
                rand_len = random.randrange(6, 513, kmer)
        line = in_file.readline()
in_file.close()
out_file.close()
print('finished script. * * *')
