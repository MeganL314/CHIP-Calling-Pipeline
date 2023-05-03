#$ -cwd
# File: RunNormals.sh

module load gatk/4.2.0.0

arr=()
while IFS= read -r line; do
   arr+=("$line")
done < Normals.txt

echo ${arr[*]}
path=/directory/bams/
reference=/directory/ref.fasta

for sample in ${arr[*]}
do
  	gatk Mutect2 \
                -R $reference \
                -I $path$sample \
                -O single_$sample.vcf.gz
        echo "Sample: $sample"
        echo "$path$sample"
done



