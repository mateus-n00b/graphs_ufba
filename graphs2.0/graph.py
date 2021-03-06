import time
import timeit
import random,sys
from threading import Thread

# Set a seed to be 'equals' to all executions
random.seed(a=1000)

class Graph(object):
    def __init__(self,G,GLENGTH,W):
        self.GLENGTH = GLENGTH
        self.G = G
        self.W = W
    # Use esta funcao, juntamente com a fixGraph, para preencher a lista de adjacencia corretamente.
    # Errei na construcao da lista de adjacencia pois estava criando um grafo orientado :/ onde o ultimo no.
    # estava em um beco sem saida.
    def fixW(self):
        for i in range(0,len(self.G)):
            for j in self.G[i]:
                if not self.W[i].has_key(j):
                    self.W[i][j] = self.W[j][i]

    # NOTE: I have been using a Directed Graph.
    # Use this function to fix it.
    def fixGraph(self):
        for i in range(0,len(self.G)):
            for j in self.G[i]:
                if i not in self.G[j]:
                    self.G[j].append(i)
        self.fixW()

    # Adds random Weights to the edges
    def random_setWeight(self,u,v):
        w = int(random.uniform(0.1,100))
        if not self.W.has_key(u):
            self.W[u] = {}

        if not self.W.has_key(v):
            self.W[v] = {}

        self.W[u][v] = w
        self.W[v][u] = w
        print "[WEIGHT] Weight added to (%d-%d)" % (u,v)

    # Adds edges in a random way
    def random_edges(self):
        while 1:
            v = random.randint(0,len(self.G)-1)
            u = random.randint(0,len(self.G)-1)
            rand = random.randint(0,4)
            # De acordo com Iury
            if rand == 1 or rand == 3:
                if (v!=u) and (v not in self.G[u]) and (u not in self.G[v]):
                    self.G[u].append(v)
                    self.G[v].append(u)
                    self.random_setWeight(u,v)
                    print "[ADDITION-EDGE] Edge %d-%d added!" % (u,v)

            elif rand == 2:
                if v!=u and v in self.G[u] and u in self.G[v]:
                    self.G[u].remove(v)
                    self.G[v].remove(u)
                    self.W[u].__delitem__(v)
                    self.W[v].__delitem__(u)
                    print "[DELETION-EDGE] Edge %d-%d deleted!" % (u,v)
            time.sleep(random.random())

    def random_vertices(self):
        while 1:
            if len(self.G) < self.GLENGTH:
                rand = random.randint(0,4)
                if  rand == 1:
                    self.G.append([])
                    # Add new entry for the new node
                    self.W[len(self.G)] = {}
                    print "[ADDITION-VERTICE] Vertice [%d] added" % len(self.G)

                elif rand == 2:
                    v = random.randint(0,len(self.G)-1)
                    # To delete every connection with 'v'
                    for e in self.G[v]:
                        if self.W[e].has_key(v):
                            self.W[e].__delitem__(v)

                    self.W[v] = {}
                    self.G[v] = []
                    print "[DELETION-VERTICE] Vertice [%d] deleted!" % (v)

                time.sleep(random.random())

    def run(self):
        v = Thread(None,self.random_vertices,None)
        v.start()

        t = Thread(None,self.random_edges,None)
        t.start()
