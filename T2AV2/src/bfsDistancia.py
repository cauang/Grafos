from collections import deque

class BFSDistancia:
    def __init__(self, G, s):
        self.dist_to = [-1 for _ in range(G.V)]
        self.bfs(G, s)

    def bfs(self, G, s):
        queue = deque([s])
        self.dist_to[s] = 0
        while queue:
            v = queue.popleft()
            for w in G.adj[v]:
                if self.dist_to[w] == -1:
                    self.dist_to[w] = self.dist_to[v] + 1
                    queue.append(w)