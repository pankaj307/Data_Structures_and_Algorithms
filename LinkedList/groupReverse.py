import my_LinkedList

def groupReverseRecursive(head,k):
    cur = head
    nxt = None
    prev = None
    c = 0
    while cur and c<k:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        c += 1
    if nxt:
        restHead = groupReverseRecursive(nxt,k)
        head.next = restHead
    return prev


def groupReverse(head,k):
    cur = head
    prevFirst = None
    firstPass = True
    while cur:
        first = cur
        prev = None
        c = 0
        while cur and c<k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            c += 1
        if firstPass:
            head = prev
            firstPass = False
        else:
            prevFirst.next = prev
        prevFirst = first
    return head




l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.insert(60)
l1.insert(70)


l1.head = groupReverse(l1.head,3)
l1.printList()