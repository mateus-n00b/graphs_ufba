# Algorithms and Graphs 2017.1
# Final Test
# Mateus Sousa, 2017 (UFBA)
#
# License GPLv3
#
#
#
from scipy.spatial import distance
from threading import Thread
import time

class Graph(object):
    def __init__(self,G,W,mobility_model,MAX_NODES,MAX_RANGE):
        self.G = G
        self.W = W
        self.mobility_model = mobility_model
        self.MAX_NODES = MAX_NODES
        self.MAX_RANGE = MAX_RANGE
        self.POS = []

    def SetPosition(self,G,W,mobility_model,MAX_NODES,MAX_RANGE):
        while 1:
            for i in range(0,MAX_NODES):
                # Move!!!
                # Return the coordinates of nodes
                positions = next(mobility_model)

                for j in range(i+1,MAX_NODES):
                    # Vertices positions
                    u = (positions[i][0],positions[i][1])
                    v = (positions[j][0],positions[j][1])

                    distUV = distance.euclidean(u,v)
                    if distUV <= MAX_RANGE: # Is in my coverage area? If yes, then is my neighbour!
                        # Builds the Graph adj. list
                        G[i].append(j)
                        G[j].append(i)

                        # Builds the Graph Weight list
                        if not W.has_key(i):
                            W[i] = {}
                        if not W.has_key(j):
                            W[j] = {}

                        W[i][j] = distUV
                        W[j][i] = distUV
    # Are all neighbours still in the neighbourhood?
    def Management(self):
        H = self.G
        pos = self.POS
        while 1:
            for u in range(0,H):
                for v in H[u]:
                    x = (pos[u][0],pos[u][1])
                    y = (pos[v][0],pos[v][1])
                    distUV = distance.euclidean(x,y)
                    if distUV > self.MAX_RANGE: # Is out of my coverage range?
                        G[u].remove(v)
                        G[v].remove(u)
                        W[u].__delitem__(v)
                        W[v].__delitem__(u)
                        print "[INFO] Link (u,v) is down!"
            time.sleep(0.5)


    def Run(self):
        self.SetPosition(self.G,self.W,self.mobility_model,self.MAX_NODES, self.MAX_RANGE)
        t = Thread(group=None,target=self.Management,args=())
        t.start()
