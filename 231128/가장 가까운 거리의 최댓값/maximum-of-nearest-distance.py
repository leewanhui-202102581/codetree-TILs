import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))
a, b, c = tuple(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]



graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]


for x, y, z in edges: 
    graph[y][x] = z   
    graph[x][y] = z 


def Dijkstra(num):
    dist = [INT_MAX] * (n + 1) 
    dist[num] = 0 
    visited = [False] * (n + 1)

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

dist_a = Dijkstra(a)
dist_b = Dijkstra(b)
dist_c = Dijkstra(c)

result = 0

for i in range(1, n+1):
    result = max(result, min(dist_a[i], dist_b[i], dist_c[i]))

print(result)