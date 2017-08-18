# Algorithms and Graphs 2017.1
# Final Test
# Mateus Sousa, 2017 (UFBA)
#
# License GPLv3
#
#
#
from scipy.spatial import distance

class Graph(object):
    def __init__(self,G,W,mobility_model,MAX_NODES,MAX_RANGE):
        self.G = G
        self.W = W
        self.mobility_model = mobility_model
        self.MAX_NODES = MAX_NODES
        self.MAX_RANGE = MAX_RANGE

    def SetPosition(self):
        for i in range(0,self.MAX_NODES):
            # Move!!!
            # Return the coordinates of nodes
            positions = next(mobility_model)

            for j in range(i+1,self.MAX_NODES):
                # Vertices positions
                u = (positions[i][0],positions[i][1])
                v = (positions[j][0],positions[j][1])

                distUV = distance.euclidean(u,v)
                if distUV <= self.MAX_RANGE: # Is in my coverage area? If yes, then is my neighbour!
                    # Builds the Graph adj. list
                    self.G[i].append(j)
                    self.G[j].append(i)

                    # Builds the Graph Weight list
                    if not W.has_key(i):
                        self.W[i] = {}
                    if not W.has_key(j):
                        self.W[j] = {}

                    self.W[i][j] = distUV
                    self.W[j][i] = distUV
