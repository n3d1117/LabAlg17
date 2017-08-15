import random


class Graph(object):

    def __init__(self, numero_vertici):
        self.numero_vertici = numero_vertici

    # Matrice di adiacenza casuale utilizzando 'perc' come probabilita' di presenza di archi tra vertici (0-10)
    def matrice_adiacenza(self, perc):
        if perc < 0 or perc > 10:
            print 'percentuale non consentita!'
        else:
            count = self.numero_vertici
            matrix = [[0] * count for _ in range(count)]
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if random.randint(1, 10) <= perc:
                        matrix[i][j] = 1
            return matrix
