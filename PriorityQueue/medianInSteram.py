import heapq

arr = [25, 7, 10, 15, 20]
n = len(arr)

left = []
right = []

res = []
res.append(arr[0])

if n == 1:
    print(arr)
elif n == 2:
    res.append(sum(arr)/2)
    print(sum(arr)/2)

else:
    for i in range(n):
        if i == 0:
            left.append(arr[i])
            heapq._siftdown_max(left, 0, len(left)-1)
        elif i == 1:
            if arr[i] < left[0]:
                t = left[0]
                left[0] = arr[i]
                right.append(t)
            else:
                right.append(arr[i])
            heapq._siftdown_max(left, 0, len(left)-1)
            heapq.heapify(right)
            res.append((left[0]+right[0])/2)
        else:
            if (i+1)%2 == 1:
                print('-->', arr[i])
                if arr[i] < right[0]:
                    left.append(arr[i])
                    heapq._siftdown_max(left, 0, len(left)-1)
                else:
                    t = heapq.heappop(right)
                    left.append(t)
                    heapq._siftdown_max(left, 0, len(left)-1)
                    heapq.heappush(right, arr[i])
                res.append(left[0])
            else:
                if arr[i] > left[0]:
                    heapq.heappush(right, arr[i])
                else:
                    t = heapq._heappop_max(left)
                    left.append(arr[i])
                    heapq._siftdown_max(left, 0, len(left)-1)
                    heapq.heappush(right, t)
                res.append((left[0]+right[0])/2)
        print(left, right)
    print(res)