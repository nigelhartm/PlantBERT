#!/bin/bash
#SBATCH -p gpu
#SBATCH -G gtx1080:2
#SBATCH -C scratch
#SBATCH -t 2-00:00:00

watch -n 30 free -m
