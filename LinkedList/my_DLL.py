class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertHead(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def delHead(self):
        if self.head == None:
            return self.head
        if self.head.next == None:
            del self.head
            return None
        self.head = self.head.next
        self.head.prev = None
        return self.head

    def delete(self):
        if self.head == None:
            return self.head
        if self.head.next == None:
            del self.head
            return None
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None
        del cur
        return self.head
        
    def printList(self):
        node = self.head 
        if node == None:
            print("DLL is empty.")
            return
        print("Traversal in forward direction")
        while node: 
            print(node.data) 
            last = node
            node = node.next
  
        print("\nTraversal in reverse direction")
        while last:
            print(last.data)
            last = last.prev
