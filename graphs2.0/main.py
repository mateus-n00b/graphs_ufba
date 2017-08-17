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
PRUNING = False
gl_algo = object

# Weights
W = {}
#                           END VARS

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#                           GRAPHS

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
G = [
[1],
[0, 2, 6, 7],
[1, 3, 7, 8],
[2, 4, 8],
[3],
[6],
[5, 1, 7],
[6, 2, 1, 8],
[2, 7, 9, 3],
[8]
]

# Set initial Weights
W = {
0: {1: 10.0},
1: {0: 10.0, 2: 10.0, 6: 8.0, 7: 13.0},
2: {8: 13.0, 1: 10.0, 3: 10.0, 7: 8.0},
3: {8: 8.0, 2: 10.0, 4: 10.0},
4: {3: 10.0},
5: {6: 10.0},
6: {1: 8.0, 5: 10.0, 7: 10.0},
7: {8: 10.0, 1: 13.0, 2: 8.0, 6: 10.0},
8: {9: 10.0, 2: 13.0, 3: 8.0, 7: 10.0},
9: {8: 10.0}}

# - - - - - - - - - - - - - - - - - - - -
#                                      END GRAPHS

#                                       Starting
H = graph.Graph(G,GLENGTH,W)
# H.fixGraph() To fix my sins
H.run()
mc = maximal.MC(Qmax)
show = show_graph.Show(G,Qmax)
# Uncomment this to see the graph
# show.run()


# Using pruning?
if len(sys.argv) > 1:
    PRUNING = True
    print "\tUsing pruning approach\n"
    gl_algo = my_kruskal
else:
    print "\tRunning without pruning approach\n"
    print "python2.7 {0} <1> - enable pruning\n".format(sys.argv[0])
    gl_algo = naive_kruskal

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
        # pruning?
        TMP = []
        Wb = {}
        TMP = list(G)
        Wb = dict(W)

        if PRUNING:
            TMP,Wb = pruning.edge_pruning(TMP,Wb)
            TMP,Wb = pruning.pruning(TMP,Wb)

        Qmax = []      # To Calculate Max clique
        start_time = timeit.default_timer()
        print "[INFO] MST >", gl_algo.kruskal(TMP,Wb)
        # Calculates execution time
        elapsed = timeit.default_timer() - start_time

        # Tracing
        fp.write(str(elapsed)+'\n')

        time.sleep(0.2)
    fp.close()
    # TODO: Find out how to kill a Thread
    # Kill the Thread :(
    os.system("killall python")


if __name__ == '__main__':
    main()
