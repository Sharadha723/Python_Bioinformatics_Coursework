# Exercise 20 Sarada Giridharan

# Write a program using NCBI's E-Utilities to retrieve the ids of RefSeq human LIME1 proteins from NCBI. 
# Use the query:
# Homo sapiens[Organism] AND LIME1[Gene Name] AND REFSEQ
# You do not need the protein sequence!
# Extend your program to blast the proteins ids vs RefSeq proteins (refseq_protein) using the NCBI blast web-service:
# Search all protein ids together (separated by newlines)
# Use the keyword argument entrez_query to restrict to mouse proteins: Mus musculus[Organism]
# Use the keyword argument expect to restrict to high quality alignments: 1e-3

# Further extend your program to filter the results for significance and display the putative human-mouse orthologs
# Filter the alignments for E-value at most 1e-5
# Print only the best hit (smallest E-value) for each query

# Make sure you use the file-based caching strategy shown in the lecture.
# If the qblast call takes more than 10 mins, kill the program (Control-C) and try again…

from Bio import Entrez, SeqIO
import os.path
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


# Set email for Entrez
Entrez.email = "sg1817@georgetown.edu"

# Retrieve IDs of refseq human LIME1 proteins from NCBI
handle = Entrez.esearch(db = 'protein', term = 'Homo sapiens[Orgn] AND LIME1[Gene] AND REFSEQ')
results = Entrez.read(handle)
handle.close()

# print out ID List
idlist = results["IdList"]
print("ID List:", idlist)
print()

# BLAST above IDs against given organism 
for protein_id in idlist:
	filename = "blastp-refseq"+protein_id+".xml"
	if os.path.exists(filename):
		blast_record = open(filename, "r")
		blast_results = blast_record.read()
		blast_record.close()
	else:
		result_handle = NCBIWWW.qblast('blastp','refseq_protein', protein_id, 
                               			entrez_query = "Mus musculus[Organism]", 
                               			expect = 1e-3)
		blast_result = result_handle.read()
		result_handle.close()

                # save file so that the next time we BLAST, we get this result
		save_file = open(filename, "w")
		save_file.write(blast_result)
		save_file.close()

        # open file to parse the result
	result_handle = open(filename)

        # parse the result from the saved xml file and print out the best hits for each query
	for blast_record in NCBIXML.parse(result_handle):
		for desc in blast_record.descriptions:
			if desc.e < 1e-5:
				print("****Alignment****")
				print("query:",blast_record.query)
				print("sequence:",desc.title)
				print("e-value:",desc.e)
				print()
				break
			










