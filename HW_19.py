from DNASeq_Giridharan import *
from codon_table2_Giridharan import *
import sys

# check if files are provided
if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

# read the codon table using module codon_table2_Giridharan
codons = codon_table2_Giridharan()
codons.read(sys.argv[1])

# read sequence file using module from DNASeq_Giridharan
seq = DNASeq_Giridharan()
seq.read(sys.argv[2])

# print forward translation
for frame in (1,2,3):
    print("Frame",frame,"(forward):",codons.translate(seq.seq,frame))

# get reverse complement of sequence
rev_comp_seq = seq.reverseComplement()

# print reverse translation
for frame in (1,2,3):
    print("Frame",frame,"(reverse):",codons.translate(rev_comp_seq,frame))


