#!/bin/bash

# 
echo "* Started 01_download_genomes.sh"

declare -a url_fna_gz



# Arabidopsis thaliana
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_000001735.4_TAIR10.1_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_000001735.4_TAIR10.1_genomic.fna
# Oriza sativa
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/853/525/GCA_018853525.1_TN1_rice_v1.0/GCA_018853525.1_TN1_rice_v1.0_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_018853525.1_TN1_rice_v1.0_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_018853525.1_TN1_rice_v1.0_genomic.fna
# Zea mays
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/902/167/145/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna
# Physcomitrium patens
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/425/GCF_000002425.4_Phypa_V3/GCF_000002425.4_Phypa_V3_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_000002425.4_Phypa_V3_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_000002425.4_Phypa_V3_genomic.fna
# Arabidopsis arenosa
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/905/216/605/GCA_905216605.1_AARE701a/GCA_905216605.1_AARE701a_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_905216605.1_AARE701a_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_905216605.1_AARE701a_genomic.fna
# Cucumis sativus
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/163/735/GCA_016163735.1_Cu2_PacBio_assembly/GCA_016163735.1_Cu2_PacBio_assembly_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_016163735.1_Cu2_PacBio_assembly_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_016163735.1_Cu2_PacBio_assembly_genomic.fna
# Gillenia trifoliata
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/257/905/GCA_018257905.1_V1/GCA_018257905.1_V1_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_018257905.1_V1_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_018257905.1_V1_genomic.fna
# Glycine max
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/020/497/155/GCA_020497155.1_ASM2049715v1/GCA_020497155.1_ASM2049715v1_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_020497155.1_ASM2049715v1_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_020497155.1_ASM2049715v1_genomic.fna
# Phaseolus vulgaris
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/015/708/805/GCA_015708805.1_OAC-Rex_P_vulgaris/GCA_015708805.1_OAC-Rex_P_vulgaris_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_015708805.1_OAC-Rex_P_vulgaris_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_015708805.1_OAC-Rex_P_vulgaris_genomic.fna
