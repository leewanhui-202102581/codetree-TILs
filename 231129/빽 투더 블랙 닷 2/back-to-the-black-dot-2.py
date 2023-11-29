import sys
import heapq



INT_MAX = sys.maxsize


n, m = tuple(map(int, input().split()))

red1, red2 = tuple(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
edges = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(m):
    x, y, z = edges[i]
    graph[x].append((y, z))
    graph[y].append((x, z))




def Dijkstra(k):#시작점
    pq = []
    dist = [INT_MAX] * (n + 1)

    dist[k] = 0

    # (거리, 정점 번호) 형태로 넣어줘야 합니다.
    heapq.heappush(pq, (0, k)) # 우선순위 큐에 시작점/ 거리에 가까운 곳이 먼저 나와야

    while pq:
        min_dist, min_index = heapq.heappop(pq)

        if min_dist != dist[min_index]:
            continue


        for target_index, target_dist in graph[min_index]:
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))


    return dist


red1_dist = Dijkstra(red1)
red2_dist = Dijkstra(red2)

result = INT_MAX
for i in range(1, n+1):
    if i == red1 or i == red2:
        continue
    result = min(result, red1_dist[i] + red1_dist[red2] + red2_dist[i])

print(result if result < INT_MAX else -1)