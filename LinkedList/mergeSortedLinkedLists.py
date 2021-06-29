import my_LinkedList

# # Space: O(n)

def merge(l1,l2,mergedList):
    currentFirst = l1.head
    currentSecond = l2.head
    while True:
        if currentFirst is None:
            while currentSecond:
                mergedList.insert(currentSecond.data)
                currentSecond = currentSecond.next
            break
        if currentSecond is None:
            while currentFirst:
                mergedList.insert(currentFirst.data)
                currentFirst = currentFirst.next
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergedList.insert(currentFirst.data)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insert(currentSecond.data)
            currentSecond = currentSecondNext

# l1 = my_LinkedList.LinkedList()
# l1.insert(1)
# l1.insert(3)
# l1.insert(4)

# l2 = my_LinkedList.LinkedList()
# l2.insert(2)
# l2.insert(7)
# l2.insert(9)

# mergedList = my_LinkedList.LinkedList()
# merge(l1,l2,mergedList)
# del l1
# del l2
# mergedList.printList()



# # Space: O(1)
def merge_2(a,b):
    if a == None:
        return b
    if b == None:
        return a
    head = None
    tail = None
    if a.data <= b.data:
        head = a
        tail = a
        a = a.next
    else:
        head = b
        tail = b
        b = b.next
    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b = b.next
    if a == None:
        tail.next = b
    else:
        tail.next = a
    return head

l1 = my_LinkedList.LinkedList()
l1.insert(1)
l1.insert(3)
l1.insert(4)

l2 = my_LinkedList.LinkedList()
l2.insert(2)
l2.insert(7)
l2.insert(9)

l1.head = merge_2(l1.head,l2.head)
l1.printList()