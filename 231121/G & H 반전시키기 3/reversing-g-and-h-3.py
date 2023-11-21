n = int(input())

string = input()
target = input()

result = 0
changing = 0


#바꾸는 중 + changing < 4 : changing += 1
# 새로 시작: 바꾸지 않는 중 or changing >= 4: changing += 1
# 바꾸는 중 + 안 바꿔도 되는 경우 :안 바꿈. 
for i in range(n):
    if changing == 0:
        if string[i] != target[i]:
            changing += 1
            result += 1
        
    if changing: #바꾸는 중이라면. 
        if string[i] == target[i]:
            changing = 0
        else:
            if changing < 4:
                changing += 1
            else:
                changing = 1
                result += 1

        

print(result)