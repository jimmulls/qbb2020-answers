#!/bin/bash

##This bash script has been commented out for each given step. When you reach a given step, un-comment
## the lines following it for it to run properly.


# for SAMPLE in *.fastq
# do
#     bwa mem -R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" sacCer3.fa $SAMPLE > ${SAMPLE%.fastq}.sam
# done


## STEP 3

# for SAMPLE in *.sam
# do
#     samtools sort $SAMPLE -o ${SAMPLE%.sam}.bam -O bam
# done


## STEP 4

#freebayes -f sacCer3.fa -p 1 --genotype-qualities *.bam > yeast_vars.vcf

## STEP 5

#vcffilter -f "QUAL > 20" yeast_vars.vcf > yeast_vars_results.vcf

## STEP 6

#vcfallelicprimitives -kg yeast_vars_results.vcf > yeast_vars_complex_hap_decomp.vcf

## STEP 7

#snpeff ann -lof R64-1-1.86 yeast_vars_complex_hap_decomp.vcf > year_vars_effect_pred.vcf