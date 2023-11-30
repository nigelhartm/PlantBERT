module load bedtools
bedtools getfasta -fi ~/data/finetune/01_oryza/all.masked.con -bed ~/data/finetune/01_oryza/no_tf.gff > ~/data/finetune/01_oryza/seq_no_tf.fna
