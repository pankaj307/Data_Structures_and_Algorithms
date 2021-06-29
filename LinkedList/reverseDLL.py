import my_DLL

def reverse(head):
    if head == None or head.next == None:
        return head
    prev = None
    cur = head
    while cur:
        prev = cur.prev
        cur.prev = cur.next
        cur.next = prev
        cur = cur.prev
    return prev.prev

l1 = my_DLL.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.head = reverse(l1.head)
l1.printList()