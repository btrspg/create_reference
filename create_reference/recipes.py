# AUTOGENERATED! DO NOT EDIT! File to edit: 05_recipes.ipynb (unless otherwise specified).

__all__ = ['recipe']

# Cell

from .tasks import *

# Cell

def recipe(workflow,species_paras,args):
    get_fasta = [
        workflow.add_task(
            func=task_get_file,
            params=dict(
                link=para['link_genome_fasta'],
                filename=para['local_files']['local_genome_fasta_gz'],
            ),
            uid='get_fasta_%s_%s' % (para['species'],para['version']) ,
            stage_name='get_fasta'
        ) for para in species_paras]

    gunzip_fasta = [
        workflow.add_task(
            func=task_gunzip,
            params=dict(
                gzipfile=para['local_files']['local_genome_fasta_gz']
            ),
            uid='gunzip_fasta_%s_%s' % (para['species'],para['version']) ,
            parents=get_fasta[i],
            stage_name='gunzip_fasta'
        ) for i,para in enumerate(species_paras)]

    get_gtf = [
        workflow.add_task(
            func=task_get_file,
            params=dict(
                link=para['link_transcriptome_gtf'],
                filename=para['local_files']['local_transcriptome_gtf_gz'],
            ),
            uid='get_gtf_%s_%s' % (para['species'],para['version']) ,
            stage_name='get_gtf'
        ) for para in species_paras]

    gunzip_gtf = [
        workflow.add_task(
            func=task_gunzip,
            params=dict(
                gzipfile=para['local_files']['local_transcriptome_gtf_gz']
            ),
            uid='gunzip_fasta_%s_%s' % (para['species'],para['version']) ,
            parents=get_gtf[i],
            stage_name='gunzip_gtf'
        ) for i,para in enumerate(species_paras)]

    get_rRNA_bed = [
        workflow.add_task(
            func=task_extract_rRNA_bed,
            params=dict(
                gtf=para['local_files']['local_transcriptome_gtf'],
                bed=para['local_files']['rrna_bed']
            ),
            uid='get_rRNA_bed_%s_%s' % (para['species'],para['version']) ,
            parents=gunzip_gtf[i],
            stage_name='get_rRNA_bed'
        ) for i,para in enumerate(species_paras)]



    if 'picard' in args.indexs:
        get_picard_idx = [
            workflow.add_task(
                func=task_picard_build_index,
                params=dict(
                    software=args.picard,
                    reference=para['local_files']['local_genome_fasta'],
                    reference_dict=para['local_files']['picard_idx'],
                    tmp=para['local_files']['tmp']
                ),
                uid='get_picard_idx_%s_%s' % (para['species'],para['version']) ,
                parents=gunzip_fasta[i],
                stage_name='get_picard_idx'
            ) for i,para in enumerate(species_paras) ]

        get_rRNA_intervals = [
            workflow.add_task(
                func=task_build_rRNA_intervals,
                params=dict(
                    software=args.picard,
                    bed=para['local_files']['rrna_bed'],
                    intervals=para['local_files']['rrna_intervals'],
                    reference_dict=para['local_files']['picard_idx'],
                    tmp=para['local_files']['tmp']
                ),
                uid='get_rRNA_intervals_%s_%s' % (para['species'],para['version']) ,
                parents=[get_picard_idx[i],get_rRNA_bed[i]],
                stage_name='get_rRNA_intervals'
            ) for i,para in enumerate(species_paras) ]



    if 'bwa' in args.indexs:
        get_bwa_idx = [
            workflow.add_task(
                func=task_bwa_build_index,
                params=dict(
                    software=args.bwa,
                    reference=para['local_files']['local_genome_fasta'],
                ),
                uid='get_bwa_index_%s_%s' % (para['species'],para['version']) ,
                parents=gunzip_fasta[i],
                stage_name='get_bwa_index'
            ) for i,para in enumerate(species_paras)]

    if 'samtools' in args.indexs:
        get_bwa_idx = [
            workflow.add_task(
                func=task_samtools_build_index,
                params=dict(
                    software=args.samtools,
                    reference=para['local_files']['local_genome_fasta'],
                ),
                uid='get_samtools_index_%s_%s' % (para['species'],para['version']) ,
                parents=gunzip_fasta[i],
                stage_name='get_samtools_index'
            ) for i,para in enumerate(species_paras)]

    if 'bowtie' in args.indexs:
        get_bowtie_idx = [
            workflow.add_task(
                func=task_bowtie_build_index,
                params=dict(
                    software=args.bowtie,
                    reference=para['local_files']['local_genome_fasta'],
                    prefix=para['local_files']['bowtie_idx']
                ),
                uid='get_bowtie_index_%s_%s' % (para['species'],para['version']) ,
                parents=gunzip_fasta[i],
                stage_name='get_bowtie_index'
            ) for i,para in enumerate(species_paras)]

    if 'bowtie2' in args.indexs:
        get_bowtie2_idx = [
            workflow.add_task(
                func=task_bowtie2_build_index,
                params=dict(
                    software=args.bwa,
                    reference=para['local_files']['local_genome_fasta'],
                    prefix=para['local_files']['bowtie2_idx']
                ),
                uid='get_bowtie2_index_%s_%s' % (para['species'],para['version']) ,
                parents=gunzip_fasta[i],
                stage_name='get_bowtie2_index'
            ) for i,para in enumerate(species_paras)]

    if 'hisat2' in args.indexs:
        get_hisat2_idx = [
            workflow.add_task(
                func=task_hisat2_build_index,
                params=dict(
                    software=args.hisat2,
                    reference=para['local_files']['local_genome_fasta'],
                    prefix=para['local_files']['hisat2_idx'],
                    snp='',
                    gtf=para['local_files']['local_transcriptome_gtf']
                ),
                uid='get_hisat2_index_%s_%s' % (para['species'],para['version']) ,
                parents=[gunzip_fasta[i],gunzip_gtf[i]],
                stage_name='get_hisat2_index'
            ) for i,para in enumerate(species_paras)]

    if 'star' in args.indexs:
        get_star_idx = [
            workflow.add_task(
                func=task_star_build_index,
                params=dict(
                    software=args.star,
                    reference=para['local_files']['local_genome_fasta'],
                    prefix=para['local_files']['star_idx_prefix']+'_'+str(read_length),
                    gtf=para['local_files']['local_transcriptome_gtf'],
                    read_length=read_length
                ),
                uid='get_star_index_%s_%s' % (para['species'],para['version']) ,
                parents=[gunzip_fasta[i],gunzip_gtf[i]],
                stage_name='get_hisat2_index'
            ) for read_length in para['read_length'] for i,para in enumerate(species_paras)]
