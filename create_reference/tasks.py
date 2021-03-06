# AUTOGENERATED! DO NOT EDIT! File to edit: 02_tasks.ipynb (unless otherwise specified).

__all__ = ['task_get_file', 'task_bwa_build_index', 'task_bowtie_build_index', 'task_bowtie2_build_index',
           'task_samtools_build_index', 'task_star_build_index', 'task_hisat2_build_index', 'task_picard_build_index',
           'task_build_rRNA_intervals', 'task_extract_rRNA_bed', 'task_gunzip']

# Cell
import os
from biocores.softwares.default import *
from biocores.softwares.bwa import Bwa
from biocores.softwares.bowtie import Bowtie
from biocores.softwares.bowtie2 import Bowtie2
from biocores.softwares.hisat2 import Hisat2
from biocores.softwares.samtools import Samtools
from biocores.softwares.picard import Picard
from biocores.softwares.star import Star
from .commands import *
from .utils import file_exists

# Cell

def task_get_file(link,filename):
    if file_exists(filename):
        return 'echo {filename} exists'.format(filename=filename)
    else:
        cmds = [
            cmd_mkdir(os.path.dirname(filename)),
            cmd_wget(link,filename)
        ]
        return '\n'.join(cmds)

def task_bwa_build_index(software,reference):
    bwa = Bwa(software,bwaDefault)
    cmds = [
            bwa.cmd_build_index(reference)
        ]

    return '\n'.join(cmds)

def task_bowtie_build_index(software,reference, prefix):
    bowtie=Bowtie(software,bowtieDefault)
    cmds = [
            cmd_mkdir(os.path.dirname(prefix)),
            bowtie.cmd_build_index(reference, prefix)
        ]

    return '\n'.join(cmds)

def task_bowtie2_build_index(software,reference, prefix):
    bowtie2=Bowtie2(software,bowtie2Default)
    cmds = [
            cmd_mkdir(os.path.dirname(prefix)),
            bowtie2.cmd_build_index(reference, prefix)
        ]

    return '\n'.join(cmds)

def task_samtools_build_index(software,reference):
    samtools = Samtools(software,samtoolsDefault)
    cmds = [
        samtools.cmd_faidx(reference)
    ]
    return '\n'.join(cmds)

def task_star_build_index(software,reference,prefix,gtf,read_length):
    star = Star(software,starDefault)
    cmds = [
        cmd_mkdir(os.path.dirname(prefix)),
        star.cmd_build_index(prefix, reference, gtf, read_length)
    ]
    return '\n'.join(cmds)

def task_hisat2_build_index(software,reference,prefix,snp='',gtf=''):
    hisat2=Hisat2(software,hisat2Default)
    genome_ss=None
    genome_exon=None
    genome_genotype=None
    genome_snp=None

    cmds = [
        cmd_mkdir(os.path.dirname(prefix))
    ]
    if snp != '':
        cmds.append(hisat2.cmd_prepare_snp_ucsc(reference,snp,prefix))
        genome_snp=prefix+'.snp'
        genome_genotype=prefix+'.haplotype'
    if gtf != '':
        cmds.append(hisat2.cmd_prepare_exon_ss(gtf,prefix))
        genome_ss=prefix+'.ss'
        genome_exon=prefix+'.exon'

    cmds.append(hisat2.cmd_build_index(reference, prefix, genome_ss=genome_ss, genome_exon=genome_exon,
                        genome_genotype=genome_genotype, genome_snp=genome_snp))
    return '\n'.join(cmds)

def task_picard_build_index(software,reference,reference_dict,tmp):
    picard=Picard(software,picardDefault)
    cmds = [
        cmd_mkdir(os.path.dirname(reference_dict),tmp),
        picard.cmd_create_sequence_dictionary(reference, reference_dict, tmp),
    ]
    return '\n'.join(cmds)

def task_build_rRNA_intervals(software,bed, intervals,reference_dict, tmp):
    picard=Picard(software,picardDefault)
    cmds = [
        cmd_mkdir(os.path.dirname(intervals),tmp),
        picard.cmd_bed2intervals(bed, intervals,reference_dict, tmp)
    ]
    return '\n'.join(cmds)

def task_extract_rRNA_bed(gtf,bed):
    cmds = [
        cmd_mkdir(os.path.dirname(bed)),
    ]
    gtf2bed = '''awk -F '\t' '{if(/gene_biotype "rRNA"/ && $3=="transcript"){print $1"\t"$4"\t"$5}}' ''' + gtf + '>' + bed
    cmds.append(gtf2bed)
    return '\n'.join(cmds)

def task_gunzip(gzipfile):
    return cmd_gunzip(gzipfile)