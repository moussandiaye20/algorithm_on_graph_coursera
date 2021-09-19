#Uses python3

import sys
import queue

def bipartite(adj):
     
    from collections import defaultdict
    colors=defaultdict(lambda:-1)
    def dfs(x,color):
       
        colors[x]=color
        for neighbor in adj[x]:
            if colors[x]==colors[neighbor]:return 0
            if colors[neighbor]==-1:
                 
    
                if    dfs(neighbor,color^1):
                    return 1
        return 1
    for vertex in range(len(adj)):
        if vertex not in visited:
            if dfs(vertex,0)==0:
                return 0

             
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
