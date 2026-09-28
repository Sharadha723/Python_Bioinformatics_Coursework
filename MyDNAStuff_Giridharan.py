#MyDNAStuff module - Sarada Giridharan

import sys

# open and get dna sequence
def readseq(seqfile):
    try:
        theseq = ''.join(open(seqfile).read().split())
        theseq_upper = theseq.upper()
        return theseq_upper
        seqfile.close()
    except FileNotFoundError:
        print("Error - The file was not found")
    except IOError:
        print("Cannot read sequence file")
    except:
        print("Cannot read file")


# get complement of sequence
def comp(seq):
    try:
        comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
        return ''.join(comp.get(nt,nt) for nt in seq)
    except TypeError:
        print("Given sequence is not a string")
    except:
        print("Cannot get complement of given sequence")

# get reversed sequence
def revseq(seq):
    try:
        return ''.join(reversed(seq))
    except TypeError:
        print("Given sequence is not a string")
    except:
        print("Cannot get complement of given sequence")

# get reverse complement
def revcomp(seq):
    try:
        return comp(revseq(seq))
    except TypeError:
        print("Given sequence is not a string")
    except:
        print("Cannot get complement of given sequence")

# get percentage of gc in given sequence
def GCPerc(seq):
    try:
        number_of_nt = len(seq)
        number_of_aa = (number_of_nt//3) - 1
        number_of_gcs = seq.count('C') + seq.count('G')
        gc_percent = 100*(number_of_gcs/number_of_nt)
        return round(gc_percent,2)
    except TypeError:
        print("Input sequence must be a string")
    except:
        print("Cannot find GC percentage")

# find position and frame of first met codon
def pos_frame_met(seq):
    try:
        met_pos = seq.find('ATG')
        met_frame = (met_pos % 3) + 1
        if met_pos == '-1':
            print ("Met codon not found in sequence")
        return "Position:",met_pos+1, "Frame:",met_frame
    except TypeError:
        print("Input sequence must be a string")
    except:
        print ("Cannot find position and frame of Met codon")

# find if methionine is in frame 1
def met_frame_1(seq):
    try:
        pos,frame = pos_frame_met(seq)
        if frame == '1':
             print("Sequence has frame 1 met codon")
        else:
             print("Sequence does NOT have frame 1 met codon")
    except:
        print("Cannot find if Met codon is in frame 1")

# find if sequence starts with methionine
def seq_start(seq):
    try:
        if seq.startswith('ATG'):
            print("Sequence starts with methionine")
        else:
            print("Sequence does NOT start with methionine")
    except TypeError:
        print("Input sequence must be a string")
    except:
        print ("Cannot find if sequence starts with methionine")

# find if given sequence contains tandem repeats
def tandem_repeat_check(seq):
    try:
        half_seq = len(seq)//2
        for i in range(1,half_seq+1):
            if len(seq) % i == 0:
                tandem_repeat = seq[:i]
                if tandem_repeat * (len(seq)//i) == seq:
                         positive = "Sequence contains tandem repeats"
                         return positive
            negative = "Sequence does not contain tandem repeats"
            return negative
    except TypeError:
        print("Input sequence must be a string")
    except:
        print("Cannot find tandem repeats")

# find if given sequence self-hybridizes (reverse complement palindrome)
def self_hyb(seq):
    try:
        n = len(seq)
        halfn = n//2
        first_half = seq[:halfn]
        second_half = seq[-halfn:]
        if first_half == revcomp(second_half):
            rcpalindrome = True
        else:
            rcpalindrome = False
        return rcpalindrome
    except TypeError:
        print("Input sequence must be a string")
    except:
        print("Cannot find self-hybridization")

