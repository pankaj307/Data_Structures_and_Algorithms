class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def showList(self):
        if self.head != None:
            temp = self.head
            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next
        print('None')

    def makeList(self, arr):
        if len(arr) == 0:
            self.head = None
            return self.head
        self.head = Node(arr[0])
        temp = self.head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return self.head

def deleteK(head, k):
    if k == 1:
        return None
    if k == 0:
        return head
    cur = head
    c = 1
    while cur:
        if c >= k-1:
            c = 0
            if cur.next:
                cur.next = cur.next.next
            else:
                break
        cur = cur.next
        c += 1
    return head


arr = [1,2,3,4,5]
l = LinkedList()
l.makeList(arr)
l.showList()
l.head = deleteK(l.head, 3)
l.showList()