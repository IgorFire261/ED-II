from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
        
    def adicionar_aresta(self,u,v):
        self.grafo[u].append(v)
    
    def BFS(self, s):
        visitado = [False]  * (len(self.grafo))
        
        fila = []
        
        fila.append(s)
        visitado[s] = True
        
        while fila:
            s = fila.pop(0)
            print(s," ")
            
            for i in self.grafo[s]:
                print(visitado[i])
                if visitado[i] == False:
                    fila.append(i)
                    visitado[i] = True
            

g = Grafo()
g.adicionar_aresta(0,1)  
g.adicionar_aresta(0,2)  
g.adicionar_aresta(1,2)  
g.adicionar_aresta(2,0)  
g.adicionar_aresta(2,3)  
g.adicionar_aresta(3,3)  

print("Execução do BFS começando pelo vértice 2")
g.BFS(2)
