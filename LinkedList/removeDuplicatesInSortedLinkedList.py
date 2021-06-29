import my_LinkedList

def removeDuplicates(l1):
    cur = l1.head
    while cur and cur.next:
        if cur.data == cur.next.data:
            temp = cur.next
            cur.next = cur.next.next
            del temp
        else:
            cur = cur.next



l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(20)
l1.insert(30)
l1.insert(30)
l1.insert(30)

removeDuplicates(l1)
l1.printList()