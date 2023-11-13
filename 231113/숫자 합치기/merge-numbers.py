from heapq import heappop, heappush, heapify

n = int(input())
arr = [int(a) for a in input().split()]
heapify(arr)

result = 0
while arr:
    try: 
        a = heappop(arr)
        b = heappop(arr)
    except:
        break
    result += a + b

    heappush(arr, a+b)

print(result)