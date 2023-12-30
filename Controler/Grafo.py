from Model.Node import Node
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
import osmnx as ox

def cria_grafo():
    g = Grafo()

    g.add_edge("1", "2", 1500)
    g.add_edge("1", "3", 600)
    g.add_edge("1", "4", 1000)
    g.add_edge("3", "4", 450)
    g.add_edge("2", "3", 650)
    g.add_edge("2", "5", 900)
    g.add_edge("3", "6", 800)
    g.add_edge("4", "6", 800)
    g.add_edge("4", "7", 750)
    g.add_edge("5", "6", 650)
    g.add_edge("6", "7", 1100)
    g.add_edge("5", "8", 400)
    g.add_edge("6", "8", 1000)
    g.add_edge("6", "9", 1200)
    g.add_edge("8", "9", 550)
    g.add_edge("7", "9", 700)
    g.add_edge("7", "11", 750)
    g.add_edge("7", "10", 850)
    g.add_edge("9", "10", 450)
    g.add_edge("9", "12", 750)
    g.add_edge("8", "12", 1100)
    g.add_edge("10", "12", 400)
    g.add_edge("10", "11", 500)

    g.add_edge("2", "1", 1500)
    g.add_edge("3", "1", 600)
    g.add_edge("4", "1", 1000)
    g.add_edge("4", "3", 450)
    g.add_edge("3", "2", 650)
    g.add_edge("5", "2", 900)
    g.add_edge("6", "3", 800)
    g.add_edge("6", "4", 800)
    g.add_edge("7", "4", 750)
    g.add_edge("6", "5", 650)
    g.add_edge("7", "6", 1100)
    g.add_edge("8", "5", 400)
    g.add_edge("8", "6", 1000)
    g.add_edge("9", "6", 1200)
    g.add_edge("9", "8", 550)
    g.add_edge("9", "7", 700)
    g.add_edge("11", "7", 750)
    g.add_edge("10", "7", 850)
    g.add_edge("10", "9", 450)
    g.add_edge("12", "9", 750)
    g.add_edge("12", "8", 1100)
    g.add_edge("12", "10", 400)
    g.add_edge("11", "10", 500)

    g.add_heuristica("1", 0)
    g.add_heuristica("2", 668)
    g.add_heuristica("3", 491)
    g.add_heuristica("4", 534)
    g.add_heuristica("5", 962)
    g.add_heuristica("6", 1040)
    g.add_heuristica("7", 1160)
    g.add_heuristica("8", 1200)
    g.add_heuristica("9", 1440)
    g.add_heuristica("10", 1700)
    g.add_heuristica("11", 1660)
    g.add_heuristica("12", 1870)

    return g

