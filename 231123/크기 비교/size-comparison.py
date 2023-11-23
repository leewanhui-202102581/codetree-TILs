import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    dist[i][i] = 1


edges = [ tuple(map(int, input().split())) for _ in range(m)]


for i in range(m ):
    x, y = edges[i]
    dist[x][y] = 1 #x가 y보다 크다

for k in range(1, n + 1): 
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] * dist[k][j])


for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dist[i][j] != 1 and dist[j][i] != 1:
            cnt += 1
    print(cnt)