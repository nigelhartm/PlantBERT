#!/bin/bash

if [ "$1" = "plants" ] || [ "$1" = "other" ]
then
	echo "STEP: 00_download_genomes.sh"
	bash 00_download_genomes.sh $1
	echo "STEP: 02_put_together.py"
	python 02_put_together.py $1
	echo "STEP: 03_tokenizer_bpe.py"
	python 03_tokenizer_bpe.py $1
	echo "STEP: 04_tokenize_data.py"
	python 04_tokenize_data_map_dataset.py $1
else
	echo "ERROR: parameter not existing (eg. plants or other)"
fi
