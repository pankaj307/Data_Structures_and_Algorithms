import my_LinkedList

def delNode(ptr):
    temp = ptr.next
    ptr.data = temp.data
    ptr.next = temp.next
    del temp


l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)


ptr = l1.head.next.next
delNode(ptr)
l1.printList()