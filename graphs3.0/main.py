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
from log import *

import time,random
import timeit
import os,sys
import copy # to copy a list

#                                   Global vars
MAX_NODES = 25
MAX_RANGE = 100
SIM_TIME = 1000
HOP_COUNT = 5

#                                  Adj. List and Weights
G = [ [] for i in range(MAX_NODES)]
W = {}

#                                  Seeds
SetSeed(MAX_NODES) # Set a seed to control the randomicity
random.seed(MAX_NODES)

# Default mobility model                      X    Y
mob = random_waypoint(MAX_NODES, dimensions=(1000, 100), velocity=(10.0, 20.0), wt_max=0.5) # check this

#                                       Graph object
H = Graph(G,W,mob,MAX_NODES,MAX_RANGE)
H.Run()

def main():
    global G
    global W
    PRUNING = False
    T = set()

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

    tmp_aux = copy.deepcopy(G)
    tmp_auxb = copy.deepcopy(W)

    for i in range(SIM_TIME):
        TMP = list()
        Wb = dict()

        try:
            TMP = copy.deepcopy(G) # Use this because there's a bug on
            Wb = copy.deepcopy(W) # list attribution (https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list)
        except:
            TMP = tmp_aux
            Wb = tmp_auxb

        if PRUNING:
            TMP,Wb = pruning.edge_pruning(TMP,Wb) # pruning every execution?
            TMP,Wb = pruning.pruning(TMP,Wb)

        # start_time = timeit.default_timer()
        start_time = timeit.time.time()
        T = gl_algo.kruskal(TMP,Wb) # Creates the tree
        # Calculates execution time
        # elapsed = timeit.default_timer() - start_time
        elapsed = timeit.time.time() - start_time

        # Send a packet
        index = random.randint(0,MAX_NODES-1)
        H.SendPacket(index,HOP_COUNT,index,T)
        print "Node {0} sending packet".format(index)
        H.clean()

        # Tracing
        trace.write(str(elapsed)+'\n')
        # Take a nap
        time.sleep(random.uniform(0,1))


    trace.close()
    # Test
    closeFile()
    # # TODO: Find out how to kill a Thread
    # # Kill the Thread :(
    os.system("killall python")


if __name__ == '__main__':
    main()
