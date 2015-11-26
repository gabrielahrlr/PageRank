__author__ = 'Gabriela'

import pandas as ps
import numpy as np
import time
#from main import *
from PRcomputation import *
from pr_test import *

start_time = time.time()

airports = ps.read_csv('airports.txt', header=None)
routes = ps.read_csv('routes.txt', header=None)

#Cleaning data

airports = airports.rename(columns ={0 : 'AirportID', 1: 'AirportName',
                                     2: 'MainCity', 3: 'Country', 4: 'IATA', 5: 'ICAO'})
airports = airports[ps.notnull(airports['IATA'])]

# Finding duplicated IATA codes

dup = airports.IATA[airports.IATA.duplicated()].values
val = ['BFT', 'ZYA']
dupRows = airports[airports['IATA'].isin(val)]


# 1st Assumption: Eliminate duplicated airports whit the same IATA code

airports = airports.drop([3670, 6271])

#  Hash Table for airports:

idx = ps.unique(airports.IATA.ravel())
idx_n = np.arange(5742)
hashT = airports[['AirportID', 'AirportName', 'IATA']]
airports = hashT.set_index(idx)
hashT = hashT.set_index(idx_n)
vertices = airports[['IATA']]
vertices = vertices.set_index(idx_n)
vertices = vertices.sort_values(by = 'IATA', axis = 0)
#vertices = vertices.reset_index()
vertices = vertices.set_index(idx_n)



# Table for routes:

routes = routes.rename(columns ={0 : 'AirlineCode', 1: 'OF-AirlineCode',
                                     2: 'OrgIATA', 3: 'OFCode', 4: 'DstIATA'})

routes= routes[['OrgIATA', 'DstIATA']]


# EDGES Computation

edgesT = routes.groupby(['OrgIATA', 'DstIATA']).size()
#edgesT = edgesT.rename(columns={0: 'Weight'})
edges = edgesT.reset_index()
edges = edges.rename(columns={0: 'Weight'})
mask = edges['OrgIATA'].isin(hashT.IATA)
not_in_Ver = edges[~mask]
edges_C = edges[edges['OrgIATA'].isin(hashT.IATA)]
edges_Clean = edges_C[edges_C['DstIATA'].isin(hashT.IATA)]

pr = page_rank(vertices, edges_Clean)
#np.savetxt("foo5.csv", pr, delimiter=",")
print(sum(pr))

# Compute the



#pointed_by = edges_Clean.OrgIATA[edges_Clean.DstIATA == 'AAL'].values
#print(edges_Clean[(edges_Clean.OrgIATA.isin(pointed_by)) & (edges_Clean.DstIATA == 'AAL')])
#print(vertices[vertices.IATA.isin(pointed_by)])
# filtering = vertices[vertices.IATA.isin(pointed_by)]
# idx_j = filtering.index.values
# print(vertices[vertices.IATA.isin(pointed_by)])
# print(idx_j)
# # filtering = vertices[vertices.IATA.isin(pointed_by)]
# # idx_j = filtering.index.values
# #airports_j = filtering.IATA.values
# g = edges[(edges.OrgIATA.isin(pointed_by)) & (edges.DstIATA == 'POM')]
# w_ji = g.Weight.values
# mask = (edges['OrgIATA'].isin(pointed_by))
# out_j = edges[mask]
# out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
# #i_j = hashT.index[hashT.IATA.isin(g.OrgIATA)]
#
# print(pointed_by)
# print(idx_j)
# #print(airports_j)
# print(w_ji)
# print(out_j)
# print(edges_Clean[edges_Clean.OrgIATA.isin(pointed_by)])
# print(edges.loc[edges.DstIATA == 'POM'])
# print(hashT.loc[hashT.IATA.isin(['BNE', 'BUA', 'BUL', 'CEB'])])


#n = len(vertices)
#p = np.ones(n)/n
# sum_de =dead_ends(vertices, edges_Clean, p)
# pointed_by = edges_Clean.OrgIATA[edges_Clean.DstIATA == 'POM'].values
# filtering = vertices[vertices.IATA.isin(pointed_by)]
# airports =filtering.IATA.values
# idx_j = filtering.index.values
# g = edges_Clean[(edges_Clean.OrgIATA.isin(pointed_by)) & (edges_Clean.DstIATA == 'POM')]
# w_ji = g.Weight.values
# mask = (edges['OrgIATA'].isin(pointed_by))
# out_j = edges[mask]
# out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
# p_j = p[idx_j]
# sum_ji = p_j*w_ji
# sum_ji = sum_ji/out_j
# sum_ji = sum(sum_ji + sum_de)
# #print(edges_Clean[edges_Clean.OrgIATA == 'BUL'])
# #print(edges_Clean[edges_Clean.DstIATA == 'POM'])
# #print(airports)
# print(idx_j)
# print(len(idx_j))
# print(w_ji)
# print(len(w_ji))
# print(out_j)
# print(len(out_j))
# print(p_j)
# print(len(p_j))
# print(sum_ji)
#print(edges_Clean.Weight[edges_Clean.OrgIATA == 'ALG'].sum())

# idx_de = vertices['IATA'].isin(edges_Clean.OrgIATA)
# dead_ends = vertices[~idx_de].IATA.values
# mask = (vertices['IATA'].isin(dead_ends))
# idx_code = vertices.index[mask].values
# p2 = p[idx_code]
# add = p2/n
# add = sum(add)
# print(add)
# print(idx_de)
# print(dead_ends)
# print(idx_code)


print("--- %s seconds ---" % (time.time() - start_time))
