from graph import Graph
from scc import SCC
from timeit import default_timer as timer


class Tests:

    def __init__(self):
        self.grandezza_fissata = 5
        self.grandezze_crescenti = range(1, 30)

        self.prob_fissata = 2
        self.prob_crescenti = range(0, 11)

    # Variazione numero di scc per grafi di dimensione crescente e probabilita' fissata 0.2
    def execute_first(self):
        numbers = []
        for i in self.grandezze_crescenti:
            g = Graph(i)
            m = g.matrice_adiacenza(self.prob_fissata)
            n, _ = SCC(m).scc()
            numbers.append(n)
        return numbers

    # Variazione numero di scc per grafi di dimensione fissata 5 e probabilita' crescente
    def execute_second(self):
        numbers = []
        for i in self.prob_crescenti:
            g = Graph(self.grandezza_fissata)
            m = g.matrice_adiacenza(i)
            n, _ = SCC(m).scc()
            numbers.append(n)
        return numbers

    # Variazione grandezza massima scc per grafi di dimensione crescente e probabilita' fissata 0.2
    def execute_third(self):
        grandezze = []
        for i in self.grandezze_crescenti:
            g = Graph(i)
            m = g.matrice_adiacenza(self.prob_fissata)
            _, d = SCC(m).scc()

            grandezza_max = 1
            for j in range(len(d)):
                if len(d[j]) > grandezza_max:
                    grandezza_max = len(d[j])
            grandezze.append(grandezza_max)

        return grandezze

    # Variazione dei tempi dell'algoritmo per trovare scc per grafi di dimensione crescente e probabilita' fissata 0.2
    def execute_fourth(self):
        tempi = []
        for i in self.grandezze_crescenti:
            g = Graph(i)
            m = g.matrice_adiacenza(self.prob_fissata)
            start = timer()
            _, _ = SCC(m).scc()
            end = timer()
            tempi.append(end-start)
        return tempi

    def execute_fifth(self):
        for i in [5, 10, 15, 20, 25, 30, 35, 40]:
            scc = []
            vol = []
            g = Graph(i)

            for j in range(0, 11, 1):
                m = g.matrice_adiacenza(j)
                n, d = SCC(m).scc()

                grandezza_max = 1
                for a in range(len(d)):
                    if len(d[a]) > grandezza_max:
                        grandezza_max = len(d[a])

                scc.append(grandezza_max)
                vol.append(grandezza_max)

            # Stampa sequenza di valori separati da &, utile per tabella LaTeX
            print ' & '.join([str(a) for a in scc])
            print ' & '.join([str(a) for a in vol])
