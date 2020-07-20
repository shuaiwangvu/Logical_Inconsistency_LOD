

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter
import difflib

PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)

sameas = "http://www.w3.org/2002/07/owl#sameAs"
equivalent = "http://www.w3.org/2002/07/owl#equivalentClass"

(triples, cardinality) = hdt_file.search_triples("", sameas, "")
print ('there are in total: ', cardinality, ' sameAs triples')

collect_sameas_nodes = set()
for (s, p, o) in triples :
    if s == o:
        collect_sameas_nodes.add(s)
print ('Among them, there are in total ', len (collect_sameas_nodes), ' reflexive arrows')



(triples, cardinality) = hdt_file.search_triples("", equivalent, "")
print ('there are in total: ', cardinality, ' equivalent triples')

collect_sameas_nodes = set()
for (s, p, o) in triples :
    if s == o:
        collect_sameas_nodes.add(s)
print ('Among them, there are in total ', len (collect_sameas_nodes), ' reflexive arrows')
