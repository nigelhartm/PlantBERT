echo "STEP: 00_download_genomes.sh"
bash 00_download_genomes.sh
echo "STEP: 02_put_together.py"
python 02_put_together.py
echo "STEP: 03_tokenizer_bpe.py"
python 03_tokenizer_bpe.py
echo "NOT Done because harder to debug STEP: 04_tokenize_data.py"
#python 04_tokenize_data.py plants
