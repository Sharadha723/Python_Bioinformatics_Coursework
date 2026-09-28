# Exercise 24 Sarada Giridharan

# Write a python program using SQLObject to lookup the scientific name for a user-supplied organism name.

# import necessary packages
from model import *
import sys

# print error message if name not provided
if len(sys.argv) < 2:
    print("Please provide an organism name.")
    sys.exit()

org_name = sys.argv[1]

# get scientific name by getting taxa related to the name and thereby their scientific name
try:
    name_entry = Name.selectBy(name=org_name)[0]
    taxonomy_entry = name_entry.taxa
    print("Scientific name:", taxonomy_entry.scientificName)

except IndexError:
    print ("Name not found")
