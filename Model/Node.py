from math import radians, sin, cos, sqrt, atan2

class Node:
    def __init__(self, name, latitude=None, longitude=None):
        self.m_name = name
        self.m_id = -1
        self.m_latitude = latitude
        self.m_longitude = longitude

    def getId(self):
        return self.m_id

    def setId(self, idx):
        self.m_id = idx

    def getName(self):
        return self.m_name

    def setlatitude(self, latitude):
        self.m_latitude = latitude

    def getlatitude(self):
        return self.m_latitude

    def setlongitude(self, longitude):
        self.m_longitude = longitude

    def getlongitude(self):
        return self.m_longitude

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.m_name == other.m_name
        elif isinstance(other, str):
            return self.m_name == other
        return False

    def __hash__(self):
        return hash(self.m_name)

def haversine_distance(lat1, lon1, lat2, lon2):
    # Função para calcular a distância haversine entre dois pontos
    R = 6371  # Raio médio da Terra em km

    # Converter coordenadas de graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Diferenças de coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula haversine
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distância em km
    distance = R * c * 1000

    return distance
