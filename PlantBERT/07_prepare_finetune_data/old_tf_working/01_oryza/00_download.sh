wget http://rice.uga.edu/pub/data/Eukaryotic_Projects/o_sativa/annotation_dbs/pseudomolecules/version_7.0/all.dir/all.masked.con.gz -P ~/data/finetune/01_oryza
gunzip -d ~/data/finetune/01_oryza/all.masked.con.gz
wget http://rice.uga.edu/pub/data/Eukaryotic_Projects/o_sativa/annotation_dbs/pseudomolecules/version_7.0/all.dir/all.gff3 -P ~/data/finetune/01_oryza
#gunzip -d ~/data/finetune/00_arabidopsis/GCF_000001735.4_TAIR10.1_genomic.gff.gz
wget http://planttfdb.gao-lab.org/download/seq/Osj_cds.fas.gz -P ~/data/finetune/01_oryza
gunzip -d ~/data/finetune/01_oryza/Osj_cds.fas.gz
