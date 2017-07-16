#!/usr/bin/env python
import time
import timeit
import random,sys
from mQueue import Queue
import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread
import os
import math

#                           GLOBAL VARS
Q = []
Qmax = []
GLENGTH = 20
#                           END VARS

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#                           GRAPHS

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
G = [
[1,3],
[2,3,4,5],
[4],
[0,1,5],
[1,2,5],
[1,3,4],
]
# - - - - - - - - - - - - - - - - - - - -
#                                      END GRAPHS


def showGraph():
    global G
    TMP = G
    labeldict = {}
    K = nx.Graph()
    while 1:
        Kdict = []
        # Drawning the Graph
        H = nx.Graph()
        H.add_nodes_from([0,len(TMP)])
        H.nodes(data=True)
        for i in range(0,len(TMP)):
            for j in TMP[i]:
                # My label to name the nodes
                labeldict[i] = i
                # Adding edges
                H.add_edge(i,j)
                # Condition to change colors
                if i in Qmax and j in Qmax:
                    H[i][j]['good']=True
                else:
                    H[i][j]['good']=False


        Kdict = [ 'r' for i in range(0,len(H.edges()))]
        edges = H.edges(data=True)
        for (u, v, good) in edges:
            if good['good']:
                Kdict[u]='b'
        # drawing
        # pos = nx.spring_layout(Qmax)
        try:
            nx.draw_circular(H,labels=labeldict, with_labels = True,edge_color=tuple(Kdict))
            plt.savefig("/tmp/g.png")
        except:
            pass

        # Showing image
        os.system("eog /tmp/g.png &")
        # nx.drawing.nx_agraph.write_dot(H,"fig.dot")
        time.sleep(0.2)

        # plt.ion()
        # plt.show()
        # plt.pause(0.2)

        # Clearing plt
        # plt.close()
        plt.clf()



#                                      BEGIN LOG
def logging(TMP):
    log = open("/tmp/logging.txt","w")
    log.write("[LENGTH]-> (%d)\n" % len(TMP))
    log.write("[Maximal Clique]-> %s  \n" % (str(Qmax)))
    for i in range(0,len(TMP)):
        log.write("[%d] -> %s\n" % (i,str(TMP[i])))
    log.close()

#                                    END LOG

#                                   BEGIN MC
def expand(R,G):
    global Q
    global Qmax

    Rp = []
    while len(R) != 0:
        p = R[0]
        if (len(Q) + len(R)) > len(Qmax):
            Q.append(p)
            for y in G[p]:
                if y in R:
                    Rp.append(y)
            if len(Rp) != 0:
                expand(Rp,G)
            else:
                if len(Q) > len(Qmax):
                    Qmax = Q

            Q = []
        R.remove(p)

def basicMC(G):
    V = [ i for i in range(0,len(G)) ]
    TMP = G
    expand(V,TMP)
    logging(TMP)
    return Qmax
#                                       END MC

#                                       BEGIN PRUNING
def pruning():
    global G
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
#                                       END PRUNING

#                               BEGIN RANDOMIC CHANGES

# TODO: Implement this
def random_setWeight(u,v,w):
    pass

def random_edges():
    global G
    while 1:
        v = random.randint(0,len(G)-1)
        u = random.randint(0,len(G)-1)
        rand = random.randint(0,2)
        if rand == 1:
            if v!=u and v not in G[u]:
                G[u].append(v)
                #print "[+] Edge %d-%d added!" % (u,v)
            else:
                if v!=u and v in G[u]:
                    G[u].remove(v)
                    #print "[-] Edge %d-%d deleted!" % (u,v)

        time.sleep(random.random())

def random_vertices():
    global G
    while 1:
        if len(G) < GLENGTH:
            rand = random.randint(0,2)
            if  rand == 1:
                G.append([random.randint(0,len(G)-1)])
                #print "[*] Vertice %d added" % len(G)
            else:
                v = random.randint(0,len(G)-1)
                G[v] = []
                #print "[!] Vertice %d deleted!" % (v)
            time.sleep(random.random())
#                               END RANDOMIC CHANGES

#                           STARTING THINGS


# TMP Holds a snapshot of G
TMP = []

t = Thread(None,random_edges)
t.start()
v = Thread(None,random_vertices)
v.start()
# Unconmment this to see the Graph
# s = Thread(None,showGraph)
# s.start()
#                           END THINGS

PRUNING = False
# Using PRUNING?
if len(sys.argv) >1:
    PRUNING = True
    print "\t\tUsing PRUNING approach\n\n"
else:
    print "\t\tRunning without PRUNING approach\n"
    print "python2.7 %s <1> - enable PRUNING\n\n" % (sys.argv[0])

# Enable time tracing
f =  "/tmp/pruning.txt" if PRUNING else "/tmp/noPruning.txt"

while 1:
    fp = open(f,'a+')
    start_time = timeit.default_timer()
    if PRUNING:
        G = pruning()
    Qmax = []
    # Calculates execution time
    print "[*] New Maximal clique is ", basicMC(G)
    elapsed = timeit.default_timer() - start_time
    # Tracing
    fp.write(str(elapsed)+'\n')
    fp.close()
    time.sleep(2)
