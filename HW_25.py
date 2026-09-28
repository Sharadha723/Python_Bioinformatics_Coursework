# Exercise 25 Sarada Giridharan

# import necessary packages
import sys
from model_ex_25 import *
init()

# send error message if name not provided
if len(sys.argv) < 2:
    print ("Enter organism name")
    sys.exit(1)

try:
    org_name = sys.argv[1]
except IndexError:
    print ("Need organism name", file=sys.stderr)
    sys.exit(1)

# find names in database that are equal to user provided name
list_names = list(Name.select(Name.q.name==org_name))
if not list_names:
    print ("No matches for given name found")  # error message if name not found

# iterates over each name if multiple names are found
for name in list_names:
    taxonomy = name.taxonomy
    print("Taxonomic lineage for",org_name,":")

    r = taxonomy  
    lineage = []  # list for storing lineage
    while r.parent is not None and r != r.parent:
        lineage.append(r.scientific_name)  # we add scientific name to the list until the end is reached 
        r = r.parent
    lineage.append(r.scientific_name) # we also add the root (the end name)

    for level in reversed(lineage):   # we print out in reversed manner so that it starts from the root
        print(level)
    

