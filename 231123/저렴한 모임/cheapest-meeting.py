import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

a_start, b_start, end = tuple(map(int, input().split()))
dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    dist[i][i] = 0


edges = [ tuple(map(int, input().split())) for _ in range(m)]



for x, y, z in edges:
    dist[x][y] = min(dist[x][y], z)
    dist[y][x] = min(dist[y][x], z)


for k in range(1, n + 1): 
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            dist[j][i] = min(dist[j][i], dist[j][k] + dist[k][i])


result = dist[a_start][end] + dist[b_start][end]

for i in range(1, n + 1):
    result = min(result,  dist[a_start][i] + dist[b_start][i] + dist[i][end]) 

print(result)