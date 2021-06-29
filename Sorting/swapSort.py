for _ in range(1):
    n = 5
    arr = [2,3,1,5,1]

    i = 0
    while i < n:
        if arr[i] != arr[arr[i]-1]:
            arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
        else:
            i += 1
    print(arr)

    for i in range(len(arr)):
        if arr[i] != i+1:
            print('Duplicate -->',arr[i],'Missing -->',i+1)
            break