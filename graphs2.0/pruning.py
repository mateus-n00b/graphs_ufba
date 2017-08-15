import math
#                                       BEGIN prunning
def edge_pruning(G,W):
    TMP = list(G)
    Wtemp = dict(W)
    medium_weigth = 0.0
    cont = 1.0
    for u in range(0,len(TMP)):
        for v in TMP[u]:
            if Wtemp[u].has_key(v):
                # total of edges
                cont+=1.0
                # average weigth of the edges
                medium_weigth += Wtemp[u][v]

    medium_weigth/=cont
    if medium_weigth > 1.0:
        for u in range(0,len(TMP)):
            for v in TMP[u]:
                if Wtemp[u].has_key(v) and Wtemp[u][v] < medium_weigth:
                    if Wtemp[u].has_key(v):
                        Wtemp[u].__delitem__(v)
                    if Wtemp[v].has_key(u):
                        Wtemp[v].__delitem__(u)
                    # NOTE: I fix this line because I found a error on it
                    # I've been just removing the Weights and not the edges
                    if v in TMP[u]:
                        TMP[u].remove(v)
                    if u in TMP[v]:
                        TMP[v].remove(u)
                    # print "Edge (%d,%d) removed!" % (u,v)
    return TMP,Wtemp


def pruning(G,W):
    TMP = list(G)
    Wtemp = dict(W)
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
                # Remove Vertice to relax the calc
                for e in TMP[i]:
                    if Wtemp[e].has_key(i):
                        Wtemp[e].__delitem__(i)
                        TMP[e].remove(i)
                Wtemp[i] = {}
                TMP[i] = []

    return TMP,Wtemp
#                                       END prunning
