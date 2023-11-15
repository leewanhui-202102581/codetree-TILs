from heapq import heappop, heappush
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: (-x[1], -x[0]))

#print(arr) #조건1: 시간제한이 가장 여유로운 것부터 조건2: 점수가 큰 순으로
curr_time = arr[0][1]
result = 0
candidate = []
i = 0 #index
while i < n:

    while i < n and arr[i][1] >= curr_time: 
        heappush(candidate, (-arr[i][0], arr[i][1]) ) #기준1: 큰 점수 기준2: 큰 시간
        i += 1
    
    if candidate :
        minus_score, minus_time_limit = heappop(candidate)
        score, time_limit = - minus_score, - minus_time_limit
        #print(score, time_limit, curr_time)
        result += score
        curr_time -= 1
    else : 
        curr_time -= 1
    
print(result)