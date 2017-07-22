#!/usr/bin/env python
# This program try to find the maximal-clique in a dynamic graph
# by using a pruning approach.
#
# Authors:
#          Mateus Sousa (UFBA)
#          Iury Maia    (UFBA)
#
# Version 2.0
# Now it is modular
# License GPLv3+
# TODO: Comment the code

import time
import timeit
import random,sys

# My imports
import kruskal
import maximal
import graph
import pruning
import show_graph

#                           GLOBAL VARS
Q = []
Qmax = []
GLENGTH = 25
# Weights
W = {}
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
H.run()
mc = maximal.MC(Qmax)
show = show_graph.Show(G,Qmax)
# Uncomment this to see the graph
# show.run()


# Using PRUNING?
PRUNING = False
if len(sys.argv) > 1:
    PRUNING = True
    print "\tUsing PRUNING approach\n"
else:
    print "\tRunning without PRUNING approach\n"
    print "python2.7 {0} <1> - enable PRUNING\n".format(sys.argv[0])

# Enable time tracing
f =  "/tmp/pruning.txt" if PRUNING else "/tmp/noPruning.txt"

while 1:
    # See: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list, for explanations
    # about this line.
    TMP = []
    Wb = {}
    TMP = list(G)
    Wb = dict(W)
    # Write logs about exec time
    fp = open(f,'a+')

    if PRUNING:
        TMP = pruning.pruning(TMP)

    Qmax = []
    start_time = timeit.default_timer()
    # #print "[*] New Maximal clique is ", mc.basicMC(TMP,Qmax)
    print "[*] New Maximal Spanning Tree >", kruskal.kruskal(TMP,Wb)
    # Calculates execution time
    elapsed = timeit.default_timer() - start_time

    # Tracing
    fp.write(str(elapsed)+'\n')
    fp.close()

    TMP = []
    time.sleep(2)
