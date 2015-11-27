__author__ = 'Gabriela'
import pandas as ps
import numpy as np
import time
from PageRankAirports import *
start_time = time.time()

# Read airports and routes

airports = ps.read_csv('airports.txt', header=None)
routes_input = ps.read_csv('routes.txt', header=None)

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

#idx = ps.unique(airports.IATA.ravel())
idx_n = np.arange(5742)
hashT = airports[['AirportID', 'AirportName', 'IATA']]
#airports = hashT.set_index(idx)
hashT = hashT.set_index(idx_n)
vertices = airports[['IATA']]
vertices = vertices.set_index(idx_n)
vertices = vertices.sort_values(by = 'IATA', axis = 0)
#vertices = vertices.reset_index()
vertices = vertices.set_index(idx_n)




# Table for routes:

routes = routes_input.rename(columns ={0 : 'AirlineCode', 1: 'OF-AirlineCode',
                                     2: 'OrgIATA', 3: 'OFCode', 4: 'DstIATA'})

routes = routes[['OrgIATA', 'DstIATA']]

routes_clean = routes[(routes.OrgIATA.isin(hashT.IATA)) & (routes.DstIATA.isin(hashT.IATA))]


out_j = routes_clean.groupby(['OrgIATA']).size().reset_index()
out_j= out_j.rename(columns={0: 'Out_j'})

#edges_from_to = routes_clean.groupby(['OrgIATA', 'DstIATA']).size().reset_index()

#print(edges_from_to)

#edges_from_to= edges_from_to.rename(columns={0: 'Weight'})
#eft = edges_from_to.groupby('OrgIATA')['DstIATA'].apply(lambda x: x.tolist()).reset_index()
#eft2 = edges_from_to.groupby(['OrgIATA']).Weight.sum()

#print(eft)
#print(eft2)
#eft2 = edges_from_to.groupby('OrgIATA')['Weight'].apply(lambda x: x.tolist()).reset_index()

#eft3 = ps.concat([eft.OrgIATA, eft.DstIATA, eft2.Weight], axis=1)

#print(eft2)
#print(routes.groupby(['OrgIATA']).size().reset_index())

#edges_from_to = edges_from_to.reset_index()
#edges_from_to = edges_from_to.rename(columns={0: 'Weight'})


edges_to_from = routes_clean.groupby(['OrgIATA', 'DstIATA']).size().reset_index()
etf = edges_to_from.groupby('DstIATA')['OrgIATA'].apply(lambda x: x.tolist()).reset_index()
etf2 = edges_to_from.groupby('DstIATA')[0].apply(lambda x: x.tolist()).reset_index()
etf2= etf2.rename(columns={0: 'Weight'})

# Airports Graph
#df['c'] = df.apply(lambda row: df.groupby('a').get_group(row['a'])['b'].tolist(), axis=1)
#df

#routes_clean['Weight'] =  routes_clean.apply(lambda row: routes_clean.groupby('DstIATA').get_group(row['DstIATA'])['OrgIATA'].tolist(), axis=1)

#print(routes_clean.groupby('DstIATA')['OrgIATA'].apply(lambda x: x.tolist()).reset_index())
#print(edges_to_from)
#print(etf)
#print(etf2)
#print(routes_clean.groupby(['OrgIATA', 'DstIATA']).size())

airports_i = ps.concat([etf.DstIATA, etf.OrgIATA, etf2.Weight], axis = 1)
#print(eft3)
#print(vertices)
#print(etf3)
#print(out_j)

### DEAD ENDS : nodes with no outgoing routes:

idx_de = vertices.IATA.isin(out_j.OrgIATA)
deadEnds_idx = vertices.index[~idx_de].values

## Nodes with no incoming routes:

idx_ne = vertices.IATA.isin(etf2.DstIATA)
no_input = vertices[~idx_ne]
no_input_idx = no_input.index.values

## Vertices - vertices with no incoming routes

vertices_rest = vertices[~vertices.IATA.isin(no_input.IATA)]

pr = page_rank(vertices, vertices_rest,airports_i,out_j, deadEnds_idx, no_input_idx)

print(sum(pr))

#TEST

# pointed_by = airports_i.OrgIATA[airports_i.DstIATA == 'AAE'].values[0]
# weights = airports_i.Weight[airports_i.DstIATA == 'AAE'].values[0]
# outs = out_j.Out_j[out_j.OrgIATA.isin(pointed_by)].values
# idx_j = vertices.index[vertices.IATA.isin(pointed_by)].values
# #print(airports_i)
# print(pointed_by)
# print(weights)
# print(outs)
# print(idx_j)


#print(vertices.loc[vertices.IATA=='ALG'])
#print(out_j)
#print(vertices_rest)
#print(len(no_input_idx))


#print(not_in_edges_idx)

#print(not_in_edges_idx)
#print(deadEnds_idx)
#print(not_in_edges_idx)
#print(len(deadEnds_idx))
#print(len(not_in_edges_idx))
#print(out_j)
#print(etf3)

#print(not_in_edges_idx)
#dead_ends = dead_ends.IATA.values
#print(idx_de)
#print(dead_ends)
  #  mask = (vertices['IATA'].isin(dead_ends))
  #  idx_code = vertices.index[mask].values
  #  p2 = p[idx_code]
  #  add = p2/n
  #  add = sum(add)
  #  return add


#print(etf2)
#print(etf.DstIATA[etf.DstIATA.isin(['AAE'])])

#print(routes_clean.groupby('DstIATA', 'OrgIATA')[0].apply(lambda x: x.tolist()))


#edges_to_from = routes_clean.groupby(['DstIATA','OrgIATA']).size().reset_index()



#edges_to_from  = routes_clean.apply(routes_clean.groupby(['DstIATA', 'OrgIATA'])['OrgIATA'].tolist())
#DataFrame({'count' : df1.groupby( [ "Name", "City"] ).size()}).reset_index()
#edges_to_from = edges_to_from.reset_index()
#edges_to_from = edges_to_from.rename(columns={0: 'Weight'})

#print(routes_clean)

#print(edges_from_to)

#print(edges_to_from)
#s = dict(list(routes_clean .groupby(['DstIATA','OrgIATA'])))
#print(s)
print("--- %s seconds ---" % (time.time() - start_time))
#print(routes)
#print(routes_clean)


#out_j = routes.groupby(['DstIATA']).size()

#print(edges_from_to)
#print(edges_test)
#print(edges_to_from)
#print(out_j)
#print(routes)
#print(routes2)
#print(edgesT)
#print(edgesP)