# My Final Test from discipline Algorithms and Graphs - August 2017.1 (UFBA)
#
# Mateus Sousa (n00b), 2017 (UFBA)
# Iury Maia, 2017   (UFBA)
#
# Version 3.0
#
# License GPLv3

from pymobility.models.mobility import random_waypoint
import graph

#                                   Global vars
MAX_NODES = 4
MAX_RANGE = 100

#                                  Adj. List and Weights
G = [ [] for i in range(MAX_NODES)]
W = {}

# Default mobility model
mob = random_waypoint(MAX_NODES, dimensions=(200, 100), velocity=(0.1, 1.0), wt_max=1.0)
