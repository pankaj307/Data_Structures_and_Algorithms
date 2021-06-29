import my_LinkedList

def printMiddle(l1):
    if l1.head is None:
        print('Linked List is Empty.')
        return
    slow = l1.head
    fast = l1.head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)


l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)

printMiddle(l1)