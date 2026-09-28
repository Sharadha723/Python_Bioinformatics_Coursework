# Exercise 14.1 Sarada Giridharan

# Write a program to pick out, and print, the references of a XML format UniProt entry, in a nicely formatted way.

# importing necessary packages
import xml.etree.ElementTree as ET
import urllib.request

# getting and opening file
thefile = urllib.request.urlopen(
                         'http://www.uniprot.org/uniprot/Q9H400.xml')

# parsing file and getting root
document = ET.parse(thefile)
root = document.getroot()

# defining namespace
ns = '{http://uniprot.org/uniprot}'

# finding entry
entry = root.find(ns+'entry')

# getting appropriate things from the reference (after finding it) and printing them out in a nicely formatted way
print("References:\n")
for ref in entry.findall(ns+'reference'):
    citation = ref.find(ns+'citation')

    # getting reference number
    if citation is not None:
        print("Reference", ref.get('key'))

        # printing authors as a list of names separated by commas first 
        authors = citation.find(ns+'authorList')
        if authors is not None:
                auth_name = ",".join([author.get('name')for author in authors.findall(ns+'person')])  
                if auth_name:
                    print("    Authors:",auth_name)
                else:
                    print("    Author name not found")
       

        # getting title and printing that next
        title = citation.find(ns+'title')
        if title is not None:
            print("    Title:","'"+title.text+"'")
        else:
            print("    Title not found")

        # getting other details from citation and printing them
        print("    Type:", citation.get('type', 'type not found'))
        print("    Date:", citation.get('date', 'date not found'))
        print("    Journal Name:", citation.get('name','Journal name not found'))
        print("    Volume:", citation.get('volume','volume not found'))
        print("    First page:", citation.get('first','first page not found'))
        print("    Last page:", citation.get('last','last page not found'))
        print("    db:", citation.get('db','db not found'))
    
        
        # printing database references next
        dbrefs = citation.findall(ns+'dbReference')
        if dbrefs:
           print("    dbReferences:")
           for dbref in dbrefs:
              print("    --Type:", dbref.get('type','type not found'),";","ID:", dbref.get('id','id not found'))
        else:
           print("    dbReference not found")

        # printing scopes as last item 
        scopes = ref.findall(ns+'scope')
        if scopes:
            print("    Scopes:")
            for scope in scopes:
                print("    --",scope.text)
        else:
           print("    Scopes not found")

        # printing an empty line to differentiate between 2 references.
        print()
   


