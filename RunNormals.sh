#$ -cwd
# File:	RunNormals.sh


arr=()
while IFS= read -r line; do
   arr+=("$line")
done < Normals

echo ${arr[*]}  

for sample in ${arr[*]}
do

	echo $sample
	echo "  "
done
