n = int(input())

string = input()
target = input()

result = 0
changing = False

for i in range(n):
    if changing:
        if string[i] != target[i]:
            changing = False

        # 두 문자가 같을 때는 그냥 pass
    else:
        if string[i] == target[i]:
            changing = True
            result += 1

print(result)