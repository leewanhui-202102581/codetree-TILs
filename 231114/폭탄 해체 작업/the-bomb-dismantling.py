n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x: x[1])

curr_time = 1
result = 0

for score, time_limit in arr:
    if time_limit >= curr_time:
        result += score
        curr_time += 1
    
print(result)