def kruskal(G,W):
    visited = set()
    path = []
    nxt = None

    while len(visited) < len(G):
        distance = 99999.9
        for s in range(0,len(G)):
            for d in G[s]:
                if s in visited and d in visited or s == d:
                    continue
                if W[s][d] < distance:
                    distance = W[s][d]
                    pre = s
                    nxt = d

        path.append((pre, nxt))
        visited.add(pre)
        visited.add(nxt)

    return path
