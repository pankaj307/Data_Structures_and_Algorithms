class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def showTree(root):
    if root == None:
        return None
    print(root.data, end=': ')
    if root.left != None:
        print('L ->', root.left.data, end=', ')
    if root.right != None:
        print('R ->', root.right.data,end=' ')
    print()
    showTree(root.left)
    showTree(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def inorderIterative(root):
    current = root
    stack = []
    # res = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack): 
            current = stack.pop()
            # res.append(current.data)
            print(current.data,end=' ')
            current = current.right  
        else: 
            break
    # return res

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def preorderIterative(root):
    if root is None:
        return
    stack = []
    # res = []
    stack.append(root)
    while(len(stack) > 0):
        node = stack.pop()
        # res.append(node.data)
        print(node.data,end=' ')
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    # return res

def preorderOptimized(root):
    if root == None:
        return
    stack = []
    stack.append(root)
    current = root
    while len(stack) > 0:
        while current != None:
            print(current.data,end=' ')
            if current.right != None:
                stack.append(current.right)
            current = current.left
        current = stack.pop()

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')

def postorderIterative(root):
    temp = root
    visited = set()
    # res = []
    while (temp and temp not in visited):
        if (temp.left and temp.left not in visited):
            temp = temp.left
        elif (temp.right and temp.right not in visited):
            temp = temp.right
        else:
            # res.append(temp.data)
            print(temp.data,end=' ')
            visited.add(temp)
            temp = root
    # return res


import queue
def treeInput():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)
    while not(q.empty()):
        curNode = q.get()
        print('Enter left child of', curNode.data)
        leftChild = int(input())
        if leftChild != -1:
            curNode.left = Node(leftChild)
            q.put(curNode.left)
        print('Enter right child of', curNode.data)
        rightChild = int(input())
        if rightChild != -1:
            curNode.right = Node(rightChild)
            q.put(curNode.right)
    return root