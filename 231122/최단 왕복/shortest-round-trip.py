import sys

INT_MAX = sys.maxsize

n, m = tuple(map(int, input().split()))

dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

#for i in range(1, n + 1):
#    dist[i][i] = 0


edges = [ tuple(map(int, input().split())) for _ in range(m)]


for i in range(m ):
    x, y, z = edges[i]
    dist[x][y] = min(dist[x][y], z)

for k in range(1, n + 1): 
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = INT_MAX * 2
for i in range(1, n + 1):
    for j in range(1, n + 1):
        result = min(result,  dist[i][j] + dist[j][i]) 

print(result)