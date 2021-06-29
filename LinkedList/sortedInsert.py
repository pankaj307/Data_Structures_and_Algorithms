import my_LinkedList

def sortedIN(cur,key):
    newNode = my_LinkedList.Node(key)
    if key < cur.data:
        newNode.next = cur
        return newNode
    curr = cur
    while curr.next and curr.next.data < key:
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return cur

l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)

l1.head = sortedIN(l1.head,111)

l1.printList()