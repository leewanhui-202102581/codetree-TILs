from heapq import heappop, heappush
n, m = tuple(map(int, input().split()))

arr = [ ] 
for _ in range(n):
    w, v = tuple(map(int, input().split()))
    heappush(arr, (-v/w, w, v)) #내림차순으로

result = 0
while m > 0:
    try: 
        v_per_w, w, v = heappop(arr)
        v_per_w = - v_per_w
    except:
        break

    if m >= w:
        m -= w
        result += v_per_w * w
    else:
        result += (v_per_w * m)
        m = 0

    
print(f'{result:.3f}')