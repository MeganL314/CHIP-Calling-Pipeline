README.md: tarCommands_Bam.sh
	echo "## CHIP Pipeline" > README.md
	echo "" >> README.md
	date >> README.md
	echo "" >> README.md
	wc -l tarCommands_Bam.sh | egrep -o "[0-9]+" >> README.md


