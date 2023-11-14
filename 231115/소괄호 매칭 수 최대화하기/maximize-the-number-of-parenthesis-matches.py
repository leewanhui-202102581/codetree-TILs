from functools import cmp_to_key

n = int(input())
arr = [input() for _ in range(n)]

def cnt_matches(string): #괄호의 가지수 반환
    string_len = len(string)
    right = [0] * string_len

    #초기값
    if string[-1] == ')':
        right[-1] = 1

    #위치별 오른쪽 괄호의 개수 누적합 
    for r in range(string_len-2, -1, -1):
        if string[r] == ')':
            right[r] = right[r+1] + 1
        else:
            right[r] = right[r+1]

    cnt = 0
    for l in range(string_len):
        if string[l] == '(':
            cnt += right[l]
    
    return cnt




# x가 앞, y가 뒤 가정/원하는 순서: -1 / 반대 순서: 1/ 동일 우선순위:
def compare(x, y):
    xy_cnt = cnt_matches(x + y)
    yx_cnt = cnt_matches(y + x)

    if xy_cnt > yx_cnt:
        return -1
    elif xy_cnt < yx_cnt:
        return 1
    return 0




arr.sort(key=cmp_to_key(compare))

print(cnt_matches(''.join(arr)))