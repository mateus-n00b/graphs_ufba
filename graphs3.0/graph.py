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
        self.G = G # Adj. list
        self.W = W # Weight list
        self.mobility_model = mobility_model # mobility_model
        self.MAX_NODES = MAX_NODES # number of nodes
        self.MAX_RANGE = MAX_RANGE # max transmition range
        self.POS = [] # holds the current position of every node
        self.verbose = None # for print infos

    def _LOG_(self, msg):
        if "y" in self.verbose.lower():
            print "[LOG] {0}".format(msg)

    def SetPosition(self,G,W,mobility_model,MAX_NODES,MAX_RANGE):
        while 1:
            for i in range(0,MAX_NODES):
                # Move!!!
                # Return the coordinates of nodes
                positions = next(mobility_model)
                self.POS = positions

                for j in range(i+1,MAX_NODES):
                    # Vertices positions
                    u = (positions[i][0],positions[i][1])
                    v = (positions[j][0],positions[j][1])

                    distUV = distance.euclidean(u,v)
                    if (distUV <= MAX_RANGE) and (j not in G[i]) and (i not in G[j]): # Is in my coverage area? If yes, then is my neighbour!
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
                        self._LOG_("Edge (%d <- %f -> %d) added!" %(i,distUV,j))
    # Are all neighbours still in the neighbourhood?
    def Management(self):
        while 1:
            H = self.G
            pos = self.POS
            if len(pos) > 0:
                for u in range(0,len(H)):
                    for v in H[u]:
                        x = (pos[u][0],pos[u][1])
                        y = (pos[v][0],pos[v][1])
                        distUV = distance.euclidean(x,y)
                        if distUV > self.MAX_RANGE: # Is out of my coverage range?
                            self.G[u].remove(v)
                            self.G[v].remove(u)
                            self.W[u].__delitem__(v)
                            self.W[v].__delitem__(u)
                            self._LOG_("Edge (%d <- %f -> %d) is down!" %(u,distUV,v))

            time.sleep(0.5)

    def Run(self):
        self.verbose = raw_input("Verbose y/n? ") # Verbose?

        # TODO: How to kill these threads?
        p = Thread(group=None,target=self.SetPosition,
        args=(self.G,self.W,self.mobility_model,self.MAX_NODES, self.MAX_RANGE))
        p.start()

        t = Thread(group=None,target=self.Management)
        t.start()
