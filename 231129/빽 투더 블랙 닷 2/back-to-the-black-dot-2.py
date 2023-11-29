import sys


INT_MAX = sys.maxsize


n, m = tuple(map(int, input().split()))

red1, red2 = tuple(map(int, input().split()))

edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for x, y, z in edges:
    graph[y][x] = z  
    graph[x][y] = z


def Dijkstra(end):
    visited = [False] * (n + 1)
    dist = [INT_MAX] * (n + 1)

    dist[end] = 0 

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
            if dist[j] > dist[min_index] + graph[min_index][j]:
                dist[j] = dist[min_index] + graph[min_index][j]
    return dist


red1_dist = Dijkstra(red1)
red2_dist = Dijkstra(red2)

result = INT_MAX
for i in range(1, n+1):
    if i == red1 or i == red2:
        continue
    result = min(result, red1_dist[i] + red1_dist[red2] + red2_dist[i])

print(result if result < INT_MAX else -1)