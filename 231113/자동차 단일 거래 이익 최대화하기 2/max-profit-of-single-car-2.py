n = int(input())
arr = [int(a) for a in input().split()]

high = [0] * n
low = [0] * n
high[-1] = arr[-1]
low[0] = arr[0]

for i in range(1, n):
    low[i] = min(arr[i], low[i-1])
for i in range(n-2, -1, -1):
    high[i] = max(arr[i], high[i+1])

result = 0
for i in range(n):
    result = max(high[i] - low[i], result)

print(result)