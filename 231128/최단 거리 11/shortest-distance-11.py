import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

edges = [tuple(map(int, input().split())) for _ in range(m)]

a, b = tuple(map(int, input().split()))

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

dist = [INT_MAX] * (n + 1) 


for i in range(m):
    x, y, z = edges[i] 
    graph[y][x] = z     #도착점을 시작점으로 
    graph[x][y] = z     #도착점을 시작점으로 


dist[b] = 0 #도착점을 시작점으로


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


print(dist[a])

x = a
print(x, end=" ")
while x != b:
    for i in range(1, n + 1):
        if graph[i][x] == 0:
            continue

        if dist[i] + graph[i][x] == dist[x]:
            x = i
            break

    print(x, end=" ")