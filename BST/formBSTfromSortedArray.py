class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def formBST(arr):
    temp = len(arr)
    if temp == 0:
        return None
    if temp == 1:
        return Node(arr[0])
    m = temp//2
    root = Node(arr[m])
    root.left = formBST(arr[:m])
    root.right = formBST(arr[m+1:])
    return root

# root = treeInput()
# showTree(root)

arr = [1,2,3,4]
root = formBST(arr)
showTree(root)