class Grafo:

    def __init__(self, directed=False):
        self.m_nodes = []
        self.m_directed = directed
        self.m_graph = {}
        self.m_h = {}

    def add_edge(self, node1, node2, weight):
        n1 = Node(node1)
        n2 = Node(node2)
        if n1 not in self.m_nodes:
            n1_id = len(self.m_nodes)  # numeração sequencial
            n1.setId(n1_id)
            self.m_nodes.append(n1)
            self.m_graph[node1] = []

        if n2 not in self.m_nodes:
            n2_id = len(self.m_nodes)  # numeração sequencial
            n2.setId(n2_id)
            self.m_nodes.append(n2)
            self.m_graph[node2] = []

        self.m_graph[node1].append((node2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
            self.m_graph[node2].append((node1, weight))

    def get_nodes(self):
        return self.m_nodes

    def get_vizinhos(self, node):
        return [vizinho for vizinho, _ in self.m_graph.get(node, [])]

    def getNeighbours(self, nodo):
        lista = []
        for (adjacente, peso) in self.m_graph[nodo]:
            lista.append((adjacente, peso))
        return lista

    def getH(self, nodo):
        if nodo not in self.m_h.keys():
            return 1000
        else:
            return (self.m_h[nodo])

    def desenha(self):
        lista_v = self.m_nodes
        lista_a = []

        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                g.add_edge(n, adjacente, weight=peso)

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    def add_heuristica(self, n, estima):
        n1 = Node(n)
        if n1 in self.m_nodes:
            self.m_h[n] = estima

    def calcula_custo(self, caminho):
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    def procura_DFS_aux(self, start, end, path=[], visited=None):
        if visited is None:
            visited = set()

        path.append(start)
        visited.add(start)

        if start == end:
            # Calcular o custo do caminho usando a função que você já possui
            custoT = self.calcula_custo(path)
            return (path, custoT)

        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS_aux(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado

        path.pop()  # Se não encontrar, remover o que está no caminho...
        return None

    def procura_DFS(self, setores_a_visitar):
        res = []
        setores_a_visitar = list(setores_a_visitar)
        visited = set()

        for i in range(len(setores_a_visitar)):
            if i == 0:
                start = "1"
                end = setores_a_visitar[i]
            else:
                start = setores_a_visitar[i - 1]
                end = setores_a_visitar[i]

            resultado = self.procura_DFS_aux(str(start), str(end), path=[], visited=visited)

            if resultado is not None:
                res.append(resultado)

        caminho_combinado, custo_total = somar_caminhos(res)
        print(f"Caminho combinado: {caminho_combinado}")
        print(f"Custo total: {custo_total}")

        return res

    def procura_BFS_aux(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
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

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    def procura_BFS(self, setores_a_visitar):
        res = []
        setores_a_visitar = list(setores_a_visitar)

        for i in range(len(setores_a_visitar)):
            if i == 0:
                start = "1"
                end = setores_a_visitar[i]
            else:
                start = setores_a_visitar[i - 1]
                end = setores_a_visitar[i]

            resultado = self.procura_BFS_aux(str(start), str(end))

            if resultado is not None:
                res.append(resultado)

        caminho_combinado, custo_total = somar_caminhos(res)
        print(f"Caminho combinado: {caminho_combinado}")
        print(f"Custo total: {custo_total}")

        return res

    ##########################################
    #    A*
    ##########################################

    def procura_aStar_aux(self, start, end, visited=None):
        if visited is None:
            visited = set()

        open_list = {start}
        closed_list = set([])

        g = {}
        g[start] = 0

        parents = {}
        parents[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + self.getH(v) < g[n] + self.getH(n):
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
                if m not in open_list and m not in closed_list and m not in visited:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

            visited.add(n)  # Adiciona o nodo corrente à lista de visitados

        print('Path does not exist!')
        return None

    def procura_aStar(self, setores_a_visitar):
        res = []
        setores_a_visitar = list(setores_a_visitar)
        visited = set()

        for i in range(len(setores_a_visitar)):
            if i == 0:
                start = "1"
                end = setores_a_visitar[i]
            else:
                start = setores_a_visitar[i - 1]
                end = setores_a_visitar[i]

            resultado = self.procura_aStar_aux(str(start), str(end), visited=visited)

            if resultado is not None:
                res.append(resultado)

        caminho_combinado, custo_total = somar_caminhos(res)
        print(f"Caminho combinado: {caminho_combinado}")
        print(f"Custo total: {custo_total}")

        return res

    ##########################################
    #   Greedy
    ##########################################

    def greedy_aux(self, start, end, visited=None):
        if visited is None:
            visited = set()

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
                if m not in open_list and m not in closed_list and m not in visited:
                    open_list.add(m)
                    parents[m] = n

            open_list.remove(n)
            closed_list.add(n)

            visited.add(n)  # Adiciona o nodo corrente à lista de visitados

        print('Path does not exist!')
        return None

    def procura_greedy(self, setores_a_visitar):
        res = []
        setores_a_visitar = list(setores_a_visitar)
        visited = set()

        for i in range(len(setores_a_visitar)):
            if i == 0:
                start = "1"
                end = setores_a_visitar[i]
            else:
                start = setores_a_visitar[i - 1]
                end = setores_a_visitar[i]

            resultado = self.greedy_aux(str(start), str(end), visited=visited)

            if resultado is not None:
                res.append(resultado)

        caminho_combinado, custo_total = somar_caminhos(res)
        print(f"Caminho combinado: {caminho_combinado}")
        print(f"Custo total: {custo_total}")

        return res


def somar_caminhos(lista_caminhos):
    caminho_combinado = []
    custo_total = 0

    for caminho, custo in lista_caminhos:
        caminho_combinado.extend(caminho[:-1])  # Exclui o último nó do caminho para evitar duplicatas
        custo_total += custo

    caminho_combinado.append(lista_caminhos[-1][0][-1])  # Adiciona o último nó do último caminho

    return caminho_combinado, custo_total