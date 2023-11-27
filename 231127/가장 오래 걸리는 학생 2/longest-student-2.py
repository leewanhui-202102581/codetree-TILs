import heapq
import sys

INT_MAX = sys.maxsize


n, m = tuple(map(int, input().split()))
k = n

graph = [[] for _ in range(n + 1)]
pq = []

dist = [INT_MAX] * (n + 1)


edges = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(m):
    x, y, z = edges[i]
    graph[y].append((x, z))

#시작점
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

result = 0

for i in range(1, n + 1):
    if result < dist[i]:
        result += dist[i]

print(result)


#행렬로 구할 경우 메모리 초과...
#import sys
#
#INT_MAX = sys.maxsize
#
#n, m = tuple(map(int, input().split()))
#
#edges = [tuple(map(int, input().split())) for _ in range(m)]
#
#graph = [
#    [0] * (n + 1)
#    for _ in range(n + 1)
#]
#visited = [False] * (n + 1)
#
#dist = [INT_MAX] * (n + 1) 
#
#
#for i in range(m):
#    x, y, z = edges[i]
#    graph[y][x] = z
#
#
#dist[n] = 0
#
#
#for i in range(1, n + 1):
#    min_index = -1
#    for j in range(1, n + 1):
#        if visited[j]:
#            continue
#        
#        if min_index == -1 or dist[min_index] > dist[j]:
#            min_index = j
#
#    visited[min_index] = True
#
#
#    for j in range(1, n + 1):
#        if graph[min_index][j] == 0:
#            continue
#
#        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])
#
#
#dist[0] = 0 #0 제외 위함
#print(max(dist))
#
#