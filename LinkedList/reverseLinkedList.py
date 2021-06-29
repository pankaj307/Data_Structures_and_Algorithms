import my_LinkedList

def reverse(l1):
    cur = l1.head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    l1.head = prev

def reverseRecursive(cur,prev):
    if cur is None:
        return prev
    nxt = cur.next
    cur.next = prev
    return reverseRecursive(nxt,cur)


l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)

print('Recursive')
l1.head = reverseRecursive(l1.head,None)
l1.printList()
print()

print('Iterative')
reverse(l1)
l1.printList()