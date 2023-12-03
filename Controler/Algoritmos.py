from queue import Queue

from View.Consulta_grafo import consulta_grafo
from main import grafo


# from main import grafo


def devolve_setores(servicos):
    setores = set()
    for s in servicos:
        setores.add(s.get_destino())

    return setores


def calcula_custo(self, caminho):
    teste = caminho
    custo = 0
    i = 0
    while i + 1 < len(teste):
        custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
        i = i + 1
    return custo


def procura_DFS(grafo, inicio, setores_a_visitar, visitados=None):
    if visitados is None:
        visitados = []

    inicio_str = str(inicio)
    visitados.append(inicio_str)

    if inicio_str in setores_a_visitar:
        setores_a_visitar.remove(inicio_str)

    vizinhos = grafo.get_vizinhos(inicio_str)

    for vizinho in vizinhos:
        if vizinho not in visitados and len(setores_a_visitar) > 0:
            procura_DFS(grafo, vizinho, setores_a_visitar, visitados)

    return visitados


def procura_BFS(self, inicio, setores_a_visitar):
    visited = set()
    fila = Queue()

    fila.put(inicio)
    visited.add(inicio)

    parent = dict()
    parent[inicio] = None

    path_found = False
    while not fila.empty() and not path_found:
        nodo_atual = fila.get()
        if nodo_atual == setores_a_visitar:
            path_found = True
        else:
            if nodo_atual in self.m_graph:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

    path = []
    custo = 0
    if path_found:
        path.append(setores_a_visitar)
        while parent[setores_a_visitar] is not None:
            path.append(parent[setores_a_visitar])
            setores_a_visitar = parent[setores_a_visitar]
        path.reverse()
        custo = self.calcula_custo(path)
    return (path, custo)


def greedy(self, start, end):
    open_list = set([start])
    closed_list = set([])

    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n is None or self.m_h[v] < self.m_h[n]:
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)
            reconst_path.reverse()

            return (reconst_path, self.calcula_custo(reconst_path))

        for (m, weight) in self.getNeighbours(n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n

        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None


def greedy_search(veiculo, grafo):
    rota = []
    for nó in veiculo.nos:
        rota.append(nó)
        for vizinho in grafo.get_vizinhos(nó):
            if vizinho not in rota:
                if vizinho.custo < rota[-1].custo:
                    rota.insert(rota.index(nó) + 1, vizinho)
                    break
    return rota
