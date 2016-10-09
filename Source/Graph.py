import pandas as ps
import time
from Source.PageRankDef import *
__author__ = 'Gabriela'

#############################################################################################
# This script  creates the Airport and Routes Network, and computes the
# Page Rank Algorithm to find the most connected airports with its correspondent rank.
#############################################################################################

# Read airports and routes
airports = ps.read_csv('../Data/airports.txt', header=None)
routes_input = ps.read_csv('../Data/routes.txt', header=None)

# Cleaning data
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
idx_n = np.arange(5742)
hashT = airports[['AirportID', 'AirportName', 'IATA']]
hashT = hashT.set_index(idx_n)
names_Airports =airports[['IATA','AirportName']]
names_Airports = names_Airports.sort_values(by='IATA', axis=0).reset_index()
vertices = airports[['IATA']]
vertices = vertices.set_index(idx_n)
vertices = vertices.sort_values(by='IATA', axis=0)
vertices = vertices.set_index(idx_n)
nodes = vertices.reset_index().set_index('IATA')

# Development of the "Graph" :
routes = routes_input.rename(columns ={0 : 'AirlineCode', 1: 'OF-AirlineCode',
                                     2: 'OrgIATA', 3: 'OFCode', 4: 'DstIATA'})
routes = routes[['OrgIATA', 'DstIATA']]
routes_clean = routes[(routes.OrgIATA.isin(hashT.IATA)) & (routes.DstIATA.isin(hashT.IATA))]
out_j = routes_clean.groupby(['OrgIATA']).size().reset_index()
out_j = out_j.rename(columns={0: 'Out_j'})
out_j2 = out_j.set_index('OrgIATA')
r = routes_clean.rename(columns={'OrgIATA': 'IATA'})
r= r.join(nodes, on='IATA')
r = r.rename(columns={'IATA': 'OrgIATA'})
r =r.join(out_j2, on='OrgIATA')
edges_r = r.groupby(['DstIATA', 'index']).size().reset_index()
edges_r2 = edges_r.groupby('DstIATA')['index'].apply(lambda x: x.tolist()).reset_index()
edges_r2 = edges_r2.rename(columns={'index': 'OrgIATA'})
edges_r3 = edges_r.groupby('DstIATA')[0].apply(lambda x: x.tolist()).reset_index()
edges_r3 = edges_r3.rename(columns={0: 'Weight'})
ed_o = r.groupby(['DstIATA','OrgIATA', 'Out_j']).size().reset_index()
ed_o2 = ed_o.groupby(['DstIATA'])['Out_j'].apply(lambda x: x.tolist()).reset_index()
airports_i = ps.concat([edges_r2.DstIATA, edges_r2.OrgIATA, edges_r3.Weight, ed_o2.Out_j], axis = 1)


# DEAD ENDS : nodes with no outgoing routes:
idx_de = vertices.IATA.isin(out_j.OrgIATA)
deadEnds_idx = vertices.index[~idx_de].values

# Nodes with no incoming routes:
idx_ne = vertices.IATA.isin(airports_i.DstIATA)
no_input = vertices[~idx_ne]
no_input_idx = no_input.index.values


# Vertices - vertices with no incoming routes
vertices_rest = vertices[~vertices.IATA.isin(no_input.IATA)]
airports_i['DstIDX'] = vertices_rest.index

# Page Rank evaluation:
n = len(vertices)

# Time for computing the Page Rank Algorithm
start_time = time.time()

# Page Rank Computation
pr = page_rank(n, airports_i, deadEnds_idx, no_input_idx)
print("--- %s seconds ---" % (time.time() - start_time))
# print(sum(pr)) # Uncomment for gettign the total sum of P

# Output Management
x = names_Airports.AirportName.tolist()
idx_res = np.arange(n)
result = ps.DataFrame({'Airport_Rank': pr.tolist(), 'Airport_Name': x})
result = result.sort_values(by='Airport_Rank', axis=0, ascending=0 )

# Final result
result = result.set_index(idx_res)
#print(airports_i)


# IF you want to get your results in a csv uncomment the below line.
#result.to_csv("Results_85.csv", sep=',')

print(result)





