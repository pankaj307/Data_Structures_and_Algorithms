# # Sort an array having three types of elements


# # Dutch National Flag Algorithm OR 3-way Partitioning


# # 1. sort arrays having 0's, 1's, and 2's
# # Input: [0,1,0,2,1,2]
# # Output: [0,0,1,1,2,2]

# # 2. Three way partitioning when multiple occurances of a pivot may exists
# # Input: [2,2,1,1,10,10,20,30]   (Pivot is 2)
# # Output: [1,1,2,2,30,10,10,20]

# # 3. Partitioning around a range
# # Input: [10,5,6,3,20,9,40]    (range is 5-10)
# # Output: [3,5,6,9,10,20,40]

# # Time: O(n),  Space: O(1)

def sort(arr,n):
    low, mid, high = 0, 0, n-1
    while mid <= high:
        # # Change these conditions according to above 3 cases 
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1

arr = [0,1,2,1,1,2]
sort(arr,len(arr))
print(arr)