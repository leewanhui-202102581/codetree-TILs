n = int(input())
arr = [int(a) for a in input().split()]

arr_sum = 0
result = -1000
for i in range(n):
    if arr[i] + arr_sum >= 0:
        arr_sum += arr[i]
    else: 
        arr_sum = 0
    
    result = max(result, arr_sum)

print(result)