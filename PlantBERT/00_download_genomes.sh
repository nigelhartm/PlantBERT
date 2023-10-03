# NCBI genome browser
## https://www.ncbi.nlm.nih.gov/genome/browse
## 4 species for each
## break down to random 1 gb of both 


# PLANTS

## Arabidopsis thaliana
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/735/GCF_000001735.4_TAIR10.1/GCF_000001735.4_TAIR10.1_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_000001735.4_TAIR10.1_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_000001735.4_TAIR10.1_genomic.fna
rm ~/data/plants/GCF_000001735.4_TAIR10.1_genomic.fna

## Oriza sativa
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/853/525/GCA_018853525.1_TN1_rice_v1.0/GCA_018853525.1_TN1_rice_v1.0_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_018853525.1_TN1_rice_v1.0_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_018853525.1_TN1_rice_v1.0_genomic.fna
rm ~/data/plants/GCA_018853525.1_TN1_rice_v1.0_genomic.fna

## Zea mays
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/902/167/145/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna
rm ~/data/plants/GCF_902167145.1_Zm-B73-REFERENCE-NAM-5.0_genomic.fna

## Physcomitrium patens
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/425/GCF_000002425.4_Phypa_V3/GCF_000002425.4_Phypa_V3_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCF_000002425.4_Phypa_V3_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCF_000002425.4_Phypa_V3_genomic.fna
rm ~/data/plants/GCF_000002425.4_Phypa_V3_genomic.fna

## Arabidopsis arenosa
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/905/216/605/GCA_905216605.1_AARE701a/GCA_905216605.1_AARE701a_genomic.fna.gz -P ~/data/plants
gunzip ~/data/plants/GCA_905216605.1_AARE701a_genomic.fna.gz
python 01_prepare_genomes.py ~/data/plants/ GCA_905216605.1_AARE701a_genomic.fna
rm ~/data/plants/GCA_905216605.1_AARE701a_genomic.fna

# OTHER

## Mus Muculus
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.27_GRCm39/GCF_000001635.27_GRCm39_genomic.fna.gz -P ~/data/other
gunzip ~/data/other/GCF_000001635.27_GRCm39_genomic.fna.gz
python 01_prepare_genomes.py ~/data/other/ GCF_000001635.27_GRCm39_genomic.fna
rm ~/data/other/GCF_000001635.27_GRCm39_genomic.fna

## Drosophila melanogaster
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/215/GCF_000001215.4_Release_6_plus_ISO1_MT/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna.gz -P ~/data/other
gunzip ~/data/other/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna.gz
python 01_prepare_genomes.py ~/data/other/ GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna 
rm ~/data/other/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna

## Homo sapiens
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.40_GRCh38.p14/GCF_000001405.40_GRCh38.p14_genomic.fna.gz -P ~/data/other
gunzip ~/data/other/GCF_000001405.40_GRCh38.p14_genomic.fna.gz
python 01_prepare_genomes.py ~/data/other/ GCF_000001405.40_GRCh38.p14_genomic.fna
rm ~/data/other/GCF_000001405.40_GRCh38.p14_genomic.fna

## Danio rerio
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/035/GCF_000002035.6_GRCz11/GCF_000002035.6_GRCz11_genomic.fna.gz -P ~/data/other
gunzip ~/data/other/GCF_000002035.6_GRCz11_genomic.fna.gz
python 01_prepare_genomes.py ~/data/other/ GCF_000002035.6_GRCz11_genomic.fna
rm ~/data/other/GCF_000002035.6_GRCz11_genomic.fna

## Caenorhabditis elegans
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/002/985/GCF_000002985.6_WBcel235/GCF_000002985.6_WBcel235_genomic.fna.gz -P ~/data/other
gunzip ~/data/other/GCF_000002985.6_WBcel235_genomic.fna.gz
python 01_prepare_genomes.py ~/data/other/ GCF_000002985.6_WBcel235_genomic.fna
rm ~/data/other/GCF_000002985.6_WBcel235_genomic.fna
