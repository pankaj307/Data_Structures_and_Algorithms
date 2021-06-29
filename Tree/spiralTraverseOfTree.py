class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=' ')
        printInorder(root.right)

# # Method 1: Time: O(n)

def spiralTraverse(root):
    if root == None:
        return
    queue = []
    stack = []
    rev = False
    queue.append(root)
    while len(queue) != 0:
        count = len(queue)
        for _ in range(count):
            curr = queue[0]
            queue = queue[1:]
            if rev:
                stack.append(curr.data)
            else:
                print(curr.data,end=' ')
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
        if rev:
            while len(stack) != 0:
                print(stack.pop(),end=' ')
        rev = not rev
        print()


# # Method 2 (Efficient way): Time: O(n)

def spiralTraverse2(root):
    if root == None:
        return
    s1, s2 = [], []
    s1.append(root)
    while len(s1) != 0 or len(s2) != 0:
        while len(s1) != 0:
            cur = s1.pop()
            print(cur.data,end=' ')
            if cur.left != None:
                s2.append(cur.left)
            if cur.right != None:
                s2.append(cur.right)
        while len(s2) != 0:
            cur = s2.pop()
            print(cur.data,end=' ')
            if cur.right != None:
                s1.append(cur.right)
            if cur.left != None:
                s1.append(cur.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

spiralTraverse2(root)