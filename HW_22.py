# Exercise 22 Sarada Giridharan

# Find potential fruit fly / yeast orthologs
# Download FASTA files drosoph-ribosome.fasta.gz and yeast-ribosome.fasta.gz from the course data-directory.
# Uncompress and format each FASTA file for BLAST
# Search fruit fly ribosomal proteins against yeast ribosomal proteins
# For each fruit fly query, output the best yeast protein if it has a significant E-value.
# What ribosomal protein is most highly conserved between fruit fly and yeast?

# import necesary package
from Bio.Blast import NCBIXML

# initialize variables to track most conserved protein
lowest_e_value = float('inf')
most_conserved_ptn = None
most_conserved_query = None

# open the results file
result_handle = open("results.xml")

# parse the results file to get desired output
for blast_result in NCBIXML.parse(result_handle):

    # initialize variables for getting best hit for each query
    best_hit = None
    best_e_value = float('inf')

    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:    # proceed only if the e-value is significant
                if hsp.expect < best_e_value:
                    best_hit = alignment
                    best_e_value = hsp.expect
                    best_hsp = hsp
            
            # update lowest e value across all queries to get most conserved protein    
            if hsp.expect < lowest_e_value:  
                lowest_e_value = hsp.expect
                most_conserved_ptn = alignment.title
                most_conserved_query = blast_result.query    

    # output results for each query
    if best_hit:            
          print("Query:", blast_result.query)
          print("Best hit:", best_hit.title)
          print("E-value:", best_e_value)
          print()

result_handle.close()


# getting the most conserved protein between fruitfly and yeast
print("Most conserved protein:")
print("Query:", most_conserved_query)
print("Protein:", most_conserved_ptn)
print("E-value:", lowest_e_value)
print()

