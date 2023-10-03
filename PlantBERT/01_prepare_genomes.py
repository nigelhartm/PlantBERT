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
rand_len = random.randint(5, 512)
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
                rand_len = random.randint(5, 512)
                if(random.random() < ratio):
                        out_file.write(buf[0:rand_len] + "\n")
                buf = buf[rand_len:len(buf)]
        line = in_file.readline()
in_file.close()
out_file.close()
print('finished script. * * *')
