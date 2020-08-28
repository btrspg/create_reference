# AUTOGENERATED! DO NOT EDIT! File to edit: 01_defaults.ipynb (unless otherwise specified).

__all__ = ['fasta_file_pattern', 'gtf_file_pattern', 'ensembl_ftp', 'species', 'softwares', 'defaults',
           'softwares_default']

# Cell

fasta_file_pattern='{species}.+?dna\..+?.fa.gz'
gtf_file_pattern='{species}.+?{version}.gtf.gz'


# Cell

ensembl_ftp='ftp.ensembl.org'

# Cell
species=['homo_sapiens',
'mus_musculus',
'rattus_norvegicus',
'caenorhabditis_elegans',
'equus_caballus',
'capra_hircus',
'drosophila_melanogaster',
'macaca_mulatta',
'ovis_aries',
'sus_scrofa',
'oryctolagus_cuniculus',
'bos_taurus',
'saccharomyces_cerevisiae',
'gallus_gallus',
'gasterosteus_aculeatus',
'danio_rerio',
'oryzias_latipes',
'anser_cygnoides',
'callithrix_jacchus',
'pan_troglodytes',
'pongo_abelii',
'meleagris_gallopavo',
'oreochromis_niloticus',
'bos_grunniens',
'phascolarctos_cinereus',
'salmo_salar',
'amphilophus_citrinellus',
'ciona_intestinalis',
'monodelphis_domestica',
'mesocricetus_auratus',
'scophthalmus_maximus',
'felis_catus',
'microcebus_murinus',
'cynoglossus_semilaevis',
'anolis_carolinensis',
'ailuropoda_melanoleuca',
'melopsittacus_undulatus',
'clupea_harengus',
'neolamprologus_brichardi',
'maylandia_zebra',
'haplochromis_burtoni',
'pundamilia_nyererei',
'larimichthys_crocea',
'chlorocebus_sabaeus']



# Cell
softwares=['bwa','bowtie','bowtie2','hisat2','samtools','picard','STAR']

# Cell

defaults={
    'FASTA_BASE':'ftp://ftp.ensembl.org/pub/release-{version}/fasta/{species}',
    'GTF_BASE':'ftp://ftp.ensembl.org/pub/release-{version}/gtf/{species}',
    'UCSC_FTP':'http://hgdownload.soe.ucsc.edu/goldenPath/',
    'DBSNP_VERSION':'144',
    'SNP_FILE':'snp{DBSNP_VERSION}Common.txt',
}




# FLAT_GRCH37=${UCSC_FTP}/hg19/database/refFlat.txt.gz
# FLAT_GRCH38=${UCSC_FTP}/hg38/database/refFlat.txt.gz


# GRCH37_GTF_FILE=Homo_sapiens.GRCh37.${HUMAN_GRCH37_VERSION}.gtf
# GRCH38_GTF_FILE=Homo_sapiens.GRCh38.${HUMAN_GRCH38_VERSION}.gtf


# DBSNP_RELEASE=144
# SNP_FILE=snp${DBSNP_RELEASE}Common.txt
# GRCH37_UCSC_COMMON_SNP=http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/${SNP_FILE}
# GRCH38_UCSC_COMMON_SNP=http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/${SNP_FILE}




# GRCH37_FASTA=Homo_sapiens.GRCh37.${HUMAN_GRCH37_VERSION}.dna.primary_assembly.fa
# GRCH38_FASTA=Homo_sapiens.GRCh38.dna.primary_assembly.fa

# GRCH37_DICT=Homo_sapiens.GRCh37.${HUMAN_GRCH37_VERSION}.dna.primary_assembly.dict
# GRCH38_DICT=Homo_sapiens.GRCh38.dna.primary_assembly.dict
# rRNA_INTERVAL_LIST=Homo_sapiens.rRNA.interval_list


# Cell
softwares_default={
    'HISAT2_BUILD_EXE':'hisat2-build',
    'HISAT2_SNP_SCRIPT':'hisat2_extract_snps_haplotypes_UCSC.py',
    'HISAT2_SS_SCRIPT':'hisat2_extract_splice_sites.py',
    'HISAT2_EXON_SCRIPT':'hisat2_extract_exons.py',
    'PICARD_EXE':'picard',
    'SAMTOOLS_EXE':'samtools',
    'BWA_EXE':'bwa',
    'STAR_EXE':'STAR',
}