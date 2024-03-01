module load bedtools
bedtools getfasta -fi ~/data/finetune/GCF_000001735.4_TAIR10.1_genomic.fna -bed ~/data/finetune/no_tf.gff > ~/data/finetune/seq_no_tf.fna
