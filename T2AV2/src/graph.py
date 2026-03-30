from algs4.bag import Bag

class Graph:
    def __init__(self, v):
        self.V = v
        self.E = 0
        self.adj = [Bag() for _ in range(self.V)]

    def __str__(self):
            lines = ["%d vertices, %d edges" % (self.V, self.E)]
            for v in range(self.V):
                # Transformamos o iterador em uma lista para o Python conseguir ler
                vizinhos_lista = []
                for w in self.adj[v]:
                    vizinhos_lista.append(str(w))
                
                neighbors = " ".join(vizinhos_lista)
                lines.append("%d: %s" % (v, neighbors))
            return "\n".join(lines)

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1