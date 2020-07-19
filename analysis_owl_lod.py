# analysis of three different RDF schemas:
    # Just RDF Schema has three versions:
    # 1) https://www.w3.org/2000/01/rdf-schema#
    # 2) http://www.w3.org/2000/01/rdf-schema-more
    # 3) http://www.w3.org/2000/01/combined-ns-translation.rdf.fr
    # linked by see also
    # http://www.w3.org/2000/01/rdf-schema# http://www.w3.org/2000/01/rdf-schema#seeAlso http://www.w3.org/2000/01/rdf-schema-more
    # in the more but not the original :
    # http://www.w3.org/2000/01/rdf-schema# http://www.w3.org/2000/01/rdf-schema#seeAlso http://www.w3.org/2000/01/combined-ns-translation.rdf.fr

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter
import difflib


PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)

# create a Graph
g = rdflib.Graph()

subClassOf = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
type = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
# parse in an RDF file hosted on the Internet

result = g.parse("https://www.w3.org/2002/07/owl")


count = 0
collect_triple_owl = set()
collect_nodes = set()
# loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    count += 1
    collect_triple_owl.add((str(subj), str(pred), str(obj)))
    collect_nodes.add (subj)
    collect_nodes.add (obj)

print('**** In the original OWL scheme ****')
print('there are in total ', len(collect_triple_owl), ' Triples' )
print('there are in total ', len(collect_nodes), ' Nodes' )


collect_triple_owl_lod = set()
count_relations_between_nodes = Counter()

for s in collect_nodes:
    for o in collect_nodes:
        (triples, cardinality) = hdt_file.search_triples(s, '', o)
        for (s, p, o) in triples :
            # if (s, p ,o) not in collect_triple_owl:
            collect_triple_owl_lod.add((str(s), str(p), str(o)))

print('# collect triple in LOD: ', len (collect_triple_owl_lod))
collect_extra = collect_triple_owl_lod.difference(collect_triple_owl)
print ('# extra: ', len(collect_extra))
for (s, p, o) in collect_extra:
    print ('They are:', s, p, o)


#
# for subj, pred, obj in collect_triple_owl:
#     if pred == subClassOf:
#         print (subj, obj)



print ('count = ',count)

#
#     # if (subj, pred, obj) not in g:
#     #    raise Exception("It better be!")
# # http://www.w3.org/2000/01/rdf-schema-more
#
# print ('---- and more ----')
#
# result = g.parse("http://www.w3.org/2000/01/rdf-schema-more")
# print (result)
# count = 0
# collect_triple_owl_more = set()
# # loop through each triple in the graph (subj, pred, obj)
# for subj, pred, obj in g:
#     # check if there is at least one triple in the Graph
#     count += 1
#     collect_triple_owl_more.add((subj, pred, obj))
#     if "http://www.w3.org/2000/01/rdf-schema#subClassOf" in subj:
#         print (subj, pred, obj)
#     if "http://www.w3.org/2000/01/rdf-schema#seeAlso" in pred:
#         print ('[MORE]SEE ALSO: ',subj, pred, obj)
#
#
# print ('count more = ', count)
#
#
# print ('================')
# for (s, p, o) in collect_triple_owl_more.difference(collect_triple_owl):
#     print ('in MORE but not in ORIGINAL: ', s, p , o)
#
#
# print ('================')
# for (s, p, o) in collect_triple_owl.difference(collect_triple_owl_more):
#     print ('in ORIGINAL but not in MORE: ', s, p , o)
#
#
# # http://www.w3.org/2000/01/combined-ns-translation.rdf.fr
#
# result = g.parse("http://www.w3.org/2000/01/combined-ns-translation.rdf.fr")
# print (result)
# count = 0
# collect_triple_owl_more = set()
# # loop through each triple in the graph (subj, pred, obj)
# for subj, pred, obj in g:
#     # check if there is at least one triple in the Graph
#     count += 1
#     collect_triple_owl_more.add((subj, pred, obj))
#     if "http://www.w3.org/2000/01/rdf-schema#subClassOf" in subj:
#         print (subj, pred, obj)
# print ('count French = ', count)
