class Node:
    def __init__(self, name):
        self.m_name = name
        self.m_id = -1

    def getId(self):
        return self.m_id

    def setId(self, idx):
        self.m_id = idx

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.m_name == other.m_name
        elif isinstance(other, str):
            return self.m_name == other
        return False

    def __hash__(self):
        return hash(self.m_name)