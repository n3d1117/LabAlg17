from vertice import Vertice


class DFS:
    def __init__(self, matrice_adiacenza, vertici_scc=None):

        self.matrice_adiacenza = matrice_adiacenza

        # Inizializza vertici con colore bianco 'W' e predecessore None
        self.vertici = [Vertice(i) for i in range(len(self.matrice_adiacenza))]

        # Variabile globale per registrare informazioni temporali
        self.time = 0

        # Variabili per la memorizzazione di informazioni riguardanti le scc
        self.numero_di_scc = 0  # numero di componenti fortemente connesse del grafo
        self.dizionario_scc = {}  # dizionario che memorizza l'insieme di vertici di ogni componente fortemente connessa

        # Booleano che indica se siamo al passo 3 dell'algoritmo scc
        self.usaDfsModificata = vertici_scc is not None
        if self.usaDfsModificata:
            self.dfs_scc(vertici_scc)
        else:
            self.dfs()

    # Funzione originale dfs (Depth First Search)
    # Chiama dfs_visit per tutti i vertici bianchi
    # Se siamo nel passo 3 di scc, memorizzo anche le informazioni riguardanti le componenti fortemente connesse
    def dfs(self):
        for i in range(len(self.vertici)):
            if self.vertici[i].colore == 'W':
                if self.usaDfsModificata:
                    self.numero_di_scc += 1  # incremento numero di componenti fortemente connesse del grafo
                    self.dizionario_scc[self.numero_di_scc - 1] = [i]  # memorizzo vertice iniziale
                self.dfs_visit(i)

    # Funzione alternativa per il passo 3 di scc: si basa su una array di vertici scoperti in precedenza
    # Prima colora tutti i vertici scoperti di bianco e mette a None i predecessori
    # Poi ordina i vertici in ordine decrescente rispetto ai tempi di completamento u.f
    # Infine chiama dfs() originale
    def dfs_scc(self, vertici_scc):
        self.vertici = vertici_scc
        for i in range(len(self.vertici)):
            self.vertici[i].colore = 'W'
            self.vertici[i].predecessore = None
        self.vertici.sort(key=lambda x: x.f, reverse=True)
        self.dfs()

    # Funzione dfs_visit
    def dfs_visit(self, u):
        vertice = self.vertici[u]

        self.time += 1  # Il vertice bianco u e' stato appena scoperto
        vertice.d = self.time
        vertice.colore = 'G'

        for i in range(len(self.vertici)):
            if self.arco(u, i) and self.vertici[i].colore == 'W':

                if self.usaDfsModificata:
                    self.append(self.numero_di_scc - 1, (u, i))  # aggiorno vertici presenti in una scc

                self.vertici[i].predecessore = u
                self.dfs_visit(i)

        vertice.colore = 'B'  # Colora di nero il vertice; visita completata
        self.time += 1
        vertice.f = self.time

    # Ritorna True se i e' adiacente a u
    def arco(self, u, i):
        return self.matrice_adiacenza[u][i] == 1

    # Inserisce i valori value se non sono gia' presenti nel dizionario all'indice dato
    def append(self, index, value):
        for v in value:
            if v not in self.dizionario_scc[index]:
                self.dizionario_scc[index].append(v)
