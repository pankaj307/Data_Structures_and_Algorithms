import my_LinkedList

# # Method 1: Time: O(m+n), Space: O(m)
def findIntersection_1(h1,h2):
    s = set()
    cur = h1
    while cur:
        s.add(cur)
        cur = cur.next
    cur2 = h2
    while cur2:
        if cur2 in s:
            print(cur2.data)
            return
        cur2 = cur2.next

# # Method 2: Time: O(max(m,n)), Space: O(1)
def findIntersection_2(h1,h2):
    cur1 = h1
    c1 = 0
    while cur1:
        cur1 = cur1.next
        c1 += 1
    cur2 = h2
    c2 = 0
    while cur2:
        cur2 = cur2.next
        c2 += 1
    temp = abs(c1-c2)
    cur1 = h1
    cur2 = h2
    if c1 > c2:
        while temp:
            cur1 = cur1.next
            temp -= 1
    elif c1 < c2:
        while temp:
            cur2 = cur2.next
            temp -= 1
    while cur1 and cur2:
        if cur1 == cur2:
            print(cur1.data)
            return
        cur1 = cur1.next
        cur2 = cur2.next


l1 = my_LinkedList.LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.insert(60)

l2 = my_LinkedList.LinkedList()
l2.insert(35)
l2.head.next = l1.head.next.next.next

findIntersection_2(l1.head,l2.head)