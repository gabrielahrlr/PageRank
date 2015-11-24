__author__ = 'Gabriela'
import numpy as np


def pageRank(vertices, edges):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    l= 0.85
    while(ite < 1):
        q = np.zeros(n)
        sum_com = dead_ends(vertices, edges, p)
        for i in np.arange(len(q)):
            node = vertices.loc[vertices.index[i]].IATA
            orgAirports = edges.loc[edges.DstIATA == node].OrgIATA.values
            sum = sum_com
            if orgAirports != []:
                for code in orgAirports:
                    idx_code = vertices.index[vertices.IATA == code].values[0]
                    w_ij = edges.loc[(edges.OrgIATA == code) & (edges.DstIATA == node)].Weight.values[0]
                    out_j = edges.loc[edges.OrgIATA == code].Weight.sum()
                    sum += (p[idx_code] * w_ij/out_j)
                q[i] = l * sum + ((1-l)/n)
            else:
                q[i] = sum + ((1-l)/n)
        if np.allclose(p, q):
            break
        else:
            p = q
            ite += 1
    return p


def dead_ends(vertices, edges, p):
    idx_de = vertices['IATA'].isin(edges.OrgIATA)
    dead_ends = vertices[~idx_de]
    dead_ends = dead_ends.IATA.values
    sum = 0
    for code in dead_ends:
        idx_code = vertices.index[vertices.IATA == code].values[0]
        sum += p[idx_code]/5742
    print(sum)
    return sum

