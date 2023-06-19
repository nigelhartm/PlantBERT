# ArabidopsisBERT
Masterthesis Bioinformatics

## Setup enivronment
```
# delete old conda environment
conda remove -n dnabert --all

# this one works! https://hackmd.io/@absrocks/Bk0JWsr4j
conda create --name dnabert python=3.6
conda activate dnabert

# on edward
conda config --set ssl_verify false 

# depends on computer 11.8 on home pc and 11.4 on edward
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# building wheel for pybed tools failed / preinstalled on edward
sudo apt install gcc
sudo apt-get install g++

# new working directory
mkdir working_dir
cd working_dir

# clone DNABERT
git clone https://github.com/jerryji1993/DNABERT

# on edward before because error seqeval in fetch build egg raise distutilserror(str(e)) from e
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org setuptools_scm

# install DNABERT requirements
# on edward after pip install add  --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org 
cd DNABERT
python3 -m pip install --editable .
cd examples
python3 -m pip install -r requirements.txt
```

## Create pretrain data
```
# Download
cd examples
mkdir arabidopsis
cd arabidopsis
wget https://www.arabidopsis.org/download_files/Sequences/Assemblies/TAIR9_chr_all.fas

# Format
python format_pretrain.py
python kmer_pretrain.py
```

## on edward error OSError:model name 'dna6' was not found
solution is reaticng directory data/6mer
```
wget https://raw.githubusercontent.com/jerryji1993/DNABERT/master/src/transformers/dnabert-config/bert-config-6/vocab.txt
```
and instead dna6 in pretrain parameter put path there

## run pretrain
```
cd DNABERT/examples

export KMER=6
export TRAIN_FILE=arabidopsis/6mer_formatted_TAIR9_chr_all.fas
export TEST_FILE=arabidopsis/6mer_formatted_TAIR9_chr_all.fas
export SOURCE=~/git/ArabidopsisBERT/working_dir/DNABERT
export OUTPUT_PATH=output$KMER

python run_pretrain.py \
    --output_dir $OUTPUT_PATH \
    --model_type=dna \
    --tokenizer_name=dna$KMER \
    --config_name=$SOURCE/src/transformers/dnabert-config/bert-config-$KMER/config.json \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --do_eval \
    --eval_data_file=$TEST_FILE \
    --mlm \
    --gradient_accumulation_steps 25 \
    --per_gpu_train_batch_size 10 \
    --per_gpu_eval_batch_size 6 \
    --save_steps 500 \
    --save_total_limit 20 \
    --max_steps 200000 \
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
