import networkx as nx

def find_cycle_mst(H,u,v,mst):
    G = nx.Graph()
    for node in range(0,len(H)):
        G.add_node(node)
        for edge in H[node]:
            G.add_edge(node,edge)

    cycle = nx.find_cycle(G,source=u)
    # cycle = nx.cycle_basis(G,u)
    # Filter output
    return cycle


#                   Graph for tests
# H = [
# [1],
# [0,2,6,7],
# [1,7,3,8],
# [2,4,8],
# [3],
# [6],
# [5,1,7],
# [6,2,1,8],
# [2,7,9,3],
# [8]
# ]
#
# print find_cycle_mst(H,7,9,[])
