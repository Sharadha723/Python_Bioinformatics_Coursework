# Exercise 3.1 Sarada Giridharan

# Download or copy-and-paste the DNA sequence of the Anthrax SASP gene from the
# anthrax_sasp.nuc file in the course data-directory.
# Treat the provided sequence as the sequence to be translated (no 5' UTR).
# Write a Python program to print answers to the following questions:
# Does the SASP gene start with a Met codon?
# Does the SASP gene have a frame 1 Met codon? 
# How many nucleotides in the SASP gene?
# How many amino-acids in the SASP protein?
# What is the GC content (% G or C nucleotides) of the SASP gene?
# Test your program with other gene sequences.

#Input DNA sequence
anthrax_seq = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"
# 6. Check with other gene sequence
# anthrax_seq = "TATTATATATATAATATATA"
# anthrax_seq = "TGCAGATCGATGACAGT"
# anthrax_seq = "atgacgatagcagataga"
print ("Given Anthrax SASP gene is:", anthrax_seq)
anthrax_seq = anthrax_seq.upper()
print(" ")

# 1. Check if seq starts with Met codon
if anthrax_seq.startswith('ATG'):
    print("SASP gene starts with a Met codon:",anthrax_seq)
else:
    print("SASP gene does not start with Met codon:",anthrax_seq)
print(" ") #for readability

# 2. Check if Met codon is in frame 1
pos_atg = anthrax_seq.find("ATG")
frame_atg = (pos_atg % 3 +1)
if frame_atg == 1 :
    print ("Met codon is in frame 1")
else:
    print ("Met codon is not in frame 1")
print(" ")

# 3. Number of nucleotides
gene_len = len(anthrax_seq)
print("The number of nucleotides in given Anthrax SASP gene is :", gene_len)
print(" ")

# 4. Number of amino acids 
aa_no = gene_len//3
if gene_len % 3 == 0:
	print ("The number of amino acids in given Anthrax SASP gene is :", aa_no)
else :
	print("There is no integer number of amino acids in the given sequence. The number of amino acids approximately is:", aa_no)
print (" ")

# 5. GC Content
num_g = anthrax_seq.count("G")
num_c = anthrax_seq.count("C")
perc_gc = ((num_g + num_c)/gene_len) *100
print("Percentage GC content in the given Anthrax SASP gene is :", perc_gc)



