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
import difflib
# create a Graph
g = rdflib.Graph()

subClassOf = "http://www.w3.org/2000/01/rdf-schema#subClassOf"


print ('RDF: ')
result = g.parse("https://www.w3.org/1999/02/22-rdf-syntax-ns")
print (result)
count = 0
collect_triple_rdf = set()
# loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    count += 1
    collect_triple_rdf.add((str(subj), str(pred), str(obj)))

for subj, pred, obj in collect_triple_rdf:
    if pred == subClassOf:
        print (subj, obj)


g = rdflib.Graph()
print ('RDFS: ')
# parse in an RDF file hosted on the Internet
result = g.parse("https://www.w3.org/2000/01/rdf-schema")
print (result)
count = 0
collect_triple_rdfs = set()
# loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    count += 1
    collect_triple_rdfs.add((str(subj), str(pred), str(obj)))
    # check if there is at least one triple in the Graph
    # if subClassOf in subj:
        # print (subj, pred, obj)
        # print ('SUBJ:', subj [0], '-', subj[-1])
        # print ("http://www.w3.org/2000/01/rdf-schema#subClassOf")
        # if ("http://www.w3.org/2000/01/rdf-schema#subClassOf" == str(subj)):
        #     print ('But they are NOW equal!')
        #     print ('len subClassOf = ', len("http://www.w3.org/2000/01/rdf-schema#subClassOf"))
        #     print ('len subj       = ', len(subj))
        #     print ('type:',type(subj))
        #     print ('type:',type("http://www.w3.org/2000/01/rdf-schema#subClassOf"))
    # if "http://www.w3.org/2000/01/rdf-schema#seeAlso" in pred:
    #     print ('SEE ALSO: ',subj, pred, obj)


for subj, pred, obj in collect_triple_rdfs:
    if pred == subClassOf:
        print (subj, obj)








# print ('count = ',count)
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
# collect_triple_rdf_more = set()
# # loop through each triple in the graph (subj, pred, obj)
# for subj, pred, obj in g:
#     # check if there is at least one triple in the Graph
#     count += 1
#     collect_triple_rdf_more.add((subj, pred, obj))
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
# for (s, p, o) in collect_triple_rdf_more.difference(collect_triple_rdf):
#     print ('in MORE but not in ORIGINAL: ', s, p , o)
#
#
# print ('================')
# for (s, p, o) in collect_triple_rdf.difference(collect_triple_rdf_more):
#     print ('in ORIGINAL but not in MORE: ', s, p , o)
#
#
# # http://www.w3.org/2000/01/combined-ns-translation.rdf.fr
#
# result = g.parse("http://www.w3.org/2000/01/combined-ns-translation.rdf.fr")
# print (result)
# count = 0
# collect_triple_rdf_more = set()
# # loop through each triple in the graph (subj, pred, obj)
# for subj, pred, obj in g:
#     # check if there is at least one triple in the Graph
#     count += 1
#     collect_triple_rdf_more.add((subj, pred, obj))
#     if "http://www.w3.org/2000/01/rdf-schema#subClassOf" in subj:
#         print (subj, pred, obj)
# print ('count French = ', count)
