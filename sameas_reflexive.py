

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter
import difflib

PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)

sameas = "http://www.w3.org/2002/07/owl#sameAs"
equivalent = "http://www.w3.org/2002/07/owl#equivalentClass"
subClassOf = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
broader = "http://www.w3.org/2004/02/skos/core#broader"
narrower = "http://www.w3.org/2004/02/skos/core#narrower"
hasPart = "http://purl.org/dc/terms/hasPart"

predicate_list = [hasPart, narrower, broader, subClassOf, equivalent, sameas]

def find_how_many(predicate):
    print('For predicate: ', predicate)
    (triples, cardinality) = hdt_file.search_triples("", predicate, "")
    print ('there are in total: ', cardinality, ' triples')

    collect_nodes = set()
    count = 0
    for (s, p, o) in triples :
        count += 1
        if count % (int (cardinality/5)) == 0:
            print ('progress: ', count /cardinality)
        if s == o:
            collect_nodes.add(s)
    print ('Among them, there are in total ', len (collect_nodes), ' reflexive arrows')
    print ('There are ', (len(collect_nodes)/cardinality)*100, 'percent reflexive arrows')

for p in predicate_list:
    find_how_many(p)
