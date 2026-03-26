from graph import Graph

class DepthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.visit_order = []
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.visit_order.append(v)
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)

    def has_path_to(self, v):
        return self.marked[v]

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