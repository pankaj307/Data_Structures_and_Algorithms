def lumuto(arr,l,h):
    pivot = arr[h]
    j = l-1
    for i in range(l,h):
        if arr[i] <= pivot:
            j+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[j+1],arr[h] = arr[h],arr[j+1]
    return j+1

def qSort_l(arr,l,h):
    if l < h:
        p = lumuto(arr,l,h)
        qSort_l(arr,l,p-1)
        qSort_l(arr,p+1,h)

arr = [8,4,7,9,3,10,5]
qSort_l(arr,0,len(arr)-1)
print(arr)

#--------------------------------------------------

def hoore(arr,l,h):
    pivot = arr[l]
    i = l-1
    j = h+1
    while True:
        i+=1
        while arr[i] < pivot:
            i+=1
        j-=1
        while arr[j] > pivot:
            j-=1
        if i >= j:
            return j
        arr[i],arr[j] = arr[j],arr[i]

def qSort_h(arr,l,h):
    if l < h:
        p = hoore(arr,l,h)
        qSort_h(arr,l,p)
        qSort_h(arr,p+1,h)

arr = [8,8,8,8]
qSort_h(arr,0,len(arr)-1)
print(arr)