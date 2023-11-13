n = int(input())

arr = []
for _ in range(n):
    s, e = input().split()
    arr.append((int(e), int(s)))
    
arr.sort()  #끝시간이 빠른 순으로 정렬

curr_time = 0
result = 0
for (e, s) in arr:
    if s >= curr_time:
        result += 1
        curr_time = e

print(result)