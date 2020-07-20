

import rdflib
from hdt import HDTDocument, IdentifierPosition
from collections import Counter
import difflib
import tldextract

PATH_LOD = "/scratch/wbeek/data/LOD-a-lot/data.hdt"
hdt_file =  HDTDocument(PATH_LOD)

sameas = "http://www.w3.org/2002/07/owl#sameAs"
equivalent = "http://www.w3.org/2002/07/owl#equivalentClass"
subClassOf = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
broader = "http://www.w3.org/2004/02/skos/core#broader"
narrower = "http://www.w3.org/2004/02/skos/core#narrower"
hasPart = "http://purl.org/dc/terms/hasPart"

predicate_list = [hasPart, narrower, broader, subClassOf, equivalent, sameas]


def get_domain(t):
    return tldextract.extract(t).domain

def get_domain_and_label(t):
    domain = tldextract.extract(t).domain
    name1 = t.rsplit('/', 1)[-1]
    name2 = t.rsplit('#', 1)[-1]
    if len(name2) < len(name1):
        return (domain, name2)
    else:
        return (domain, name1)


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

# for p in predicate_list:
#     find_how_many(p)

# find out the domain and count them:
(triples, cardinality) = hdt_file.search_triples("", sameas, "")
print ('there are in total: ', cardinality, ' triples')
ct_domain = Counter()
ct_name = Counter()
# ct[] += 1
count = 0
for (s, p, o) in triples:
    if s == o:
        count += 1
        domain = get_domain(s)
        ct_domain[domain] += 1
        # ct_name[name] += 1

        if count % (int (cardinality/100000)) == 0:
            print ('progress: ', count /cardinality)
            print (ct_domain)
        if count > cardinality/1000:
            break

for n in ct_domain:
    if ct_domain[n] > 10:
        print ('DOMAIN: ', ct_domain[n])


# for n in ct_name:
#     if ct_name[n] > 5:
#         print ('NAME: ', ct_name[n])
