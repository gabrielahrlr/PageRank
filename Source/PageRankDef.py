import numpy as np
__author__ = 'Gabriela'

#This function computes the Page Rank Algorithm

def page_rank(n, airports_i, deadEnds_idx, no_input_idx ):
    ite = 0
    n = n
    p = np.ones(n)/n
    l = 0.85
    comp = (1-l)/n
    while ite < 100:
        print(ite)
        q = np.zeros(n)
        p2 = p[deadEnds_idx]
        add = p2/n
        sum_de = sum(add)
        default = (l * sum_de) + comp
        q[no_input_idx] = default
        for index, row in airports_i.iterrows():
            w_ji = row.Weight
            out_j = row.Out_j
            p_j = p[row.OrgIATA]
            sum_ji = p_j*w_ji
            sum_ji = sum_ji/out_j
            sum_ji = sum(sum_ji) + sum_de
            q[row.DstIDX] = (l * sum_ji) + comp
        if np.allclose(p, q, rtol=1e-4, atol=1e-4):
            break
        else:
            p = q
            ite += 1
    return p


