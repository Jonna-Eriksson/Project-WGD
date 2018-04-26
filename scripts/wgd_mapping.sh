#!/bin/bash

echo "Start mapping"
#$1 is the taxon´s name

clc_mapper -o $1_$2.cas -p fb ss 300 1000 -q [Example: /home/trimmed_files/$1/trimmed_file.fq] -s 0.7 -d $3 --cpus 1;
echo "Mapping completed, starting cas to bam conversion"

clc_cas_to_sam -a $1_$2.cas -o $1_$2.bam -f 33 -u;
echo "Cas to bam conversion complete"

echo "start sorting"
samtools sort $1_$2.bam -o $1_$2.sorted.bam;

echo "start bam to sam conversion"
samtools view $1_$2.sorted.bam -o $1_$2.sorted.sam;

echo "Done"
