# this file prints redundent relations between the following three nodes

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter


rdfs_class = "http://www.w3.org/2000/01/rdf-schema#Class"
rdfs_resource = "http://www.w3.org/2000/01/rdf-schema#Resource"
rdf_property = "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"

PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)
rdf = "https://www.w3.org/1999/02/22-rdf-syntax-ns"
rdfs = "https://www.w3.org/2000/01/rdf-schema"
owl = "https://www.w3.org/2002/07/owl"


collect_nodes = [rdfs_class, rdfs_resource, rdf_property]

collect_triple_lod = set()

for s in collect_nodes:
    for o in collect_nodes:
        (triples, cardinality) = hdt_file.search_triples(s, '', o)
        for (s, p, o) in triples :
            # if (s, p ,o) not in collect_triple_rdf:
            collect_triple_lod.add((str(s), str(p), str(o)))

for (s, o, p) in collect_triple_lod:
    print ('all relations: ', s, o, p)
