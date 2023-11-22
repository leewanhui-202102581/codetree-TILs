import sys

INT_MAX = sys.maxsize

n, m, p, q = tuple(map(int, input().split()))

#starts from 1
dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

red = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, p+1):
    red[i][i] == True
    for j in range(1, n+1):
        red[i][j], red[j][i] = True, True


edges = [ list(map(int, input().split())) for _ in range(m)]
queries = [ tuple(map(int, input().split())) for _ in range(q)]

for i in range(m ):
    x, y, z = edges[i]
    dist[x][y] = min(dist[x][y], z)

for k in range(1, n+1): 
    for i in range(1, n+1): 
        for j in range(1, n+1):
            if dist[i][j] >= dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k] + dist[k][j]
                red[i][j] = red[i][j] | red[i][k] | red[k][j] #셋 중 하나라도 1이면 1

cnt = 0
min_sum = 0
for a, b in queries:
    if red[a][b]:
        cnt += 1
        min_sum += dist[a][b]

print(cnt)
print(min_sum)