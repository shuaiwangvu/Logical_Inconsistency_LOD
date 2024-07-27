# analysis of the original RDF, RDF schema, and OWL, against the LOD-a-lot file.
# The output are in the file output.txt and has been manually examined and checked.
# Contact: Shuai Wang (shuai.wang@vu.nl)

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter


PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)
rdf = "https://www.w3.org/1999/02/22-rdf-syntax-ns"
rdfs = "https://www.w3.org/2000/01/rdf-schema"
owl = "https://www.w3.org/2002/07/owl"

#print only edges that are useful for our plot.
nodes_drawing = ['http://www.w3.org/1999/02/22-rdf-syntax-ns#type',
'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property',
'http://www.w3.org/2000/01/rdf-schema#subClassOf',
'http://www.w3.org/2000/01/rdf-schema#subPropertyOf',
'http://www.w3.org/2000/01/rdf-schema#Resource',
'http://www.w3.org/2000/01/rdf-schema#Class',
'http://www.w3.org/2002/07/owl#Class',
'http://www.w3.org/2002/07/owl#Nothing',
'http://www.w3.org/2002/07/owl#Thing',
'http://www.w3.org/2002/07/owl#sameAs']

def compute_extra (name):

    # create a Graph
    g = rdflib.Graph()
    # count how many additional edges are between two nodes


    # parse in an RDF file hosted on the Internet
    result = g.parse(name)

    # print (result)
    count = 0
    collect_triple = set()
    collect_nodes = set()
    # loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        count += 1
        collect_triple.add((str(subj), str(pred), str(obj)))
        collect_nodes.add (subj)
        collect_nodes.add (obj)

    # print('**** In the original RDF ****')
    # print('there are in total ', len(collect_triple_rdf), ' Triples' )
    # print('there are in total ', len(collect_nodes), ' Nodes' )


    collect_triple_lod = set()
    count_relations_between_nodes = Counter()

    for s in collect_nodes:
        for o in collect_nodes:
            (triples, cardinality) = hdt_file.search_triples(s, '', o)
            for (s, p, o) in triples :
                # if (s, p ,o) not in collect_triple_rdf:
                collect_triple_lod.add((str(s), str(p), str(o)))
            (triples, cardinality) = hdt_file.search_triples(o, '', s)
            for (o, p, s) in triples :
                # if (s, p ,o) not in collect_triple_rdf:
                collect_triple_lod.add((str(o), str(p), str(s)))

    # print('# collect triple in LOD: ', len (collect_triple_lod))
    collect_extra = collect_triple_lod.difference(collect_triple)
    collect_not_included = collect_triple.difference(collect_triple_lod)

    return collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included


print ('FOR RDF')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(rdf)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected in LOD. ')
print ('there are ', len(collect_extra), ' extra triples found. ')

for (s, p ,o) in collect_extra:
    if s in nodes_drawing and o in nodes_drawing:
        print (s, p, o)


print ('there are ', len(collect_not_included), ' triples not included in LOD. ')
for (s, p ,o) in collect_not_included:
    if s in nodes_drawing and o in nodes_drawing:
        print (s, p, o)




print ('FOR RDFS')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(rdfs)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected in LOD. ')
print ('there are ', len(collect_extra), ' extra triples found. ')

for (s, p ,o) in collect_extra:
    if s in nodes_drawing and o in nodes_drawing:
        if 'http://www.w3.org/2000/01/rdf-schema#subClassOf' in p or 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' in p:
            print (s, p, o)

print ('there are ', len(collect_not_included), ' triples not included in LOD. ')
for (s, p ,o) in collect_not_included:
    if s in nodes_drawing and o in nodes_drawing:
        if 'http://www.w3.org/2000/01/rdf-schema#subClassOf' in p or 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' in p:
            print (s, p, o)

print ('FOR OWL')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(owl)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected in LOD. ')
print ('there are ', len(collect_extra), ' extra triples found. ')

for (s, p ,o) in collect_extra:
    if s in nodes_drawing and o in nodes_drawing:
        if 'http://www.w3.org/2000/01/rdf-schema#subClassOf' in p or 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' in p:
            print (s, p, o)

print ('there are ', len(collect_not_included), ' triples not included in LOD. ')
for (s, p ,o) in collect_not_included:
    if s in nodes_drawing and o in nodes_drawing:
        print (s, p, o)
