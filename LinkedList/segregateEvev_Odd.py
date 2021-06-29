import my_LinkedList

def segregate(head):
    es, ee, os, oe = None, None, None, None
    cur = head
    while cur:
        x = cur.data
        if x%2 == 0:
            if es == None:
                es = cur
                ee = es
            else:
                ee.next = cur
                ee = ee.next
        else:
            if os == None:
                os = cur
                oe = os
            else:
                oe.next = cur
                oe = oe.next
        cur = cur.next
    if es == None or os == None:
        return head
    ee.next = os
    oe.next = None
    return es



l1 = my_LinkedList.LinkedList()
l1.insert(17)
l1.insert(15)
l1.insert(8)
l1.insert(12)
l1.insert(10)
l1.insert(5)
l1.insert(4)

l1.head = segregate(l1.head)
l1.printList()