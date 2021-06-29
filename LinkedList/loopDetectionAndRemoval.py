import my_LinkedList

def detectRemoveLoop(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None



l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)

l1.head.next.next.next.next = l1.head.next

detectRemoveLoop(l1.head)
l1.printList()