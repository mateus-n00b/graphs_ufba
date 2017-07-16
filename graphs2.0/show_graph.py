import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread
import os

class Show(object):
    def __init__(self,G):
        self.G = G

    def showGraph():
        TMP = self.G
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

    def run(self):
         t = Thread(None,self.showGraph,None)
         t.start()
