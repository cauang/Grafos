from collections import deque
from graph import Graph

class BreadthFirstPaths:
    def __init__(self, G, s):
        self._marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.visit_order = []
        self.bfs(G, s)

    def bfs(self, G, s):
        self._marked[s] = True
        self.visit_order.append(s)
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for w in G.adj[v]:
                if not self._marked[w]:
                    self.edge_to[w] = v
                    self._marked[w] = True
                    self.visit_order.append(w)
                    queue.append(w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return reversed(path)