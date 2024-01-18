module load bedtools
bedtools getfasta -fi ~/data/finetune/00_arabidopsis/GCF_000001735.4_TAIR10.1_genomic.fna -bed ~/data/finetune/00_arabidopsis/no_tf.gff > ~/data/finetune/00_arabidopsis/seq_no_tf.fna
