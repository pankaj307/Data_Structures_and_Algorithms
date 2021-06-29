import my_LinkedList

def NthLast(l1,n):
    if l1.head is None:
        print('Linked List is empty.')
        return
    first = l1.head
    for _ in range(n):
        if first is None:
            print('Linked List is smaller than given n.')
            return
        first = first.next
    second = l1.head
    while first:
        second = second.next
        first = first.next
    print(second.data)


l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.insert(60)

n = 3
NthLast(l1,n)