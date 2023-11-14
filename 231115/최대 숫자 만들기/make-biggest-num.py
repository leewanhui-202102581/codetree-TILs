from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]


# x가 앞, y가 뒤 가정/원하는 순서: -1 / 반대 순서: 1/ 동일 우선순위:
def compare(x, y):
    xy = int(x + y)
    yx = int(y + x)

    if xy > yx:
        return -1
    elif xy < yx:
        return 1
    return 0



# 내림차순 정렬
arr.sort(key=cmp_to_key(compare))

for elem in arr: # 정렬 이후의 결과 출력
    print(elem, end="")