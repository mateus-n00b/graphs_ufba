#!/usr/bin/env python
# My Final Test from discipline Algorithms and Graphs - August 2017.1 (UFBA)
#
# Mateus Sousa (n00b), 2017 (UFBA)
# Iury Maia, 2017   (UFBA)
#
# Version 3.0
#
# License GPLv3

from pymobility.models.mobility import random_waypoint
from graph import Graph
import naive_kruskal
import my_kruskal
import pruning
import time
import timeit
import os,sys

#                                   Global vars
MAX_NODES = 4
MAX_RANGE = 100

#                                  Adj. List and Weights
G = [ [] for i in range(MAX_NODES)]
W = {}

# Default mobility model                      X    Y
mob = random_waypoint(MAX_NODES, dimensions=(500, 50), velocity=(0.1, 1.0), wt_max=1.0)

H = Graph(G,W,mob,MAX_NODES,MAX_RANGE)
H.Run()

def main():
    PRUNING = False
    # Using pruning?
    if len(sys.argv) > 1:
        PRUNING = True
        print "\tUsing pruning approach\n"
        gl_algo = my_kruskal
    else:
        print "\tRunning without pruning approach\n"
        print "python2.7 {0} <1> - enable pruning\n".format(sys.argv[0])
        gl_algo = naive_kruskal


    # Enable time tracing
    f =  "/tmp/pruning.txt" if PRUNING  else "/tmp/nopruning.txt"
    trace = open(f,'a+')

    for i in range(10000):
        TMP = []
        Wb = {}
        TMP = list(G)
        Wb = dict(W)

        if PRUNING:
            TMP,Wb = pruning.edge_pruning(TMP,Wb)
            TMP,Wb = pruning.pruning(TMP,Wb)

        start_time = timeit.default_timer()
        print "[INFO] MST >", gl_algo.kruskal(TMP,Wb)
        # Calculates execution time
        elapsed = timeit.default_timer() - start_time

        # Tracing
        trace.write(str(elapsed)+'\n')

        time.sleep(0.5)
    # trace.close()
    # # TODO: Find out how to kill a Thread
    # # Kill the Thread :(
    os.system("killall python")


if __name__ == '__main__':
    main()
