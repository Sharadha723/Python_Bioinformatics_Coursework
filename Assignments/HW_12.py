# Exercise 12 Sarada Giridharan

# 1a. Download human proteins from RefSeq and compute amino-acid frequencies for the (RefSeq) human proteome.
# Which amino-acid occurs the most? The least?
# Hint: access RefSeq human proteins in human.protein.fasta.gz from the course data-folder.
# 1b. Download human proteins from SwissProt and compute amino-acid frequencies for the SwissProt human proteome.
# Which amino-acid occurs the most? The least?
# Hint: access UniProt XML format SwissProt human proteins from 	http://www.uniprot.org/downloads -> “Taxonomic divisions”
# 1c. How similar are the human amino-acid frequencies of in RefSeq and SwissProt? 
# Which amino-acids show the biggest difference in frequency?

# import necessary packages
import Bio.SeqIO
import sys
import gzip

# Check the input
if len(sys.argv) < 3:
    print("Please provide sequence files", file=sys.stderr)
    sys.exit(1)

# Get the sequence filename
refseqfile = sys.argv[1]
swissprotfile = sys.argv[2]

# Function to count amino acids in each file
def count_amino_acids(filename):
	aa_count = {}
	total_aa = 0

	f = gzip.open(filename, "rt")
	if filename.endswith(".fasta.gz"):
		format_type = "fasta" 
	else:
		format_type = "uniprot-xml"

	for seq_record in Bio.SeqIO.parse(f, format_type):
		for aa in seq_record.seq:
			if aa in aa_count:
				aa_count[aa] +=1
			else:
				aa_count[aa] = 1
			total_aa +=1
	f.close()
	return [aa_count, total_aa]

# Function to print amino acid frequencies in descending order
def print_freq(aa_count, total_aa, label):
    print("Frequency of amino acids in ",label,"in descending order:")
    sorted_aa_count = sorted(aa_count.items(), key=lambda p: p[1], reverse=True)
    for k, v in sorted_aa_count:
        freq = round((v / total_aa) * 100, 2)
        print(k, ":", freq, "%", end=", ")
    print()
    
    return sorted_aa_count

# Function to get the amino acid with the highest frequency
def max_freq(sorted_aa_count, total_aa):
	max_aa = sorted_aa_count[0]
	max_freq = round((max_aa[1]/total_aa)*100, 2)
	print("The amino acid with the highest frequency is:", max_aa[0], "with frequency", max_freq, "%")
	return max_aa

# Function to get the amino acid with the lowest frequency
def min_freq(sorted_aa_count, total_aa):
	min_aa = sorted_aa_count[-1]
	min_freq = round((min_aa[1] / total_aa) * 100, 2)
	print("The amino acid with the lowest frequency is:", min_aa[0], "with frequency", min_freq, "%")
	print()
	return min_aa

# 1.a. Applying function on RefSeq file
result1 = count_amino_acids(refseqfile)
aa_count1 = result1[0]
total_aa1 = result1[1]
sorted_aa_count1 = print_freq(aa_count1, total_aa1, "RefSeq file")
max_aa1 = max_freq(sorted_aa_count1, total_aa1)
min_aa1 = min_freq(sorted_aa_count1, total_aa1)

# 1.b. Applying functions on SwissProt file
result2 = count_amino_acids(swissprotfile)
aa_count2 = result2[0]
total_aa2 = result2[1]
sorted_aa_count2 = print_freq(aa_count2, total_aa2, "SwissProt file")
max_aa2 = max_freq(sorted_aa_count2, total_aa2) 
min_aa2 = min_freq(sorted_aa_count2, total_aa2)

# 1.c. Function to calculate frequency in a dictionary
def calc_freq_dict(aa_count, total_aa):
    freq_dict = {}
    for aa, count in aa_count.items():
        freq_dict[aa] = round((count / total_aa) * 100, 2)
    return freq_dict

freq1 = calc_freq_dict(aa_count1, total_aa1)
freq2 = calc_freq_dict(aa_count2, total_aa2)

# Creating a list to store the differences as tuples
diff_list = []

for aa in freq1:
    if aa in freq2:
        difference = abs(freq1[aa] - freq2[aa])
        diff_list.append((aa, difference))

# Sort the list by the difference in descending order and print them
sorted_diff_list = sorted(diff_list, key=lambda x: x[1], reverse=True)

print("Sorted list of differences in amino acid frequencies:")
for aa, diff in sorted_diff_list:
    print(aa,round(diff,2))

# Get amino acid with highest difference (first item/tuple in the sorted list)
max_diff_aa, max_diff_value = sorted_diff_list[0]

# output the amino acid with highest difference
print("Amino acid with the biggest difference:", max_diff_aa)
print("Frequency difference:",round(max_diff_value,2))



	

