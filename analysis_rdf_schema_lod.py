# analysis of the original RDF schema against the LOD cloud and see what are the differences:

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter


PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)



# create a Graph
g = rdflib.Graph()
# count how many additional edges are between two nodes


# parse in an RDF file hosted on the Internet
result = g.parse("https://www.w3.org/2000/01/rdf-schema")
# print (result)
count = 0
collect_triple_rdf = set()
collect_nodes = set()
# loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    count += 1
    collect_triple_rdf.add((subj, pred, obj))
    collect_nodes.add (subj)
    collect_nodes.add (obj)

print('there are in total ', len(collect_triple_rdf), ' Triples' )
print('there are in total ', len(collect_nodes), ' Nodes' )


collect_triple_rdf_lod = set()
count_relations_between_nodes = Counter()

for s in collect_nodes:
    for o in collect_nodes:
        (triples, cardinality) = hdt_file.search_triples(s, '', o)
        for (s, p, o) in triples :
            # if (s, p ,o) not in collect_triple_rdf:
            collect_triple_rdf_lod.add(s, p, o)

print('# collect triple in LOD: ', len (collect_triple_rdf_lod))
collect_extra = collect_triple_rdf_lod.difference(collect_triple_rdf)
print ('# extra: ', len(collect_extra))
