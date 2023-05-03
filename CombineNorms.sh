#$ -cwd
# File: CreatePanelofNormals.sh

ref=/directory/ref.fasta

echo $ref

module load gatk/4.2.0.0

gatk GenomicsDBImport -R $ref \
      --genomicsdb-workspace-path pon_db \
      -L CHIP_NEJM2017_74genes_new.bed \
      -V .bam.vcf.gz \
      -V .bam.vcf.gz \
      -V .bam.vcf.gz \


gatk CreateSomaticPanelOfNormals -R $ref -V gendb://pon_db -O pon.vcf.gz
