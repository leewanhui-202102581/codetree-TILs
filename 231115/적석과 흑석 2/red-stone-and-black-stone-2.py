c, n = tuple(map(int, input().split()))

red_stone = [int(input()) for _ in range(c)]
black_stone = [tuple(map(int, input().split())) for _ in range(n)]

red_stone.sort()
black_stone.sort()

idx = 0 #black 인덱스
result = 0
for red in red_stone:
    if idx == n:
        break
    #if black_stone[idx][0] > red:
    #    pass

    if red > black_stone[idx][1]:
        idx += 1
    if idx < n and (black_stone[idx][0] <= red <= black_stone[idx][1]): 
        result += 1
        idx += 1

print(result)