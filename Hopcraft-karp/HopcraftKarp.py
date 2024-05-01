from collections import deque

class HopcroftKarp:
    def __init__(self, graph):
        self.graph = graph
        self.pair_u = {}
        self.pair_v = {}
        self.dist = {}
        self.matching = 0

    def bfs(self):
        queue = deque()
        for u in self.graph.keys():
            if u not in self.pair_u:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        self.dist[None] = float('inf')
        
        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[None]:
                for v in self.graph[u]:
                    if self.dist.get(self.pair_v.get(v), float('inf')) == float('inf'):
                        self.dist[self.pair_v.get(v)] = self.dist[u] + 1
                        queue.append(self.pair_v.get(v))
        
        return self.dist[None] != float('inf')

    def dfs(self, u):
        if u is not None:
            for v in self.graph[u]:
                if self.dist.get(self.pair_v.get(v)) == self.dist[u] + 1:
                    if self.dfs(self.pair_v.get(v)):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float('inf')
            return False
        return True

    def max_matching(self):
        while self.bfs():
            for u in self.graph.keys():
                if u not in self.pair_u:
                    if self.dfs(u):
                        self.matching += 1

        return self.matching

if __name__ == "__main__":
    graph = {
        'A': ['1', '2'],
        'B': ['1'],
        'C': ['2', '3'],
        'D': ['3']
    }

    hk = HopcroftKarp(graph)
    max_matching = hk.max_matching()
    print("Tamanho do emparelhamento máximo:", max_matching)
    print("Emparelhamento máximo:", hk.pair_u)
