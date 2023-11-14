n = int(input())

arr = [True for _ in range(2 * n + 1)] #A가 낼 수 있는 카드의 목록: True
arr[0] = False
B = []
for _ in range(n):
    b = int(input())
    B.append(b)
    arr[b] = False


result = 0
for b in B:
    a = (b + 1) // (2 * n )#a는 최소 b보다 1 이상 큰 카드를 내야 함
    #if b == 2 * n:
    #    a = 0

    while a <= 2 * n:
        if arr[a]:
            break
        else:
            a += 1

    if a == 2 * n + 1: #만약 A가 이길 수 없는 경우. 
        a = 0
        while a <= 2 * n:
            if arr[a]:
                break
            else:
                a += 1

    # 이 시점에서 A가 이번에 낼 카드가 정해짐
    arr[a] = False

    if a > b:
        result += 1

print(result)