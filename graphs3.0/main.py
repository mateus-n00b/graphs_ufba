#!/usr/bin/env python
# My Final Test from discipline Algorithms and Graphs - August 2017.1 (UFBA)
#
# Mateus Sousa (n00b), 2017 (UFBA)
# Iury Maia, 2017   (UFBA)
#
# Version 3.0
#
# License GPLv3
#
#
# Bugs Fixed:
#       List copy creating a pointer -> we used copy.deepcopy to do it
#       We've modified the pymobility module to add a SetSeed method

from pymobility.models.mobility import random_waypoint
from pymobility.models.mobility import SetSeed
from graph import Graph
import naive_kruskal
import my_kruskal
import pruning
import time,random
import timeit
import os,sys
import copy # to copy a list

#                                   Global vars
MAX_NODES = 25
MAX_RANGE = 100
SIM_TIME = 10000

#                                  Adj. List and Weights
G = [ [] for i in range(MAX_NODES)]
W = {}

SetSeed(1000)
# Default mobility model                      X    Y
mob = random_waypoint(MAX_NODES, dimensions=(500, 50), velocity=(0.1, 1.0), wt_max=0.8) # check this

H = Graph(G,W,mob,MAX_NODES,MAX_RANGE)
H.Run()

def main():
    global G
    global W

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

    for i in range(SIM_TIME):
        TMP = []
        Wb = {}
        TMP = copy.deepcopy(G) # Use this because there's a bug on python
        Wb = copy.deepcopy(W) # list attribution (https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list)

        if PRUNING:
            TMP,Wb = pruning.edge_pruning(TMP,Wb) # pruning every execution?
            TMP,Wb = pruning.pruning(TMP,Wb)

        start_time = timeit.default_timer()
        print "[INFO] MST >", gl_algo.kruskal(TMP,Wb)
        # Calculates execution time
        elapsed = timeit.default_timer() - start_time

        # Tracing
        trace.write(str(elapsed)+'\n')

        time.sleep(random.uniform(0,1))
    trace.close()
    # # TODO: Find out how to kill a Thread
    # # Kill the Thread :(
    os.system("killall python")


if __name__ == '__main__':
    main()
