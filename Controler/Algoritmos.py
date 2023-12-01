from queue import Queue


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


def procura_DFS(grafo, inicio, setores_a_visitar, visitados=[]):
    visitados = visitados.copy()
    visitados.append(inicio)

    if inicio in setores_a_visitar:
        setores_a_visitar.remove(inicio)

    for (vizinho, _) in grafo.m_graph.get(inicio, []):
        if vizinho not in visitados and setores_a_visitar:
            procura_DFS(grafo, vizinho, setores_a_visitar, visitados)

    return visitados


def procura_BFS(self, start, end):
    visited = set()
    fila = Queue()
    custo = 0
    fila.put(start)
    visited.add(start)

    parent = dict()
    parent[start] = None

    path_found = False
    while not fila.empty() and path_found == False:
        nodo_atual = fila.get()
        if nodo_atual == end:
            path_found = True
        else:
            for (adjacente, peso) in self.m_graph[nodo_atual]:
                if adjacente not in visited:
                    fila.put(adjacente)
                    parent[adjacente] = nodo_atual
                    visited.add(adjacente)

    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
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
