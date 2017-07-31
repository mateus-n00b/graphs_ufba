import math
#                                       BEGIN prunning
def edge_prunning(G,W):
    TMP = list(G)
    medium_weigth = 0.0
    cont = 0.0

    for u in range(0,len(TMP)):
        for v in G[u]:
            # total of edges
            cont+=1.0
            # average weigth of the edges
            medium_weigth += W[u][v]

    medium_weigth/=cont
    if medium_weigth > 1.0:
        for u in range(0,len(TMP)):
            for v in G[u]:
                if W[u][v] < medium_weigth:
                    TMP[u].remove(v)
                    # print "Edge (%d,%d) removed!" % (u,v)
    return TMP


def prunning(G):
    TMP = list(G)
    # Holds the average degree of all nodes
    medium_degree = 0.0
    # Number of vertices
    vertices = float(len(TMP))
    for i in range(0,len(TMP)):
        medium_degree+=len(TMP[i])

    medium_degree/=vertices
    medium_degree = math.ceil(medium_degree)

    # If degree greater than 1
    if medium_degree > 1.0:
        for i in range(0,len(TMP)):
            # If degree of node i is less than medium_degree
            if len(TMP[i]) < medium_degree:
                # Remove Vertice to easy the Maximal-Clique computation
                TMP[i] = []
    return TMP
#                                       END prunning
