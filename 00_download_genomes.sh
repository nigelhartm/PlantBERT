#!/bin/bash

# Status
echo "* Started 00_download_genomes.sh"

# Array with urls to the genome files
declare -a url_fna_gz
url_fna_gz[0]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz" # Arabidopsis thaliana
url_fna_gz[1]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/853/525/GCA_018853525.1_TN1_rice_v1.0/GCA_018853525.1_TN1_rice_v1.0_genomic.fna.gz" # Oriza sativa
url_fna_gz[2]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/902/167/145/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz" # Zea mays
url_fna_gz[3]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/425/GCF_000002425.4_Phypa_V3/GCF_000002425.4_Phypa_V3_genomic.fna.gz" # Physcomitrium patens
url_fna_gz[4]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/905/216/605/GCA_905216605.1_AARE701a/GCA_905216605.1_AARE701a_genomic.fna.gz" # Arabidopsis arenosa
url_fna_gz[5]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/163/735/GCA_016163735.1_Cu2_PacBio_assembly/GCA_016163735.1_Cu2_PacBio_assembly_genomic.fna.gz" # Cucumis sativus
url_fna_gz[6]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/257/905/GCA_018257905.1_V1/GCA_018257905.1_V1_genomic.fna.gz" # Gillenia trifoliata
url_fna_gz[7]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/020/497/155/GCA_020497155.1_ASM2049715v1/GCA_020497155.1_ASM2049715v1_genomic.fna.gz" # Glycine max
url_fna_gz[8]="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/015/708/805/GCA_015708805.1_OAC-Rex_P_vulgaris/GCA_015708805.1_OAC-Rex_P_vulgaris_genomic.fna.gz" # Phaseolus vulgaris

# Loop over all urls
for (( i=0; i<${#url_fna_gz[@]}; i++ ));
do
        wget ${url_fna_gz[$i]} -P ~/data/plants # download into users local data folder
        gunzip "~/data/plants/$(basename ${url_fna_gz[$i]})" # unpack into users local data folder
        python 01_prepare_genomes.py ~/data/plants/ GCF_000001735.4_TAIR10.1_genomic.fna # call genome cleaning and sampling script
done