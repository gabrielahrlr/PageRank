__author__ = 'Gabriela'

__author__ = 'Gabriela'
import numpy as np


def pageRank(vertices, edges):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    l= 0.85
    q = np.zeros(n)
    x = True
    while (ite <2):
        sum_com = dead_ends(vertices, edges, p)
        for index, row in vertices.iterrows():
            node = row.IATA
            #print(node)
            mask = (edges['DstIATA'] == node)
            orgAirports = edges[mask].OrgIATA.values
            sum_default = sum_com
            if orgAirports.any():
                #idx_codes = vertices.index[[x in orgAirports for x in vertices.IATA]].values
                mask = (vertices['IATA'].isin(orgAirports))
                idx_codes = vertices.index[mask].values
                mask = (edges.DstIATA == node)
                w_ji = edges.Weight[mask].values
                p1 = p[idx_codes]
                suma = p1*w_ji
                mask = (edges['OrgIATA'].isin(orgAirports))
                out_j = edges[mask]
                out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
                suma = sum(suma/out_j)
                suma = suma + sum_default
                q[index] = l * suma + ((1-l)/n)
            else:
               # print('---YES---')
               # print(node)
                q[index] = l* sum_default + ((1-l)/n)
        #if np.array_equal(p,q):
         #   break
          #  x = False
        #else:
        p = q
        ite +=1
    return p


def dead_ends(vertices, edges, p):
    idx_de = vertices['IATA'].isin(edges.OrgIATA)
    dead_ends = vertices[~idx_de]
    dead_ends = dead_ends.IATA.values
    mask = (vertices['IATA'].isin(dead_ends))
    idx_code = vertices.index[mask].values
    p2 = p[idx_code]
    add = p2/5742
    add = sum(add)
    print(add)
    return add



