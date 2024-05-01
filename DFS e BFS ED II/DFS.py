
class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def adicionar_aresta(self,u,v):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append(v)
        
    def dfs_util(self,v,visitado):
        visitado.add(v)
        print(v,end=' ')
        
        for vizinho in self.grafo.get(v,[]):
            if vizinho not in visitado:
                self.dfs_util(vizinho,visitado)
      
    def DFS(self,inicio):
        visitado = set()
        self.dfs_util(inicio,visitado)
        
g = Grafo()
g.adicionar_aresta(0,1)
g.adicionar_aresta(0,2)
g.adicionar_aresta(1,2)
g.adicionar_aresta(2,0)
g.adicionar_aresta(2,3)
g.adicionar_aresta(3,3)

print("DFS a partir do vértice 2:\n")
g.DFS(2)
        
    