import time
import timeit
import random,sys
from threading import Thread

class Graph(object):
    def __init__(self,G,GLENGTH,W):
        self.GLENGTH = GLENGTH
        self.G = G
        self.W = W

    # Adds random Weights to the edges
    def random_setWeight(self,u,v):
        w = random.random()*10
        if not self.W.has_key(u):
            self.W[u] = {}
            self.W[u][v] = w
        else:
            self.W[u][v] = w

        print "[++] Weight added to (%d-%d)" % (u,v)

    # Adds edges in a random way
    def random_edges(self):
        while 1:
            v = random.randint(0,len(self.G)-1)
            u = random.randint(0,len(self.G)-1)
            rand = random.randint(0,4)
            if rand == 1:
                if v!=u and v not in self.G[u]:
                    self.G[u].append(v)
                    self.random_setWeight(u,v)
                    print "[+] Edge %d-%d added!" % (u,v)
            elif rand == 2:
                if v!=u and v in self.G[u]:
                    self.G[u].remove(v)
                    # self.W[u].__delitem__(v)
                    print "[-] Edge %d-%d deleted!" % (u,v)

            time.sleep(random.random())

    def random_vertices(self):
        while 1:
            if len(self.G) < self.GLENGTH:
                rand = random.randint(0,4)
                if  rand == 1:
                    self.G.append([random.randint(0,len(self.G)-1)])
                    print "[*] Vertice %d added" % len(self.G)
                elif rand == 2:
                    v = random.randint(0,len(self.G)-1)
                    self.G[v] = []
                    print "[!] Vertice %d deleted!" % (v)
                time.sleep(random.random())

    def run(self):
        v = Thread(None,self.random_vertices,None)
        v.start()

        t = Thread(None,self.random_edges,None)
        t.start()
