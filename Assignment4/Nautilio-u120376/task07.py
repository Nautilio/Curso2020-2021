# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uwgMguSiKe1AT0SUqpcEo6ZKeg9n7Fpe

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery

query2 = prepareQuery('''
  SELECT 
    ?s
	WHERE { 
    ?s rdfs:subclassOf ns:Person.
  } 
  ''',
  initNs = { "rdfs": RDFS,"ns":ns}
)

for r in g.query(query2):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""

ns = Namespace("http://somewhere#")
print("RDFLib:")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    print(s1)

print("SPARQL:")
from rdflib.plugins.sparql import prepareQuery

query3 = prepareQuery('''
  SELECT ?s1
  WHERE { 
    { 
      ?s1 rdf:type ns:Person. 
    } UNION {
      ?s2 rdfs:subClassOf ns:Person.
      ?s1 rdf:type ?s2
    }
  }
  ''',
  initNs = { "rdfs": RDFS,"rdf": RDF, "ns": ns}
)

for r in g.query(query3):
  print(r)
"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery


VCARD = Namespace("http://somewhere#/Person")


qt = prepareQuery('''
  SELECT 
    ?Person
  WHERE { 
    ?Person clave:FN ?FullName. 
  }
  ''',
  initNs = { "clave": VCARD}
)


for r in g.query(qt):
  print(r)