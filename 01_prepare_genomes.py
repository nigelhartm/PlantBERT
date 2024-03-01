# Import Libraries
import sys
import os
import random

# Status
print("* Started 01_prepare_genomes.py")
print("Warning: This script is planned to get started automatically by the 00_download_genomes.sh script")

# Declare variables
folder = None
file_name = None

# Check for parameters
if len(sys.argv) > 2:
        folder = str(sys.argv[1])
        file_name = str(sys.argv[2])
else:
        sys.exit("Error: Mistake during call of 01_prepare_genomes.py. Expected parameters not provided. [1] = data folder; [2] = file name")

# Open Filestreams
in_file = open(folder + file_name, 'r') # READ
out_file = open(folder + 'sample_' + str(file_name), 'w') # WRITE

# Initialize Variables
buf = ''
kmer = 6
seq_len = 512

# Go through file line by line
line = in_file.readline()
while line:
        # Check if line contains data
        if not line.startswith('>'):
                buf += line
                buf = buf.upper().replace('N', '').replace('.', '').replace('\n', '').replace(' ', '')
        # No data line
        else:
                buf = ''
        # Is our buffer full?
        if len(buf) >= seq_len:
                # Write buffer to file
                out_file.write(buf[0:seq_len] + "\n")
                buf = buf[seq_len:len(buf)]
        # Read a new line
        line = in_file.readline()

# Close files
in_file.close()
out_file.close()

# Status
print("* Finished 01_prepare_genomes.py")