# PlantBERT

![alt_text](img/logo.jpeg)

## 1: run and wait for resources
sbash 90_reserve_slurm_pre_processing.sh<br>
screen -S ...<br>
ssh ...<br>
srun -p medium -c 30 --mem-per-cpu 4G -t 5-00:00:00 --pty bash<br>
sh 90_run_pre_processing.sh
<br>
sbash 91_reserve_slurm_pre_training.sh<br>
screen -S ... <br>
ssh ...<br>
srun -p gpu -G v100:8 -t 5-00:00:00 --pty bash<br>
python 05_tokenize_data_map_dataset.py plants<br>
python 06_pretrain.py plants<br>
<br> 
