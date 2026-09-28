# Exercise 13 Sarada Giridharan

# Starting with the program of slide 19 and working with BAM file 10_Normal_Chr21.bam,  find the locus with:
# Single diploid-organism heterozygosity (approx.), and highest coverage
# Output the locus, its alleles, and the number of high-quality reads for each allele.
# Then, add the code to filter out bad/poor alignments (slide 20) to your program.
# Does the highest coverage heterozygous locus and its read counts change? If so, how?

# importing library necessary for reading Sam/Bam file
import pysam

# opening the bam file
bf = pysam.Samfile('10_Normal_Chr21.bam')

# initialisation of variables to store values later
max_coverage = 0
max_position = None
max_counts = {}

# For every position in the reference
for pileup in bf.pileup('21'):
    counts = {}
    # ...examine every aligned read
    for pileupread in pileup.pileups:
    # ...check the read and alignment - bad/poor alignment filter code
        if pileupread.indel:  #skips if the read contains an insertion
            continue
        if pileupread.is_del:  #skips if the read contains a deletion
            continue
        al = pileupread.alignment  #get alignment of read
        if al.is_unmapped:   #skip if read is unmapped
            continue
        if al.is_secondary:   #skip if read is not the best
            continue
        if int(al.opt('NM')) > 1:  #skip if more than one mismatch
           continue
        if int(al.opt('NH')) > 1:  #skip if more than one hit
           continue
        # ...and get the read-base
        if not pileupread.query_position:  #skip if not get a valid query position
            continue
        readbase = pileupread.alignment.seq[pileupread.query_position]
        # Count the number of each base
        if readbase not in counts:
             counts[readbase] = 0
        counts[readbase] += 1
    # If there is no variation, move on
    if len(counts) != 2:
            continue
    # relative difference
    counts_alleles = list(counts.values())
    diff = abs(counts_alleles[0] - counts_alleles[1])
    avg = (counts_alleles[0]+counts_alleles[1])/2
    perc = (diff/avg) *100

    
    # store the position, coverage and base counts
    if perc < 20:   # threshold value of relative difference is 20% here
        coverage = pileup.n  #current coverage
        if coverage > max_coverage:  #check if current coverage is greater than max coverage
            max_coverage = coverage
            max_position = pileup.pos
            max_counts = counts

#output results of maximum coverage
if max_position is not None:
     print("Locus:", max_position)
     print("Coverage (maximum):",max_coverage)
     for k,v in sorted(max_counts.items()):
          print("Allele:", k, "Reads:", v)
     print()





