import heapq

arr = [1,4,5,7,11,9,2]
heapq.heapify(arr)
print(arr)

heapq.heappush(arr, 3)
print(arr)

print(heapq.heappop(arr))
print(arr)

print(heapq.heapreplace(arr, 6))
print(arr)

print()

heapq._heapify_max(arr)
print(arr)

print(heapq._heappop_max(arr))
print(arr)

print(heapq._heapreplace_max(arr, 10))
print(arr)

arr.append(11)
heapq._siftdown_max(arr, 0, len(arr)-1)
print(arr)