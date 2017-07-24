import math
#                                       BEGIN prunning
def prunning(G):
    TMP = G
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
