import csv


with open("allvariants.csv", "r") as file:

	# GT:AD:AF:DP:F1R2:F2R1:SB
	# reader = csv.reader(file) #tells python package to allow to parse file
	# next(row) #will skip the first row
	reader = csv.DictReader(file) #allows use of header as the key
	
	with open('allvariants_expandQC_initialFilter.txt', 'a') as f:
		f.write("Gene.refGene\tChr\tStart\tEnd\tRef\tAlt\tFunc.refGene\tGeneDetail.refGene\tExonicFunc.refGene\tAAChange.refGene\tcosmic70\tOtherinfo1\tOtherinfo2\tOtherinfo3\t")
		f.write("Otherinfo4\tOtherinfo5\tOtherinfo6\tOtherinfo7\tOtherinfo8\tOtherinfo9\tOtherinfo10\tOtherinfo11\tOtherinfo12\tOtherinfo13\tADminor\tDP\tF1R2minor\tF2R1minor\tSample\tAccession\ttranscriptOI\t")
		f.write("NonsynOI\twhitelist\twl.mis\twl.lof\twl.splice\twl.exception\tmanualreview\n")
		for row in reader:
			AD = row["Otherinfo13"].split(":")[1].split(",")[1]
			DP = row["Otherinfo13"].split(":")[3]
			F1R2 = row["Otherinfo13"].split(":")[4].split(",")[1]
			F2R1 = row["Otherinfo13"].split(":")[5].split(",")[1]
			
			if float(AD) >= 3 and float(DP)  >= 20 and float(F1R2) >= 1 and float(F2R1) >= 1:	
							
				f.write(row["Gene.refGene"] + "\t" + row["Chr"] + "\t" +  row["Start"] + "\t" + row["End"] + "\t" + row["Ref"] + "\t" + row["Alt"] + "\t")
				f.write(row["Func.refGene"] + "\t" + row["GeneDetail.refGene"] + "\t" + row["ExonicFunc.refGene"] + "\t" + row["AAChange.refGene"] + "\t" + row["cosmic70"] + "\t" + row["Otherinfo1"] + "\t")
				f.write(row["Otherinfo2"] + "\t" + row["Otherinfo3"] + "\t" + row["Otherinfo4"] + "\t" + row["Otherinfo5"] + "\t" + row["Otherinfo6"] + "\t" + row["Otherinfo7"] + "\t")
				f.write(row["Otherinfo8"] + "\t" + row["Otherinfo9"] + "\t" + row["Otherinfo10"] + "\t" + row["Otherinfo11"] + "\t" + row["Otherinfo12"] + "\t" + row["Otherinfo13"] + "\t")
				f.write(AD + "\t" + DP + "\t" + F1R2 + "\t" + F2R1 + "\t")
				f.write(row["Sample"] + "\t" + row["Accession"] + "\t" + row["transcriptOI"] + "\t" + row["NonsynOI"] + "\t")
				f.write(row["whitelist"] + "\t" + row["wl.mis"] + "\t" + row["wl.lof"] + "\t" + row["wl.splice"] + "\t" + row["wl.exception"] + "\t" + row["manualreview"] + "\n")
		f.close()
	
	



