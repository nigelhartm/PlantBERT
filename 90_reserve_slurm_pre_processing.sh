#!/bin/bash
#SBATCH -p medium
#SBATCH -c 30
#SBATCH --mem-per-cpu 4G
#SBATCH -C scratch
#SBATCH --qos=long
#SBATCH -t 5-00:00:00

watch -n 30 free -m
