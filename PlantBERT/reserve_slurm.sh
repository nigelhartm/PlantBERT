#!/bin/bash
#SBATCH -p gpu
#SBATCH -G v100:8
#SBATCH -C scratch
#SBATCH --qos=long
#SBATCH -t 5-00:00:00

watch -n 30 free -m
