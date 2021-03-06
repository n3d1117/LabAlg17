import matplotlib.pyplot as plt
from tests import Tests
import numpy as np


class Exp:

    def __init__(self):
        self.t = Tests()

    def start_first(self):
        numbers = self.t.execute_first()
        x = range(1, len(numbers)+1)
        plt.figure()
        plt.plot(x, numbers)
        plt.xlabel('Dimensione grafo')
        plt.ylabel('Numero di componenti fortemente connesse')
        plt.grid()

    def start_second(self):
        numbers = self.t.execute_second()
        x = np.arange(0.0, 1.1, 0.1)
        plt.figure()
        plt.plot(x, numbers)
        plt.xlabel("Probabilita' di archi")
        plt.ylabel('Numero di componenti fortemente connesse')
        plt.grid()

    def start_third(self):
        grandezze = self.t.execute_third()
        x = range(1, len(grandezze)+1)
        plt.figure()
        plt.plot(x, grandezze)
        plt.xlabel("Dimensione grafo")
        plt.ylabel('Grandezza massima componenti fortemente connesse')
        plt.grid()

    def start_fourth(self):
        tempi = self.t.execute_fourth()
        x = range(1, len(tempi)+1)
        plt.figure()
        plt.plot(x, tempi)
        plt.xlabel("Dimensione grafo")
        plt.ylabel('Tempo di esecuzione (secondi)')
        plt.grid()


if __name__ == '__main__':

    e = Exp()

    e.start_first()
    e.start_second()
    e.start_third()
    e.start_fourth()

    plt.show()
