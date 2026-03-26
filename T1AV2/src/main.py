import os
from graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths

def main():
    estados = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
    nome_para_id = {nome: i for i, nome in enumerate(estados)}
    id_para_nome = {i: nome for i, nome in enumerate(estados)}

    caminho_arquivo = os.path.join(os.path.dirname(__file__), '..', 'dados', 'nordeste.txt')
    
    try:
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()
            
            V = int(linhas[0].strip())
            E = int(linhas[1].strip())
            
            g = Graph(V)
            for i in range(2, 2 + E):
                v, w = linhas[i].split()
                g.add_edge(int(v), int(w))
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado. Verifique a pasta 'dados'.")
        return

    print("--- Problema com Grafos - Região Nordeste ---")
    origem_str = input("Digite o estado de origem X (ex: CE): ").strip().upper()
    destino_str = input("Digite o estado de destino Y (ex: BA): ").strip().upper()

    if origem_str not in estados or destino_str not in estados:
        print("Erro: Estado(s) inválido(s).")
        return

    X = nome_para_id[origem_str]
    Y = nome_para_id[destino_str]

    dfs = DepthFirstPaths(g, X)
    bfs = BreadthFirstPaths(g, X)

    print("\n" + "="*50)
    print("RESPOSTAS DO TRABALHO")
    print("="*50)

    alcança = dfs.has_path_to(Y)
    print(f"1) É possível sair de {origem_str} e chegar a {destino_str}? \n   -> {'Sim' if alcança else 'Não'}\n")

    caminho_dfs = dfs.path_to(Y)
    if caminho_dfs:
        print(f"2) Caminho encontrado pela DFS: \n   -> {' -> '.join([id_para_nome[v] for v in list(caminho_dfs)])}\n")
    else:
        print(f"2) Caminho encontrado pela DFS: \n   -> Nenhum\n")

    caminho_bfs = bfs.path_to(Y)
    if caminho_bfs:
        print(f"3) Caminho encontrado pela BFS: \n   -> {' -> '.join([id_para_nome[v] for v in list(caminho_bfs)])}\n")
    else:
        print(f"3) Caminho encontrado pela BFS: \n   -> Nenhum\n")

    alcancaveis = [id_para_nome[i] for i in range(g.V) if dfs.has_path_to(i)]
    print(f"4) Estados alcançáveis a partir de {origem_str}: \n   -> {', '.join(alcancaveis)}\n")

    if hasattr(dfs, 'visit_order'):
        print(f"5) Ordem de visita da DFS: \n   -> {' -> '.join([id_para_nome[v] for v in dfs.visit_order])}\n")
    else:
        print(f"5) Ordem de visita da DFS: \n   -> (Atributo não implementado)\n")

    if hasattr(bfs, 'visit_order'):
        print(f"6) Ordem de visita da BFS: \n   -> {' -> '.join([id_para_nome[v] for v in bfs.visit_order])}")
    else:
        print(f"6) Ordem de visita da BFS: \n   -> (Atributo não implementado)")
    print("="*50)

if __name__ == '__main__':
    main()

