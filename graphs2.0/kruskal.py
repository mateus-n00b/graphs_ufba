# Copied from some link on github (put here later)
#
# I modified some part (run function)
#
# Mateus-n00b, July 2017
#
#
import pruning
from log import *

parent = dict()

def make_set(vertice):
    parent[vertice] = vertice


# returns first element of set, which includes 'vertice'
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]


# joins two sets: set, which includes 'vertice1' and set, which
# includes 'vertice2'
def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    # print ancestor1,ancestor2

    # if u and v are not connected by a path
    if ancestor1 != ancestor2:
        # Not necessary
        # for edge in edges:
            parent[ancestor1] = ancestor2


def kruskal(G,W):
    graph = run(G,W)
    mst = set()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    # In my case, the list will be sorted in descending order (edges.reverse)
    # logging_kruskal(G,weight)
    logging(G,[])

    for edge in edges:
        weight, u, v = edge
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)
        else:
            pass

    return mst

def run(G,weight):
    graph = {}
    conj = set()
    graph['V'] = [str(i) for i in range(0,len(G))]
    for i in range(0,len(G)):
        for j in G[i]:
            conj.add((weight[i][j],str(i),str(j)))
    graph['E'] = conj
    return graph

# input graph
# Testbed
#
# G = [
# [1],
# [2,6,7],
# [7,3,8],
# [8,4],
# [],
# [6],
# [7],
# [8],
# [9],
# []
# ]

# # Uncomment this to test the alg.
# W = {0: {1: 10.0}, 1: {2: 10.0, 6: 8.0, 7: 13.0},
# 2: {8: 13.0, 3: 10.0, 7: 8.0}, 3: {8: 8.0, 4: 10.0},
# 4: {}, 5: {6: 10.0}, 6: {7: 10.0}, 7: {8: 10.0},
# 8: {9: 10.0}, 9: {}}
# print kruskal(G,W)


# Do not uncomment this part, it just read the weights
# for i in range(0,len(G)):
#     W[i] = {}
#     for j in G[i]:
#         W[i][j] = float(raw_input("(%d,%d)> " % (i,j) ))
# The output must contain: (0,1), (1,2), (1,6),(2,3),(2,7), (3,4),(3,8), (5,6), (8,9)
