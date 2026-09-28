# Exercise 15 Sarada Giridharan

# Download the file     
#            proteomics.summary.tsv 
# from the course data-directory
# columns are genes; rows are samples; 
# values are # of distinct peptides observed
# Write a pandas-based program to 
# determine the number of genes with at least two distinct peptides in all samples.
# determine the number of genes with at least two distinct peptides in at least one sample.
# Hint: Slide 21 contains the essential tricks

# import necessary packages
import numpy as np
import pandas as pd

# read file
df = pd.read_csv("proteomics.summary.tsv",sep='\t')


# Find those genes (columns) with at least 2 distict peptides in all samples
qualifying_genes = (df>=2)


# count number of genes with atleast 2 distict peptides across all samples (must be 1 (true) everywhere thus sum equalling to the number of rows)
counts1 = (qualifying_genes.sum(axis=0) == df.shape[0]).sum()
print("Number of genes with at least 2 distinct peptides across all samples:",counts1)


# count number of genes with atleast 2 distinct peptides in atleast 1 sample (min = 1, therefore greater than zero)
counts2 = (qualifying_genes.sum(axis=0) > 0).sum()
print("Number of genes with at least 2 distinct peptides in atleast 1 sample:",counts2)


