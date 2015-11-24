__author__ = 'Gabriela'
import numpy as np


def pageRank(vertices, edges):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    #print(p)
    #print('first P', sum(p))
    l= 0.85
    while(ite < 1):
        q = np.zeros(n)
        sum_com = dead_ends(vertices, edges, p)
        for i in np.arange(len(q)):
            node = vertices.loc[vertices.index[i]].IATA
            orgAirports = edges.loc[edges.DstIATA == node].OrgIATA.values
            sum_default = sum_com
            if orgAirports.any():
                idx_codes = vertices.index[vertices['IATA'].isin(orgAirports)].values
                w_ji = edges.Weight[(edges['OrgIATA'].isin(orgAirports)) & (edges.DstIATA == node)].values
                p1 = p[idx_codes]
                suma = p1*w_ji
                out_j = edges[edges['OrgIATA'].isin(orgAirports)]
                out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
                suma = sum(suma/out_j)
                suma = suma + sum_default
                q[i] = l * suma + ((1-l)/n)
            else:
                q[i] = sum_default + ((1-l)/n)

        p = q
        ite += 1
    return p


def dead_ends(vertices, edges, p):
    idx_de = vertices['IATA'].isin(edges.OrgIATA)
    dead_ends = vertices[~idx_de]
    dead_ends = dead_ends.IATA.values
    sum = 0
    idx_code = vertices.index[vertices['IATA'].isin(dead_ends)].values
    p2 = p[idx_code]
    add = p2/5742
    add = add.sum()
    print(add)
    return add

