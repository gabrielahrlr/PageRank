import numpy as np
__author__ = 'Gabriela'


def page_rank(vertices, vertices_rest, airports_i, out_j, deadEnds_idx, no_input_idx ):
    ite = 0
    n = len(vertices)
    p = np.ones(n)/n
    l = 0.85
    comp = (1-l)/n
    #x = True
    while ite < 50:
        print(ite)
        q = np.zeros(n)
        p2 = p[deadEnds_idx]
        add = p2/n
        sum_de = sum(add)
        default = (l * sum_de) + comp
        q[no_input_idx] = default
        for index, row in vertices_rest.iterrows():
            node = row.IATA
            pointed_by = airports_i.OrgIATA[airports_i.DstIATA == node].values[0]
            w_ji = airports_i.Weight[airports_i.DstIATA == node].values[0]
            outs = out_j.Out_j[out_j.OrgIATA.isin(pointed_by)].values
            idx_j = vertices.index[vertices.IATA.isin(pointed_by)].values
            p_j = p[idx_j]
            sum_ji = p_j*w_ji
            sum_ji = sum_ji/outs
            sum_ji = sum(sum_ji) + sum_de
            q[index] = (l * sum_ji) + comp

#            else:
#                q[index] = default
        if np.array_equal(p, q):
            break
        else:
            p = q
            ite += 1
    return p


# def dead_ends(vertices, edges, p, n):
#     idx_de = vertices.IATA.isin(edges.OrgIATA)
#     dead_ends = vertices[~idx_de]
#     dead_ends = dead_ends.IATA.values
#     mask = (vertices.IATA.isin(dead_ends))
#     idx_code = vertices.index[mask].values
#     p2 = p[idx_code]
#     add = p2/n
#     add = sum(add)
#     return add


# def alone_nodes(vertices, edges):
#     #mask1 = vertices.IATA.isin(edges.OrgIATA)
#     mask2 = vertices.IATA.isin(edges.DstIATA)
#     #notINO =  vertices[~mask1]
#     notinD = vertices[~mask2]
#     prun = vertices[vertices.IATA.isin(notinD.IATA)]
#     #print(prun)
#     return prun