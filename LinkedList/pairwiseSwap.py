import my_LinkedList

def pairwiseSwap(head):
    if head == None or head.next == None:
        return
    cur = head.next.next
    prev = head
    head = head.next
    head.next = prev
    while cur and cur.next:
        prev.next = cur.next
        prev = cur
        nxt = cur.next.next
        cur.next.next = cur
        cur = nxt
    prev.next = cur
    return head


l3 = my_LinkedList.LinkedList()
l3.insert(10)
l3.insert(20)
l3.insert(30)
l3.insert(40)
l3.insert(50)

l3.head = pairwiseSwap(l3.head)

l3.printList()