__author__ = 'Gabriela & Maìra'

import pandas as ps
import numpy as np
import time
#import networkx as nx
#import os
#from Graph import graph
from pr_test import pageRank


start_time = time.time()
# Read airports and routes

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



# Table for routes:

routes = routes.rename(columns ={0 : 'AirlineCode', 1: 'OF-AirlineCode',
                                     2: 'OrgIATA', 3: 'OFCode', 4: 'DstIATA'})

routes= routes[['OrgIATA', 'DstIATA']]


# EDGES Computation

edgesT = routes.groupby(['OrgIATA', 'DstIATA']).size()
#edgesT = edgesT.rename(columns={0: 'Weight'})
edges = edgesT.reset_index()
edges = edges.rename(columns={0: 'Weight'})
edges = edges[edges['OrgIATA'].isin(hashT.IATA)]

#nod =  vertices.loc[vertices.index[5738]].IATA
#nodew = vertices[vertices.index==5738].IATA.values[0]
#orgAirports = edges.loc[edges.DstIATA == nodew].OrgIATA.tolist()
#print(nod)

#print(edges)
#g = graph(vertices, edges)


pr = pageRank(hashT, edges)
#np.savetxt("foo2.csv", pr, delimiter=",")

#print(pr)
print('sum of PR', sum(pr))
#print(g['TSE']['k'])
#pr = pageRank(g)
#print(pr)
#print(sum(pr))
#print(g)
print("--- %s seconds ---" % (time.time() - start_time))



#print(hashT.head())
#print(edges.head())

#graph = {j: g['DstIATA'].tolist() for j,g in edges.groupby('OrgIATA') }

#airportEdges = edges.loc[edges['OrgIATA'] == 'AAE']
#airportOutj = airportEdges.Weight.sum()


#print(airportEdges)
#print(airportOutj)
#dup2 = edges[edges.OrgIATA.duplicated()]
#print(len(vertices))
#print(edges)


#print(vertices)
#print(edges.loc[vertices['IATA']=='GKA'])
#print(edges)
#print(edges.loc[edges['OrgIATA']== 'AAE'])
# Graph


#DG = DG.add_node(verti)

#print(type(verti))
#print(DG.out_degree('ALG',weight='weight'))


# dup2 = routes[routes.duplicated()]





#print(hash.loc['IATA'] = 'BFT')
#print(hash.IATA[hash.IATA.duplicated()].values)

#dict = {'Name': 'Zara', 'Age': {'ARE': 2,  'REF':3, 2:'SWE'}, 'Class': 'First'}

#print(dict)
#print(dict['Age'][2])

#hash = hash.reindex(index= index)

#print(len(hash), len(index))
#print(hash)
#print(airports.loc[0,'AirportName'])