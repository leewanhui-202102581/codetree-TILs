n = int(input())



cnt = n // 5
n = n % 5

#나머지가 1일 때, 3일 때,
if n == 1 or n == 4:
    print(cnt + 2) # -1 + 3
elif n == 3:
    print(cnt + 3)
elif n ==2:
    print(cnt + 1)
else: #n==0
    print(cnt)