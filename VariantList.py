import csv


with open("allvariants.csv", "r") as file:
	Vcounts = {}
	Gcounts = {}
	AD = {}
	DP = {}
	F1R2 = {}
	F2R1 = {}
	
	# GT:AD:AF:DP:F1R2:F2R1:SB
	
	# reader = csv.reader(file) #tells python package to allow to parse file
	# next(row) #will skip the first row
	reader = csv.DictReader(file) #allows use of header as the key
	for row in reader:
		variant = row["Gene.refGene"] + ":" + row["NonsynOI"]
		#print(variant)
		if variant in Vcounts:
			Vcounts[variant] += 1
		else:
			Vcounts[variant] = 1
		
		gene = row["Gene.refGene"]
		if gene in Gcounts:
			Gcounts[gene] += 1
			AD[gene] = AD[gene] + float(row["Otherinfo13"].split(":")[1].split(",")[1])
			DP[gene] = DP[gene] + float(row["Otherinfo13"].split(":")[3])
			F1R2[gene] = F1R2[gene] + float(row["Otherinfo13"].split(":")[4].split(",")[1])
			F2R1[gene] = F2R1[gene] + float(row["Otherinfo13"].split(":")[5].split(",")[1])
			
		else:
			Gcounts[gene] = 1			
			AD[gene] = float(row["Otherinfo13"].split(":")[1].split(",")[1])
			DP[gene] = float(row["Otherinfo13"].split(":")[3])
			F1R2[gene] = float(row["Otherinfo13"].split(":")[4].split(",")[1])
			F2R1[gene] = float(row["Otherinfo13"].split(":")[5].split(",")[1])


with open('genecounts.txt', 'a') as f:
	f.write("Gene,Count,averageAD,averageDP,averageF1R2,averageF2R1\n")
	for gene in sorted(Gcounts):
		ADav = AD[gene] / Gcounts[gene]
		#print ADav
		DPav = DP[gene] / Gcounts[gene]
		F1R2av = F1R2[gene] / Gcounts[gene]
		F2R1av = F2R1[gene] / Gcounts[gene]
		f.write(gene + "," + str(Gcounts[gene]) + "," + str(ADav) + "," + str(DPav) + "," + str(F1R2av) + "," + str(F2R1av)+ "\n")
		#f.write("," + str(AD[gene]) + "," + str(DP[gene]) + "," + str(F1R2[gene]) + "," + str(F2R1[gene]) )

    
 	


with open('variantcounts.txt', 'a') as f:
	for variant in sorted(Vcounts):
		f.write(variant + ":" + str(Vcounts[variant]) + "\n")
    	#print variant + "," + str(counts[variant])
    



#favorite = input("Favorite: ")
#if favorite in counts:
#	print(f"{favorite}: {counts[favorite]}") 


