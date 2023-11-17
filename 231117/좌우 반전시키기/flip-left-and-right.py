n = int(input())
string = list(map(int, input().split()))
cnt =0


for i in range(1, n-1): #마지막 n번째 자리는 따로 처리해주기. 
    if string[i-1] == 0:
        string[i-1] = abs(string[i-1] -1)
        string[i] =   abs(string[i]  - 1)
        string[i+1] = abs(string[i+1] - 1)
        cnt += 1



if n == 1 and not string[0]:
    print(-1)
elif string[n-2] != string[n-1]:
    print(-1)
else:
    print(cnt + abs(string[n-1] -1))