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
        if y[i] > x[j]:
            return 1
        else:
            i += 1
            j += 1
    if len_x < len_y:#x: 더 앞에 오는 수 : '4' vs '43'
        return -1
    elif  len_x > len_y:
        return 1
    return 0 



# 내림차순 정렬
arr.sort(key=cmp_to_key(compare))

for elem in arr: # 정렬 이후의 결과 출력
    print(elem, end="")