# Exercise 25 model.py Sarada Giridharan

# Write a python program using SQLObject to find the taxonomic lineage of a user-supplied organism name.

from sqlobject import *
import os.path, sys

dbfile = 'small_taxa.db3'

def init(new=False):
    # Magic formatting for database URI
    conn_str = os.path.abspath(dbfile)
    conn_str = 'sqlite:'+ conn_str
    # Connect to database
    sqlhub.processConnection = connectionForURI(conn_str)
    if new:
            # Create new tables (remove old ones if they exist)
            Taxonomy.dropTable(ifExists=True)
            Name.dropTable(ifExists=True)
            Taxonomy.createTable()
            Name.createTable()

class Taxonomy(SQLObject):
    taxid = IntCol(alternateID=True)
    scientific_name = StringCol()
    rank = StringCol()
    parent = ForeignKey("Taxonomy")

class Name(SQLObject):
    taxonomy = ForeignKey("Taxonomy")
    name = StringCol()
    name_class = StringCol()

