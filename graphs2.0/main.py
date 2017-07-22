#!/usr/bin/env python
# This program try to find the maximal-clique in a dynamic graph
# by using a prunning approach.
#
# Authors:
#          Mateus Sousa (UFBA)
#          Iury Maia    (UFBA)
#
# Version 2.0
# Now it is modular
# License GPLv3+
# TODO: Comment the code

import time,os
import timeit
import random,sys

# My imports
import kruskal
import maximal
import graph
import prunning
import show_graph

#                           GLOBAL VARS
Q = []
Qmax = []
GLENGTH = 75
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


# Using prunning?
PRUNNING = False
if len(sys.argv) > 1:
    PRUNNING = True
    print "\tUsing prunning approach\n"
else:
    print "\tRunning without prunning approach\n"
    print "python2.7 {0} <1> - enable prunning\n".format(sys.argv[0])

# Enable time tracing
f =  "/tmp/prunning.txt" if PRUNNING  else "/tmp/noprunning.txt"
cont = 0
while cont < 1000:
    # See: https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list, for explanations
    # about this line.
    TMP = []
    Wb = {}
    TMP = list(G)
    Wb = dict(W)
    # Write logs about exec time
    fp = open(f,'a+')

    if PRUNNING:
        TMP = prunning.prunning(TMP)

    Qmax = []
    start_time = timeit.default_timer()
    # #print "[*] New Maximal clique is ", mc.basicMC(TMP,Qmax)
    print "[*] New Maximal Spanning Tree >", kruskal.kruskal(TMP,Wb)
    # Calculates execution time
    elapsed = timeit.default_timer() - start_time

    # Tracing
    fp.write(str(elapsed)+'\n')
    fp.close()

    cont +=1
    TMP = []
    time.sleep(0.2)
os.system("killall python")
