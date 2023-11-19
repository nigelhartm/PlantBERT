# PlantBERT

![alt_text](img/logo.jpeg)

(for debugging -> else build pipeline with checkpoints and automatic restart)

## 1: run and wait for resources
sbash reserve_slurm.sh

## 2: connect to reserved node and run
squeue --user=nigel.hartman
ssh {node name}
sh run.sh
