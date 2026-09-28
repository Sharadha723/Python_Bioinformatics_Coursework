## Python_Bioinformatics_Coursework
My solutions to programming exercises from a Master's-level Python course in Bioinformatics, covering Python programming, biological data processing, sequence analysis, and computational problem-solving.

The assignments progress from Python fundamentals and sequence manipulation to genomic data analysis, databases, APIs, and computational biology.

## Repository structure

    Python_Bioinformatics_Coursework/
    ├── Assignments/       # Python solutions for individual coursework assignments
    ├── modules/           # Reusable Python modules developed for the assignments
    └── README.md          # Assignment overview, repository information and notes

## Assignment overview table

| Assignment  | Description                                                                                                                                                                                        | Main Python / Bioinformatics Concepts                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **HW 2.1**  | Stores the methionine start codon (`ATG`), converts it to lowercase, reverses the sequence, and prints the result.                                                                                 | String variables, string indexing, string concatenation, `lower()`                                                                   |
| **HW 2.2**  | Finds the position of the first start codon (`ATG`) in a DNA sequence and determines its translation frame.                                                                                        | String searching with `find()`, indexing, modulo (`%`), reading frames                                                               |
| **HW 3.1**  | Analyzes an Anthrax SASP gene sequence to determine whether it starts with a methionine codon, whether the start codon is in frame 1, sequence length, predicted amino-acid count, and GC content. | String methods, conditional statements, `len()`, integer division, modulo, GC-content calculation, DNA/protein sequence analysis     |
| **HW 4.1**  | Calculates the reverse complement of DNA codons using modularized `complement()` and reverse-complement functions that handle uppercase and lowercase input.                                       | Functions, modular programming, loops, string manipulation, DNA reverse complements, input validation                                |
| **HW 4.2**  | Determines whether DNA sequences consist of an integer number of perfect tandem repeats and identifies the repeating unit.                                                                         | Functions, loops, string slicing, modulo, sequence pattern detection, tandem repeats                                                 |
| **HW 5.1**  | Retrieves forward and reverse PCR primers for the human **TP53** gene and calculates their reverse-complement sequences.                                                                           | Functions, loops, string manipulation, DNA complement/reverse complement, PCR primer analysis                                        |
| **HW 5.2**  | Tests whether PCR primer sequences form reverse-complement palindromes, including odd-length sequences that may self-hybridize around a central nucleotide.                                        | Functions, slicing, integer division, conditional logic, reverse complements, DNA palindrome detection, primer self-hybridization    |
| **HW 6.1**  | Extends the PCR primer reverse-complement program to accept forward and reverse primer sequences as command-line arguments.                                                                        | Command-line arguments, `sys.argv`, functions, reverse complements, input handling                                                   |
| **HW 6.2**  | Creates a command-line program that reads a DNA sequence from a file and performs a requested operation: complement, reverse, or reverse complement.                                               | Command-line arguments, file I/O, `sys.argv`, `open()`, `read()`, string manipulation, conditional logic                             |
| **HW 7.1**  | Reads primer pairs from a file and outputs the reverse complement of each forward and reverse primer while retaining the input pair format.                                                        | File I/O, command-line arguments, `splitlines()`, `split()`, loops, functions, reverse complements                                   |
| **HW 8.1**  | Implements DNA reverse-complement calculation using three different approaches and compares the techniques.                                                                                        | Dictionaries, functions, loops, list comprehension, `reversed()`, `join()`, lists, alternative algorithmic approaches                |
| **HW 8.2**  | Translates a nucleotide sequence into an amino-acid sequence using a codon table supplied as a command-line file, and checks whether the initial codon is a valid translation start site.          | Command-line arguments, file I/O, dictionaries, codon tables, translation, sequence parsing, list operations, bacterial genetic code |
| **HW 9**    | Extends DNA translation to all three forward and three reverse-complement reading frames and handles ambiguous `N` symbols in the third codon position.                                            | Functions, reading frames, reverse complements, dictionaries, list comprehension, ambiguous nucleotides, codon translation           |
| **HW 10.1** | Implements a compact two-line DNA reverse-complement program using a complement dictionary, `reversed()`, list comprehension, and `join()`.                                                        | Dictionaries, list comprehension, `reversed()`, `dict.get()`, `join()`, concise Python programming                                   |
| **HW 10.2** | Calculates nucleotide frequencies in a DNA sequence and reports them from most frequent to least frequent, including percentage composition.                                                       | Dictionaries, counting, `.items()`, `sorted()`, sorting by values, `reversed()`, percentage calculation                              |
| **HW 11** | Reads microarray expression data from a CSV file and calculates the mean and standard deviation of a specified gene overall and separately for two sample categories. | CSV file I/O, command-line arguments, `sys.argv`, `csv.DictReader`, functions, lists, loops, mean and standard deviation calculations |
| **HW 12** | Calculates amino-acid frequencies in the human RefSeq and SwissProt proteomes, identifies the most and least frequent amino acids, and compares amino-acid frequencies between the two datasets. | FASTA/SwissProt parsing, `Bio.SeqIO`, gzip files, dictionaries, functions, sorting, frequency calculations, proteomics, comparative analysis |
| **HW 13** | Identifies the highest-coverage heterozygous locus in a BAM file and reports its alleles and read counts, then applies alignment-quality filters and compares the resulting locus and read counts. | BAM file processing, read alignment, heterozygosity, coverage, allele counts, quality filtering, genomic data analysis |
| **HW 14.1** | Parses a UniProt XML entry and extracts and formats its references, including authors, title, journal, publication details, database references, and scopes. | XML parsing, `ElementTree`, XML namespaces, `urllib`, loops, nested elements, string formatting |
| **HW 15** | Uses pandas to determine how many genes have at least two distinct peptides in all samples and how many have at least two distinct peptides in at least one sample. | Pandas, TSV file processing, Boolean filtering, DataFrames, `sum()`, `axis`, `shape`, vectorized operations |
| **HW 16.1** | Builds a `MyDNAStuff` module containing reusable DNA sequence functions and a `codon_table` module for codon lookup and translation, then uses them to translate a DNA sequence in all six reading frames. | Python modules, functions, code reuse, DNA sequence manipulation, codon tables, translation, reading frames, reverse complements, ambiguous nucleotides |
| **HW 17.1** | Extends the `MyDNAStuff` and `codon_table` modules by adding error handling with `try`/`except` blocks for file, type, key, and other errors. | Exception handling, `try`/`except`, `IOError`, `FileNotFoundError`, `TypeError`, `KeyError`, Python modules, input validation |
| **HW 19** | Converts the DNA sequence and codon-table modules into classes and uses their methods to translate DNA sequences in all six reading frames. | Object-oriented programming, classes, methods, `self`, constructors, modules, encapsulation, DNA translation, reverse complements |
| **HW 20** | Uses NCBI E-Utilities to retrieve human RefSeq LIME1 protein IDs and BLASTs them against mouse RefSeq proteins, using caching and filtering to identify significant best hits. | NCBI E-Utilities, Entrez, BLAST, `Bio.Blast`, XML parsing, web services, file-based caching, E-values, ortholog identification |
| **HW 22** | Searches for potential fruit fly/yeast ribosomal protein orthologs by running BLASTP and parsing the XML results to identify significant best hits and the most conserved protein. | BLASTP, command-line tools, FASTA files, XML parsing, `Bio.Blast`, E-values, ortholog detection, comparative genomics |
| **HW 23** | Uses a database query to look up the scientific name corresponding to a user-supplied organism common name. | SQL/database queries, database connections, command-line arguments, relational tables, SQL queries, error handling |
| **HW 24** | Uses SQLObject to look up the scientific name corresponding to a user-supplied organism name through related taxonomy and name tables. | SQLObject, object-relational mapping (ORM), database models, foreign keys, table relationships, `SelectBy()`, exception handling |
| **HW 25** | Uses a taxonomy database to retrieve and print the complete taxonomic lineage of a user-supplied organism, from the root through successive taxonomic levels. | SQLObject/database queries, relational data, taxonomy, foreign keys, parent-child relationships, loops, lists, command-line arguments |

## Topics Covered
- Python programming and data structures
- DNA and protein sequence analysis
- File parsing and command-line programs
- FASTA, BAM, XML, and CSV/TSV data
- Biopython and pandas
- BLAST and NCBI E-Utilities
- SQL and database interaction
- Object-oriented programming and Python modules
- Error handling and code reuse
- Comparative genomics and taxonomy

## Version Note

All code was implemented and tested using Python 3.x.

## Coursework Note

This repository contains coursework completed as part of my master's-level
studies in Bioinformatics. The solutions represent my own implementations
and learning throughout the course.

## Academic Use

This repository is intended for educational and portfolio purposes. Please use these solutions as a reference for learning and do not submit them as your own coursework.

## Author
Sarada Giridharan
