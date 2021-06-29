class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    
    def isListEmpty(self):
        if self.head is None:
            return True
        return False

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode:
            length += 1
            currentNode = currentNode.next
        return length
    
    def insert(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.next is None:
                    break
                temp = temp.next
            temp.next = newNode
    
    def insertHead(self,data):
        newHead = Node(data)
        temp = self.head
        self.head = newHead
        newHead.next = temp
        del temp
    
    def insertAt(self,data,position):
        if (position < 0) or (position >= self.listLength()):
            print('Invalid Position')
            return
        if position == 0:
            self.insertHead(data)
            return
        newNode = Node(data)
        currentNode = self.head
        currentPosition = 0
        while currentPosition != position:
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        previousNode.next = newNode
        newNode.next = currentNode
    
    def deleteEnd(self):
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode = self.head
            while lastNode.next:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print('Linked List is already empty.')

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print('Linked List is already empty.')
    
    def deleteAt(self,position):
        if position < 0 or position >= self.listLength():
            print('Invalid Position')
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while currentPosition != position:
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1
            previousNode.next = currentNode.next
            currentNode.next = None

    def printList(self):
        if self.head is None:
            print('Linked List is empty')
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def searchNode(self,data):
        if self.isListEmpty():
            print('Linked List is empty.')
            return -1
        temp = self.head
        position = 0
        while temp:
            if temp.data == data:
                print('Element is found at position.')
                return position
            temp = temp.next
            position += 1
        print('Element is not in the Linked List.')
        return -1

# l1 = LinkedList()
# l1.insert(1)
# l1.insert(3)
# l1.insert(4)


# l2 = LinkedList()
# l2.insert(2)
# l2.insert(7)
# l2.insert(9)