n = int(input())
arr = [int(a) for a in input().split()]

arr_sum = arr[0]
result = arr[0]
for i in range(1, n):
    if arr_sum + arr[i] >= 0: #현재 원소를 더했을 때 합이 양수라면
        arr_sum += arr[i]
        result = max(result, arr_sum)

    elif arr[i] > result: #현재 원소를 더했을 때 음수지만, 이전의 합보다 현재 원소가 크다면
        arr_sum = arr[i]
        result = max(result, arr_sum)

    else: arr_sum = 0 #현재 원소를 더했을 때 음수이고, 이전의 합보다 현재 원소가 작다면 "초기화"
        #    result = max(result, arr_sum) 0은 원소가 아니므로 result에 저장하면 안 됨

print(result)