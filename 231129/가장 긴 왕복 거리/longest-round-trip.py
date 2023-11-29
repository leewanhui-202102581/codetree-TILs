import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m, x = tuple(map(int, input().split()))

# 간선을 입력받습니다.
edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

graph1 = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
graph2 = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
dist1 = [INT_MAX] * (n + 1)
dist2 = [INT_MAX] * (n + 1)
ans = 0


def dijkstra(dist, graph):
    # visited값을 전부 False로 초기화 해놓고 시작합니다.
    visited = [False] * (n + 1)

    # 시작위치에는 dist값을 0으로 설정
    dist[x] = 0

    # O(|V|^2) 다익스트라 코드
    for i in range(1, n + 1):
        # V개의 정점 중 
        # 아직 방문하지 않은 정점 중
        # dist값이 가장 작은 정점을 찾아줍니다.
        min_index = -1
        for j in range(1, n + 1):
            if visited[j]:
                continue
            
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j

        # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
        visited[min_index] = True

        # 최솟값에 해당하는 정점에 연결된 간선들을 보며
        # 시작점으로부터의 최단거리 값을 갱신해줍니다.
        for j in range(1, n + 1):
            # 간선이 존재하지 않는 경우에는 넘어갑니다.
            if graph[min_index][j] == 0:
                continue

            dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])


# 그래프를 인접행렬로 표현
for a, b, c in edges:
    graph1[a][b] = c

# 1차 다익스트라 진행 (x번 정점에서 i번 정점으로 가는 최단거리)
dijkstra(dist1, graph1)

# 주어진 그래프에서
# 간선을 전부 뒤집어준 뒤
# 다시 다익스트라를 진행합니다.
# 이렇게 되면
# 마치 i번 정점에서 x번 정점으로 가는 각각의 최단거리가 구해지는
# 효과를 얻을 수 있게 됩니다.
for a, b, c in edges:
    graph2[b][a] = c

dijkstra(dist2, graph2)

# 각 정점에 대해 왕복 거리를 계산한 뒤
# 이 중 최댓값을 계산합니다.
for i in range(1, n + 1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)