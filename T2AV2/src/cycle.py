class Cycle:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self._cycle = None
        for s in range(G.V):
            if not self.marked[s]:
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj[v]:
            if self._cycle: return
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w, v)
            elif w != u:
                self._cycle = []
                x = v
                while x != w:
                    self._cycle.append(x)
                    x = self.edge_to[x]
                self._cycle.append(w)
                self._cycle.append(v)

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle