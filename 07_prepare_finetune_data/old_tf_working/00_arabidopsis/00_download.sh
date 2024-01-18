wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz -P ~/data/finetune/00_arabidopsis
gunzip -d ~/data/finetune/00_arabidopsis/GCF_000001735.4_TAIR10.1_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.gff.gz -P ~/data/finetune/00_arabidopsis
gunzip -d ~/data/finetune/00_arabidopsis/GCF_000001735.4_TAIR10.1_genomic.gff.gz
wget http://planttfdb.gao-lab.org/download/seq/Ath_cds.fas.gz -P ~/data/finetune/00_arabidopsis
gunzip -d ~/data/finetune/00_arabidopsis/Ath_cds.fas.gz
