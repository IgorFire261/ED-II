class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def addAresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def busca(self, pai, i):
        if pai[i] == i:
            return i
        return self.busca(pai, pai[i])

    def uniao(self, pai, rank, x, y):
        x_raiz = self.busca(pai, x)
        y_raiz = self.busca(pai, y)

        if rank[x_raiz] < rank[y_raiz]:
            pai[x_raiz] = y_raiz
        elif rank[x_raiz] > rank[y_raiz]:
            pai[y_raiz] = x_raiz
        else:
            pai[y_raiz] = x_raiz
            rank[x_raiz] += 1

    def boruvka(self):
        pai = []
        rank = []
        arvore_minima = []

        for node in range(self.V):
            pai.append(node)
            rank.append(0)

        num_arvores = self.V
        while num_arvores > 1:
            menor = [None] * self.V

            for i in range(len(self.grafo)):
                u, v, w = self.grafo[i]
                set_u = self.busca(pai, u)
                set_v = self.busca(pai, v)

                if set_u != set_v:
                    if menor[set_u] is None or menor[set_u][2] > w:
                        menor[set_u] = [u, v, w]
                    if menor[set_v] is None or menor[set_v][2] > w:
                        menor[set_v] = [u, v, w]

            for node in range(self.V):
                if menor[node] is not None:
                    u, v, w = menor[node]
                    set_u = self.busca(pai, u)
                    set_v = self.busca(pai, v)
                    if set_u != set_v:
                        arvore_minima.append([u, v, w])
                        self.uniao(pai, rank, set_u, set_v)
                        num_arvores -= 1

        return arvore_minima


g = Grafo(4)
g.addAresta(0, 1, 10)
g.addAresta(0, 2, 6)
g.addAresta(0, 3, 5)
g.addAresta(1, 3, 15)
g.addAresta(2, 3, 4)

arvore_minima = g.boruvka()
print("Arestas na árvore de extensão mínima:")
for u, v, w in arvore_minima:
    print(f"{u} -- {v} == {w}")
