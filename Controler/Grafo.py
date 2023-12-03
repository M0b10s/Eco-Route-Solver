from Model.Node import Node
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem


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

