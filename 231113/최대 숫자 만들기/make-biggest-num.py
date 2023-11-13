from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]


# x가 앞, y가 뒤 가정/원하는 순서: -1 / 반대 순서: 1/ 동일 우선순위:
def compare(x, y):
    len_x = len(x)
    len_y = len(y)
    i, j = 0, 0
    while i < len_x and j < len_y:
        if x[i] > y[j]: #x: 더 앞에 오는 수
            return -1
        if y[j] > x[i]:
            return 1
        else:
            i += 1
            j += 1

    while i < len_x: 
        j = -1
        if x[i] > y[j]: #x: 더 앞에 오는 수
            return -1
        if y[j] > x[i]:
            return 1
        else:
            i += 1
    
    while j < len_y:
        i = -1
        if x[i] > y[j]: #x: 더 앞에 오는 수
            return -1
        if y[j] > x[i]:
            return 1
        else:
            j += 1

    return 0 



# 내림차순 정렬
arr.sort(key=cmp_to_key(compare))

for elem in arr: # 정렬 이후의 결과 출력
    print(elem, end="")