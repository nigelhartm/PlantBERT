import requests
import ssl

# ssl verified error cause vpn network
ssl._create_default_https_context = ssl._create_unverified_context

downloads = {
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/735/GCA_000001735.2_TAIR10.1/GCA_000001735.2_TAIR10.1_genomic.fna.gz',
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/211/275/GCA_000211275.1_ASM21127v1/GCA_000211275.1_ASM21127v1_genomic.fna.gz',
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/020/911/765/GCA_020911765.2_ASM2091176v2/GCA_020911765.2_ASM2091176v2_genomic.fna.gz',
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/660/825/GCA_900660825.1_Ath.Ler-0.MPIPZ.v1.0/GCA_900660825.1_Ath.Ler-0.MPIPZ.v1.0_genomic.fna.gz',
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/903/064/275/GCA_903064275.1_AT7213.Ler-0.PacBio/GCA_903064275.1_AT7213.Ler-0.PacBio_genomic.fna.gz',
'https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/902/825/305/GCA_902825305.1_AT6909.Col-0.PacBio/GCA_902825305.1_AT6909.Col-0.PacBio_genomic.fna.gz'
}

# get
i = 0
for element in downloads:
    	i+=1
    	print('download: ' + str(element))
    	page = requests.get(element, allow_redirects=True)
    	open('fnagz/' + str(i) + '.fna.gz', 'wb').write(page.content)
