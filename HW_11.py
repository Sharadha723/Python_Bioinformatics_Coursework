# Exercise 11 Sarada Giridharan

# Write a program that reads the microarray data in “data.csv” and computes the mean and standard deviation of the expression values of a specific gene overall, and within each sample category (sample subset 1 and 2).
# Get the name of the microarray datafile from the command-line.
# Get the name of the gene from the command-line.
# Do not use statistics module- standard deviation function. Implement SD and mean directly.

# importing necessary packages
import sys
import csv

# getting file and gene name from command line
f = sys.argv[1]
gene = sys.argv[2]

# opening file and getting rows
f = open(f, mode = 'r')
rows = csv.DictReader(f)

# creating function to calculate mean
def mean(values):
	return float(sum(values)/len(values)) 

# creating function to calculate standard deviation
def stand_dev(values):
	avg = mean(values)
	return (sum((x - avg) ** 2 for x in values) / len(values)) ** 0.5

# creating empty lists to store the expression values
one = []
two = []
both = []

# Iterate through the rows
for r in rows:
	gene_value = float(r[gene])
	both.append(gene_value) 
	if r['TUMOUR'] == '1':
		one.append(gene_value)
	elif r['TUMOUR'] == '2':
		two.append(gene_value)	
f.close()

# output results
print("Mean value for gene:", gene, round(mean(both),2))
print("Mean value for gene", gene, "in category 1:", round(mean(one),2)) 
print("Mean value for gene", gene, "in category 2:", round(mean(two),2))
print("Standard deviation value for gene", gene,":", round(stand_dev(both),2))
print("Standard deviation value for gene", gene, "in category 1:", round(stand_dev(one),2)) 
print("Standard deviation value for gene", gene, "in category 2:", round(stand_dev(two),2)) 


