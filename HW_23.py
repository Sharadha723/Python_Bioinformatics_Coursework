# Exercise 23 Sarada Giridharan

# Write a python program to lookup the scientific name for a user-supplied organism name.

# import necessary packages
import sys
import sqlite3

# print error message if common name not given
if len(sys.argv) < 2:
    print ("Insufficient arguments provided")
    sys.exit()

# get common name from command line
common_name = sys.argv[1]

conn = sqlite3.connect('taxa.db3')
params = [common_name]
c = conn.cursor()

# execute query to get tax id for common name
c.execute("""
   SELECT * from name
   WHERE name = ? 
   AND (name_class = 'common name' OR name_class = 'genbank common name');
   """,params)

# iterate over result rows
found_name = False  # for error handling
for row in c:
   tid = row[1]
   found_name = True
   break

if not found_name:
    print("Name not found")
else:
    # if records were found, execute second query to get scientific name from tax id
    params2 = [tid]

    c.execute("""
        SELECT * from taxonomy
        WHERE tax_id = ?;
        """,params2)

    # iterate over second query results
    found_scientific_name = False
    for row in c:
        print("Scientific name:",row[1])
        found_scientific_name = True

    if not found_scientific_name:
        print("Scientific name not found")

# close database connection
conn.close()

