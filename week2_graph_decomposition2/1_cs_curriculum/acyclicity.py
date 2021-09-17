#Uses python3

import sys


def acyclic(adj):

    from collections import defaultdict
    visited=defaultdict(int)

    def dfs(x):
        visited[x]=1
        for neighbor in adj[x]:
            if visited[neighbor]==0:
                if dfs(neighbor)==1:
        
                    return 1
            elif  visited[neighbor]==1:
                return 1
            
        visited[x]=2
        return 0
    for vertex in range(len(adj)):
        if visited[vertex]==0:
            if dfs(vertex)==1:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
