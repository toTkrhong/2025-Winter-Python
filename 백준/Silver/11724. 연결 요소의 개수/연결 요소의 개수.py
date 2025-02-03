import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

visited = [False] * n

def dfs(node):
    visited[node] = True
    for neighbor in range(n):
        if graph[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor)

connected_components = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        connected_components += 1

print(connected_components)