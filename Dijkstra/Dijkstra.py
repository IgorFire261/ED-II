import heapq

def dijkstra(graph, inicio):
    #dicionário que armazena a menor distância conhecida até cada vértice, inicialmente todas são definidas como infinito, menos o vértice inicial que inicia como 0.
    distancia = {v: float("inf") for v in graph}
    distancia[inicio] = 0
    #fila para armazenar os vértices a serem explorados
    fila = [(0, inicio)]
    
    while fila:
        #a cada iteração o vértice com menor distância é retirado da fila
        distancia_atual, v_atual = heapq.heappop(fila)
        
        if distancia_atual > distancia[v_atual]:
            continue
        #calcula-se a nova distância para cada vizinho 
        for vizinho, peso in   graph[v_atual].items():
            distancia_nova = distancia_atual + peso
        #se a distância nova form menor que a distância de seu vizinho, a distância é calculada e o vizinho é adicionado a fila
            if distancia_nova < distancia[vizinho]:
                distancia[vizinho] = distancia_nova
                heapq.heappush(fila, (distancia_nova, vizinho))

    return distancia

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

v_inicio = 'A'
print(dijkstra(graph, v_inicio))
