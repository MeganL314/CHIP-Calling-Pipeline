#$ -cwd
# File: RunTumorOnlyMode.sh

module load gatk/4.2.0.0

arr=()
while IFS= read -r line; do
   arr+=("$line")
done < Samples.txt

echo ${arr[*]}
path=/path/to/bams/
reference=/directory/.fasta
interval=/directory/.bed
germline=/directory/.hg38.vcf.gz
result_dir=/directory/results/

for sample in ${arr[*]}
do
  	gatk Mutect2 \
                -L $interval \
                -R $reference \
                -I $path$sample \
                --germline-resource $germline \
                --panel-of-normals pon.vcf.gz \
                -O $result_dir/TumorOnlyMode_$sample.vcf.gz
        echo "Sample: $sample"
        echo "Path: $path$sample"
done
