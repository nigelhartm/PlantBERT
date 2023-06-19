# ArabidopsisBERT
Masterthesis Bioinformatics

## Setup enivronment
```
# delete old conda environment
conda remove -n dnabert --all

# this one works! https://hackmd.io/@absrocks/Bk0JWsr4j
conda create --name dnabert python=3.6
conda activate dnabert
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# building wheel for pybed tools failed
sudo apt install gcc
sudo apt-get install g++

# new working directory
mkdir working_dir
cd working_dir

# clone DNABERT
git clone https://github.com/jerryji1993/DNABERT

# install DNABERT requirements
cd DNABERT
python3 -m pip install --editable .
cd examples
python3 -m pip install -r requirements.txt
```

## Create pretrain data
```
# Download
mkdir arabidopsis
cd arabidopsis
wget https://www.arabidopsis.org/download_files/Sequences/Assemblies/TAIR9_chr_all.fas

# Format
python format_pretrain.py
python kmer_pretrain.py
```

## run pretrain
```
cd DNABERT/examples

export KMER=6
export MODEL_PATH=PATH_TO_THE_PRETRAINED_MODEL
export DATA_PATH=sample_data/ft/$KMER
export OUTPUT_PATH=./ft/$KMER

python run_pretrain.py \
    --output_dir $OUTPUT_PATH \
    --model_type=dna \
    --tokenizer_name=dna$KMER \
    --config_name=$SOURCE/src/transformers/dnabert-config/bert-config-$KMER/config.json \
    --do_train \
    --train_data_file=$PATH_ARA$KMER$TRAIN_FILE \
    --do_eval \
    --eval_data_file=$PATH_ARA$KMER$TEST_FILE \
    --mlm \
    --gradient_accumulation_steps 25 \
    --per_gpu_train_batch_size 10 \
    --per_gpu_eval_batch_size 6 \
    --save_steps 500 \
    --save_total_limit 20 \
    --max_steps 1000 \
    --evaluate_during_training \
    --logging_steps 500 \
    --line_by_line \
    --learning_rate 4e-4 \
    --block_size 512 \
    --adam_epsilon 1e-6 \
    --weight_decay 0.01 \
    --beta1 0.9 \
    --beta2 0.98 \
    --mlm_probability 0.025 \
    --warmup_steps 10000 \
    --overwrite_output_dir \
    --n_process 24
```
