import random
# Creates a graph
#
# in: Number of vertices
# output: An adjacency list
#

def graph_creator(nv):
    '''Graph generator by n00b'''
    G = []
    for v in range(0,nv):
        G.append([])
        e = random.randint(0,nv)
        for j in range(0,e):
            edge = random.randint(0,e)
            if edge not in G[v] and edge != v:
                G[v].append(edge)
            else:
                j-=1
    return G
