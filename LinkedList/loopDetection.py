import my_LinkedList

# # This method will destroy the whole Linked List

def isLoop_1(head):
    temp = my_LinkedList.Node(1)
    cur = head
    while cur:
        if cur.next == None:
            return False
        if cur.next == temp:
            return True
        nxt = cur.next
        cur.next = temp
        cur = nxt
    return False

l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
print('Method 1')
l1.head.next.next.next.next = l1.head.next
print(isLoop_1(l1.head))
print()


# #--------------------------------------------------------

# # This will not destroy but uses extra space
# # Time: O(n), Space: O(n)

def isLoop_2(head):
    s = set()
    cur = head
    while cur:
        if cur in s:
            return True
        s.add(cur)
        cur = cur.next
    return False


l2 = my_LinkedList.LinkedList()
l2.insert(10)
l2.insert(20)
l2.insert(30)
l2.insert(40)
print('Method 2')
l2.head.next.next.next.next = l2.head.next
print(isLoop_2(l2.head))
print()


# #----------------------------------------------------------


def floyd(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False




l3 = my_LinkedList.LinkedList()
l3.insert(10)
l3.insert(20)
l3.insert(30)
l3.insert(40)
print('Method 3 Floyds\'s Cycle Detection')
l3.head.next.next.next.next = l3.head.next
print(floyd(l3.head))