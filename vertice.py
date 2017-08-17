class Vertice:
    def __init__(self, numero, colore='W', d=0, f=0, predecessore=None):
        self.numero = numero
        self.colore = colore  # 'W' se t < d, 'G' se d < t < f, 'B' se t > f
        self.d = d  # tempo di scoperta
        self.f = f  # tempo di completamento
        self.predecessore = predecessore
