#!/usr/bin/env python
import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread
import os,math
import mQueue

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

def pruning():
    global G
    TMP = G
    medium_degree = 0.0
    vertices = float(len(TMP))
    for i in range(0,len(TMP)):
        medium_degree+=len(TMP[i])

    medium_degree/=vertices
    medium_degree = math.ceil(medium_degree)

    if medium_degree > 1.0:
        for i in range(0,len(TMP)):
            if len(TMP[i]) < medium_degree:
                TMP[i] = []

    return TMP

#                                       BEGIN COMP

def compGraph(graph,H,source):
    queue = []
    bfsInfo = []
    distance = 0;
    # Checa o numero de vertices
    if len(graph) != len(H):
        return False

    for i in range(0,len(graph)):
        if len(graph[i]) != len(H[i]):
            return False

    for i in range(0,len(graph)):
        bfsInfo.append({'distance':None, 'predecessor':None})

    bfsInfo[source]['distance'] = distance
    queue = Queue()
    queue.enqueue(source)

    while queue.isEmpty():
        u = queue.dequeue()
        for i in range(0,len(graph[u])):
            v = graph[u][i]
            if graph[u][i] == H[u][i]:
                if bfsInfo[v]['distance'] == None and v != source :
                    queue.enqueue(v)
                    bfsInfo[v]['distance'] = bfsInfo[u]['distance']+1
                    bfsInfo[v]['predecessor'] = u
            else:
                return False

    return True

#                               END COMP


#                               BEGIN RANDOMIC CHANGES

# TODO: Implement this
def random_setWeight(u,v,W):
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
                print "[+] Edge %d-%d added!" % (u,v)
        elif rand == 2:
            time.sleep(random.random()*10)
        else:
            if v!=u and v in G[u]:
                G[u].remove(v)
                print "[-] Edge %d-%d deleted!" % (u,v)

        time.sleep(random.random())

def random_vertices():
    global G
    while 1:
        if len(G) < GLENGTH:
            rand = random.randint(0,2)
            if  rand == 1:
                G.append([random.randint(0,len(G)-1)])
                print "[*] Vertice %d added" % len(G)
        elif rand == 2:
            time.sleep(random.random()*10)
        else:
            v = random.randint(0,len(G)-1)
            G[v] = []
            print "[!] Vertice %d deleted!" % (v)
        time.sleep(random.randint(1,2))
#                               END RANDOMIC CHANGES

#                           STARTING THINGS
NG = basicMC(G)
TMP = []

t = Thread(None,random_edges)
t.start()
v = Thread(None,random_vertices)
v.start()
# s = Thread(None,showGraph)
# s.start()
#                           END THINGS

while 1:
    AUX = []
    FOO = []
    if not compGraph(G,TMP,0):
        print "[!] Graph has changed! Recalculating..."
        # NG = basicMC(G)
        Qmax = []
        print "[*] New Maximal clique is ", basicMC(G)
        NG = FOO
        AUX.append(G)
        TMP = AUX
    else:
        print "[!] Maximal Clique (NOT MODIFIED) => ",NG

    time.sleep(2)
