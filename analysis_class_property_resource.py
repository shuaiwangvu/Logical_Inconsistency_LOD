# this file prints redundent relations between the following three nodes

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter


rdfs_class = "http://www.w3.org/2000/01/rdf-schema#Class"
rdfs_resource = "http://www.w3.org/2000/01/rdf-schema#Resource"
rdf_property = "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"
subClassOf = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
subPropertyOf = "http://www.w3.org/2000/01/rdf-schema#subPropertyOf"
owlClass = "http://www.w3.org/2002/07/owl#Class"

PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)
rdf = "https://www.w3.org/1999/02/22-rdf-syntax-ns"
rdfs = "https://www.w3.org/2000/01/rdf-schema"
owl = "https://www.w3.org/2002/07/owl"


g = rdflib.Graph()
result = g.parse(rdf)
result = g.parse(rdfs)
result = g.parse(owl)

collect_triple_original = set()
# loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    collect_triple_original.add((str(subj), str(pred), str(obj)))

def get_triple(subj, obj, triples):
    collect = set()
    for (s, p, o) in triples:
        if s == subj and o == obj:
            collect.add ((s, p, o))
    return collect


collect_nodes = [rdfs_class, rdfs_resource, rdf_property, subClassOf, subPropertyOf, owlClass]

collect_triple_lod = set()

for s in collect_nodes:
    for o in collect_nodes:
        (triples, cardinality) = hdt_file.search_triples(s, '', o)
        for (s, p, o) in triples :
            # if (s, p ,o) not in collect_triple_rdf:
            collect_triple_lod.add((str(s), str(p), str(o)))

for s in collect_nodes:
    for o in collect_nodes:
        print ('subj: ', s)
        print ('obj: ', o)
        for (s, p, o) in get_triple(s, o, collect_triple_original):
            print ('\toriginal: ', p)
        for (s, p, o) in get_triple(s, o, collect_triple_lod):
            print ('\t     lod: ', p)
