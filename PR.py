import numpy as np
__author__ = 'Gabriela'


def page_rank(vertices, edges, ae, rest):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    l = 0.85
    comp = (1-l)/n
    while ite < 3:
        q = np.zeros(n)
        sum_de = dead_ends(vertices, edges, p, n)
        default = (l * sum_de) + comp
        ae_idx = ae.index.values
        q[ae_idx] = default
        for index, row in rest.iterrows():
            node = row.IATA
            pointed_by = edges.OrgIATA[edges.DstIATA == node].values
#            if pointed_by.any():
            idx_j = vertices.index[vertices.IATA.isin(pointed_by)].values
            w_ji = edges.Weight[(edges.OrgIATA.isin(pointed_by)) & (edges.DstIATA == node)].values
            mask = (edges['OrgIATA'].isin(pointed_by))
            out_j = edges[mask]
            out_j = out_j.groupby(['OrgIATA']).Weight.sum().values
            p_j = p[idx_j]
            sum_ji = p_j*w_ji
            sum_ji = sum_ji/out_j
            sum_ji = sum(sum_ji) + sum_de
            q[index] = (l * sum_ji) + comp

#            else:
#                q[index] = default
        p = q
        ite += 1
    return p


def dead_ends(vertices, edges, p, n):
    idx_de = vertices.IATA.isin(edges.OrgIATA)
    dead_ends = vertices[~idx_de]
    dead_ends = dead_ends.IATA.values
    mask = (vertices.IATA.isin(dead_ends))
    idx_code = vertices.index[mask].values
    p2 = p[idx_code]
    add = p2/n
    add = sum(add)
    return add


# def alone_nodes(vertices, edges):
#     #mask1 = vertices.IATA.isin(edges.OrgIATA)
#     mask2 = vertices.IATA.isin(edges.DstIATA)
#     #notINO =  vertices[~mask1]
#     notinD = vertices[~mask2]
#     prun = vertices[vertices.IATA.isin(notinD.IATA)]
#     #print(prun)
#     return prun