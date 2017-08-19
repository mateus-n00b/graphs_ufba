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

    def SetPosition(self):
        while 1:
            for i in range(0,self.MAX_NODES):
                # Move!!!
                # Return the coordinates of nodes
                positions = next(self.mobility_model)
                self.POS = positions

                for j in range(0,self.MAX_NODES):
                    # Vertices positions
                    u = (positions[i][0],positions[i][1])
                    v = (positions[j][0],positions[j][1])
                    distUV = distance.euclidean(u,v)

                    if (distUV <= self.MAX_RANGE) and (j not in self.G[i])\
                    and (i not in self.G[j]) and (i!=j): # Is in my coverage area? If yes, then is my neighbour!
                                # Builds the Graph adj. list
                                self.G[i].append(j)
                                self.G[j].append(i)

                                # Builds the Graph Weight list
                                if not self.W.has_key(i):
                                        self.W[i] = {}
                                if not self.W.has_key(j):
                                        self.W[j] = {}

                                self.W[i][j] = distUV
                                self.W[j][i] = distUV
                                self._LOG_("Edge (%d <- %f -> %d) added!" %(i,distUV,j))

            time.sleep(0.3)

    # Are all neighbours still in the neighbourhood?
    def Management(self):
        while 1:
            pos = self.POS
            if len(pos) > 0:
                for u in range(0,len(self.G)):
                    for v in self.G[u]:
                        x = (pos[u][0],pos[u][1])
                        y = (pos[v][0],pos[v][1])
                        distUV = distance.euclidean(x,y)
                        if distUV > self.MAX_RANGE: # Is out of my coverage range?
                                self.G[u].remove(v)
                                self.G[v].remove(u)
                                self.W[u].__delitem__(v)
                                self.W[v].__delitem__(u)
                                self._LOG_("Edge (%d <- %f -> %d) is down!" %(u,distUV,v))
            time.sleep(0.1)

    def SendPacket(self,s,ttl,MST):
        temp = [(int(i),int(j)) for w,i,j in MST ]
        if ttl <= 0:
            self._LOG_("Packet dropped on %d" % s)
        else:
            ttl-=1
            for u in self.G[s]:
                if (s,u) not in temp:
                    self.SendPacket(u,ttl,MST)
                else:
                    self._LOG_("Packet received by %d" % s)
                    break


    # May be useful
    def BFS(self,s):
        level = {s:0}
        parent = {s:None}
        i=1
        frontier =[s]
        while frontier:
            nxt = []
            for u in frontier:
                for v in self.G[u]:
                    if v not in level:
                        level[v]=i
                        parent[v] = u
                        nxt.append(v)
            frontier = nxt
            i+=1
        return level

    def Run(self):
        self.verbose = raw_input("Verbose y/n? ") # Verbose?

        # TODO: How to kill these threads?
        p = Thread(group=None,target=self.SetPosition)
        p.start()

        t = Thread(group=None,target=self.Management)
        t.start()
