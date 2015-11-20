__author__ = 'Gabriela & Maìra'

import pandas as ps
import numpy as np
import networkx as nx
import os





# Read airports and routes

airports = ps.read_csv('~/Documents/GitHub/Lab3-IR/airports.txt', header=None)
routes = ps.read_csv('~/Documents/GitHub/Lab3-IR/routes.txt', header=None)

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
hashT = airports[['AirportID', 'AirportName', 'IATA']]
vertices = hashT.set_index(idx)

# Table for routes:

routes = routes.rename(columns ={0 : 'AirlineCode', 1: 'OF-AirlineCode',
                                     2: 'OrgIATA', 3: 'OFCode', 4: 'DstIATA'})

routes= routes[['OrgIATA', 'DstIATA']]


# EDGES Computation

edges = routes.groupby(['OrgIATA', 'DstIATA']).size()
edges = edges.reset_index()
edges = edges.rename(columns={0: 'Weight'})

airportEdges = edges.loc[edges['OrgIATA'] == 'AAE']
airportOutj = airportEdges.Weight.sum()
#print(airportEdges)
#print(airportOutj)
#dup2 = edges[edges.OrgIATA.duplicated()]
#print(len(vertices))
#print(edges)

print(edges)


# Graph
verti = vertices.index.values.tolist()
DG = nx.DiGraph()
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