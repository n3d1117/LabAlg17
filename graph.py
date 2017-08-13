class Graph(object):
    _matrice_adiacenza = None

    def __init__(self, numero_vertici):
        self.vertici = []
        self.numero_vertici = numero_vertici

    def add(self, da, a):
        vertice = da, a
        self.vertici.append(vertice)

    @property
    def matrice_adiacenza(self):
        count = self.numero_vertici
        matrix = [[0] * count for _ in range(count)]
        for src, dest in self.vertici:
            src -= 1
            dest -= 1
            matrix[src][dest] = 1
        self._matrice_adiacenza = matrix
        return self._matrice_adiacenza


if __name__ == '__main__':
    g = Graph(5)
    g.add(1, 2)
    g.add(2, 3)
    g.add(1, 3)
    print g.matrice_adiacenza
