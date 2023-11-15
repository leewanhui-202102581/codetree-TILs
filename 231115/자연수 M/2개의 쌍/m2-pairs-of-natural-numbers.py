n = int(input())

arr = []
m = 0
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    m += x
    for _ in range(x):
        arr.append(y)

arr.sort()

i = 0
j = m -1
max_sum = 0
while i < j:
    max_sum = max(arr[j] + arr[i], max_sum)
    i += 1
    j -= 1

print(max_sum)