n, k = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

idx = n-1
cnt = 0
while k > 0:
    cnt += k // arr[idx] 
    k = k % arr[idx]
    idx -= 1

print(cnt)