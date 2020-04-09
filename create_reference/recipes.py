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
                filename=para['local_genome_fasta_gz'],
            ),
            uid='get_fasta_%s_%s' % (para['species'],para['version']) ,
            stage_name='get_fasta'
        ) for para in species_paras]

    get_gtf = [
        workflow.add_task(
            func=task_get_file,
            params=dict(
                link=para['link_transcriptome_gtf'],
                filename=para['local_transcriptome_gtf_gz'],
            ),
            uid='get_gtf_%s_%s' % (para['species'],para['version']) ,
            stage_name='get_gtf'
        ) for para in species_paras]

    get_bwa_idx = [
        workflow.add_task(
            func=task_bwa_build_index,
            params=dict(
                software=args.bwa,
                reference=para['local_genome_fasta'],
            ),
            uid='get_bwa_index_%s_%s' % (para['species'],para['version']) ,
            parents=get_fasta[i],
            stage_name='get_bwa_index'
        ) for i,para in enumerate(species_paras)]

    get_bowtie_idx = [
        workflow.add_task(
            func=task_bowtie_build_index,
            params=dict(
                software=args.bowtie,
                reference=para['local_genome_fasta'],
                prefix=para['bowtie_idx']
            ),
            uid='get_bowtie_index_%s_%s' % (para['species'],para['version']) ,
            parents=get_fasta[i],
            stage_name='get_bowtie_index'
        ) for i,para in enumerate(species_paras)]

    get_bowtie2_idx = [
        workflow.add_task(
            func=task_bowtie2_build_index,
            params=dict(
                software=args.bwa,
                reference=para['local_genome_fasta'],
                prefix=para['bowtie2_idx']
            ),
            uid='get_bowtie2_index_%s_%s' % (para['species'],para['version']) ,
            parents=get_fasta[i],
            stage_name='get_bowtie2_index'
        ) for i,para in enumerate(species_paras)]

