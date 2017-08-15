from dfs import DFS
import numpy as np


class SCC:

    def __init__(self, matrice_adiacenza):
        self.matrice_adiacenza = matrice_adiacenza

    def scc(self):

        # calcola i tempi di completamento per ciascun vertice
        dfs = DFS(self.matrice_adiacenza)

        # memorizzo i vertici in una variabile globale
        vertici = dfs.vertici

        # calcolo il grafo trasposto formato dagli archi del grafo originale con direzioni invertite
        matrice_trasposta = self.trasposta(self.matrice_adiacenza)

        # chiamo DFS su grafo trasposto passando i vertici calcolati in precedenza
        dfs_t = DFS(matrice_trasposta, vertici)

        return dfs_t.numero_di_scc, dfs_t.dizionario_scc

    @staticmethod
    def trasposta(matrice):
        return np.array(matrice).transpose()

if __name__ == '__main__':

    # Esempio libro
    m = [[0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1]]

    n, d = SCC(m).scc()
    print "ho trovato %s componenti fortemente connesse!" % n
    for i in range(n):
        print "la scc #%s ha %s nodi ~> %s" % (i + 1, len(d[i]), d[i])
