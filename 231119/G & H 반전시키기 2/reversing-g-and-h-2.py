n = int(input())
string = input()
target = input()


result = 0 #짝수: 원래/ 홀수: 반전된 상태



#같지 않고 원래인 경우 -> 바꿔야
#같지 않고 원래가 아닌 경우 -> 그대로 둬야
#같고 원래인 경우 -> 그대로 두어야
#같고 원래가 아닌 경우 -> 바꿔야
#배타적 연산 XOR 사용해야 함. 

for i in range(n-1, -1, -1):
    if (string[i] == target[i]) ^ (result % 2 == 0 ): 
        result += 1

print(result)