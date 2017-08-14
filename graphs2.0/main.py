#!/usr/bin/env python
# This program try to find the maximal-clique in a dynamic graph
# by using a pruning approach and a MST as well.
#
# Authors:
#          Mateus Sousa (UFBA)
#          Iury Maia    (UFBA)
#
# Version 2.0
# Now it is modular
# License GPLv3+
# TODO: Comment the code
# ////////////////////////////////////////////////////////////////////////////////////////////////////

import time,os
import timeit
import random,sys

# My imports
import naive_kruskal
import my_kruskal
import maximal
import graph
import pruning
import show_graph

#                           GLOBAL VARS
Q = []
Qmax = []
GLENGTH = 75
# Weights
W = {}
gl_algo = object
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

# Set initial Weights
for i in range(0,len(G)):
    W[i] = {}
    for j in G[i]:
        W[i][j] = random.randint(0,100)

# - - - - - - - - - - - - - - - - - - - -
#                                      END GRAPHS

#                                       Starting
H = graph.Graph(G,GLENGTH,W)
H.fixGraph()
print G
H.run()
mc = maximal.MC(Qmax)
show = show_graph.Show(G,Qmax)
# Uncomment this to see the graph
# show.run()


# Using pruning?
PRUNING = False
if len(sys.argv) > 1:
    PRUNING = True
    print "\tUsing pruning approach\n"
    gl_algo = naive_kruskal
else:
    print "\tRunning without pruning approach\n"
    print "python2.7 {0} <1> - enable pruning\n".format(sys.argv[0])
    gl_algo = my_kruskal

def main():
    global gl_algo
    global PRUNING

    # Enable time tracing
    f =  "/tmp/pruning.txt" if PRUNING  else "/tmp/nopruning.txt"
    # Write logs about exec time
    fp = open(f,'a+')

    for i in range(1000):
        # See: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list, for explanations
        # about this line.
        TMP = []
        Wb = {}
        TMP = list(G)
        Wb = dict(W)

        # pruning?
        if PRUNING:
            TMP = pruning.pruning(TMP)
            TMP = pruning.edge_pruning(TMP,Wb)

        Qmax = []      # To Calculate Max clique
        start_time = timeit.default_timer()
        # #print "[*] New Maximal clique is ", mc.basicMC(TMP,Qmax)
        print "[*] New Maximal Spanning Tree >", gl_algo.kruskal(TMP,Wb)
        # Calculates execution time
        elapsed = timeit.default_timer() - start_time

        # Tracing
        fp.write(str(elapsed)+'\n')

        TMP = []
        time.sleep(0.2)
    fp.close()
    os.system("killall python")


if __name__ == '__main__':
    main()
