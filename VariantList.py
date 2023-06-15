import csv


with open("allvariants.csv", "r") as file:
	counts = {}
	# reader = csv.reader(file) #tells python package to allow to parse file
	# next(row) #will skip the first row
	reader = csv.DictReader(file) #allows use of header as the key
	for row in reader:
		variant = row["Gene.refGene"] + ":" + row["NonsynOI"]
		#print(variant)
		if variant in counts:
			counts[variant] += 1
		else:
			counts[variant] = 1


with open('variantcounts.txt', 'a') as f:
	for variant in sorted(counts):
		f.write(variant + ":" + str(counts[variant]) + "\n")
    
    
    
    

	#print counts[variant]
 	print variant + "," + str(counts[variant])


#def get_value(language):
	#print(counts[language])
#	return counts[language]

#favorite = input("Favorite: ")
#if favorite in counts:
#	print(f"{favorite}: {counts[favorite]}") 


print(

