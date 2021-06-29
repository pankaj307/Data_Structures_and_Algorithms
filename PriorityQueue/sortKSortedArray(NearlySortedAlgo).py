import heapq

arr = [2,6,3,12,56,8]
arr = [6,5,3,2,8,10,9]
k = 3
if k >= len(arr):
    k = len(arr)-1
n = len(arr)
pq = []

for i in range(k+1):
    heapq.heappush(pq, arr[i])
print(pq)

index = 0
for i in range(k+1, n):
    arr[index] = heapq.heappop(pq)
    index += 1
    heapq.heappush(pq, arr[i])
print(arr)
print(pq, index)

while len(pq) != 0:
    arr[index] = heapq.heappop(pq)
    index += 1

print(pq)
print('Final array',arr)