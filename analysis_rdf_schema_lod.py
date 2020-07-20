# analysis of the original RDF schema against the LOD cloud and see what are the differences:

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter


PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)
rdf = "https://www.w3.org/1999/02/22-rdf-syntax-ns"
rdfs = "https://www.w3.org/2000/01/rdf-schema"
owl = "https://www.w3.org/2002/07/owl"

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

    # print('# collect triple in LOD: ', len (collect_triple_lod))
    collect_extra = collect_triple_lod.difference(collect_triple)
    collect_not_included = collect_triple.difference(collect_triple_lod)

    return collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included


print ('FOR RDF')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(rdf)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected. ')
print ('there are ', len(collect_extra), ' extra triples found. ')
print ('there are ', len(collect_not_included), ' triples not included in LOD. ')

print ('FOR RDFS')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(rdfs)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected. ')
print ('there are ', len(collect_extra), ' extra triples found. ')
print ('there are ', len(collect_not_included), ' triples not included in LOD. ')

print ('FOR OWL')

collect_triple, collect_nodes, collect_triple_lod, collect_extra, collect_not_included =  compute_extra(owl)
print ('there are ', len(collect_triple), ' triples collected, which consists of ', len(collect_nodes), ' nodes')
print ('there are ', len(collect_triple_lod), ' triples collected. ')
print ('there are ', len(collect_extra), ' extra triples found. ')
print ('there are ', len(collect_not_included), ' triples not included in LOD. ')
