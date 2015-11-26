import numpy as np

__author__ = 'Gabriela'


def page_rank(vertices, edges):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    l = 0.85
    comp = (1-l)/n

    while ite < 4:
        q = np.zeros(n)
        sum_de = dead_ends(vertices, edges, p, n)
        for index, row in vertices.iterrows():
            node = row.IATA
            pointed_by = edges.OrgIATA[edges.DstIATA == node].values
            if pointed_by.any():
                filtering = vertices[vertices.IATA.isin(pointed_by)]
                idx_j = filtering.index.values
                g = edges[(edges.OrgIATA.isin(pointed_by)) & (edges.DstIATA == node)]
                w_ji = g.Weight.values
                mask = (edges['OrgIATA'].isin(pointed_by))
                out_j = edges[mask]
                out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
                p_j = p[idx_j]
                sum_ji = p_j*w_ji
                sum_ji = sum_ji/out_j
                sum_ji = sum(sum_ji) + sum_de
                p_new = (l * sum_ji) + comp
                q[index] = p_new

            else:
                q[index] = (l * sum_de) + comp
        p = q
        ite += 1
    return p


def dead_ends(vertices, edges, p, n):
    idx_de = vertices['IATA'].isin(edges.OrgIATA)
    dead_ends = vertices[~idx_de]
    dead_ends = dead_ends.IATA.values
    mask = (vertices['IATA'].isin(dead_ends))
    idx_code = vertices.index[mask].values
    p2 = p[idx_code]
    add = p2/n
    add = sum(add)
    return add
