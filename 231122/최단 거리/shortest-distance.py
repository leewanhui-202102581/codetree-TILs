n, m = tuple(map(int, input().split()))

dist = [ list(map(int, input().split())) for _ in range(n)]

queries = [ tuple(map(int, input().split())) for _ in range(m)]



for k in range(n): 
    for i in range(n): 
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


for a, b in queries:
    print(dist[a-1][b-1])