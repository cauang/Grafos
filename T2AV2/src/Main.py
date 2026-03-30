import os
import sys

sys.path.append(os.path.dirname(__file__))

from graph import Graph
from cc import CC
from cycle import Cycle
from bfsDistancia import BFSDistancia

def main():
    caminho = os.path.join(os.path.dirname(__file__), '..', 'dados', 'entrada.txt')
    with open(caminho, 'r') as f:
        V = int(f.readline())
        E = int(f.readline())
        g = Graph(V)
        for _ in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)

    print("--- T2: O Grafo do Cavalo ---")
    print("\n1) Lista de adjacência:")
    print(g)

    cc = CC(g)
    print(f"\n2) Componentes conexas: {cc.count}")
    for i in range(cc.count):
        membros = [str(v) for v in range(g.V) if cc.id[v] == i]
        print(f"   Componente {i}: {' '.join(membros)}")

    dist_bfs = BFSDistancia(g, 0)
    d = dist_bfs.dist_to
    print(f"\n3) Distância mínima entre (0,0) e (2,2): {d if d != -1 else 'Inalcançável'}")

    cyc = Cycle(g)
    print(f"\n4) O grafo possui ciclo? {'Sim' if cyc.has_cycle() else 'Não'}")
    if cyc.has_cycle():
        print(f"5) Um ciclo encontrado: {' '.join(map(str, cyc.cycle()))}")

if __name__ == "__main__":
    main()