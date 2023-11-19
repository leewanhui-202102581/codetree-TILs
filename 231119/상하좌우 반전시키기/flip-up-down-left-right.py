def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 0, -1, 0, 1], [0, -1, 0, 1, 0]

result = 0 
for i in range(1, n):
    for j in range(n):

        if is_range(i-1,j) and not arr[i-1][j]: #바로 윗 칸이 0이면
            result += 1
            for k in range(5):                        #자기자신 + 상하좌우 모두 바꿔주기
                nx, ny = i + dx[k], j + dy[k]
                if is_range(nx,ny):
                    arr[nx][ny] = 1 - arr[nx][ny]


print(result if sum(arr[n-1]) == n else -1) 

#아이디어: 바로 윗 칸이 0이면 바꾸자.