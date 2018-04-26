# Project-WGD
Identify all paralogs and assemble full sequences across all exons in a gene. 

## Usage
python wgd_mapping_workflow.py [path to working directory]

## Install


## Requirements
* Working directory containing a target folder and script folder.
  * Target folder should contain subfolder of each gene.
  * Each gene have subfolders:
    * One consensus folder, containing fasta files for running CLC-mapper.
    * Species folders - That should be empty. All output (SAM-files) will be created.
  * Script folder where the python and bash script exist.
    
* CLC-Assembly-Cell/v5.0.4
* samtools/v1.3.1
* Python (v2 or v3)

## Steps
* For each species, assembling each exon in a gene with a low similarity score (0.7) using CLC_mapper.
* Converting a sorted .bam to .sam.
* .sam files are used for identifying copies using Project-cluster.

## Authors

J.S. Eriksson & D.J. Bennett
