# # Sort an array with negative elements on left and
# #  positive on right in any order

# # Time   O(n),   Space  O(1)

def sort(arr,n):
    i, j = -1, n
    while True:
        i += 1
        while arr[i] < 0:
            i += 1
        j -= 1
        while arr[j] >= 0:
            j -= 1
        if i >= j:
            return
        arr[i],arr[j] = arr[j],arr[i]

arr = [-12,10,-10,15]
sort(arr,len(arr))
print(arr)


# # Use this for sorting array with 0's and 1's efficiently
# # Also for even and odd