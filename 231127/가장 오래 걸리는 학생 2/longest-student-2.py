import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

dist = [INT_MAX] * (n + 1) 


for i in range(m):
    x, y, z = edges[i]
    graph[y][x] = z


dist[n] = 0


for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    visited[min_index] = True


    for j in range(1, n + 1):
        if graph[min_index][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])


dist[0] = 0 #0 제외 위함
print(max(dist))