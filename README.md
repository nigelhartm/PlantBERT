# ArabidopsisBERT
Masterthesis Bioinformatics

## Setup enivronment
```
# delete old conda environment<br>
conda remove -n dnabert --all<br>

# create new conda enivronment
conda create -n dnabert python=3.6
conda activate dnabert

# this one works! https://hackmd.io/@absrocks/Bk0JWsr4j
conda create --name torch-cuda python=3.7
conda activate torch-cuda
conda install -c "nvidia/label/cuda-11.7.0" cuda-toolkit
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

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
