class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def serialize(root,arr):
    if root == None:
        arr.append(-1)
        return
    arr.append(root.data)
    serialize(root.left,arr)
    serialize(root.right,arr)

def deserialize(arr):
    if deserialize.index == len(arr):
        return None
    val = arr[deserialize.index]
    deserialize.index += 1
    if val == -1:
        return None
    root = Node(val)
    root.left = deserialize(arr)
    root.right = deserialize(arr)
    return root


root = Node(10)
root.left = Node(20)
root.right = Node(30)

arr = []
serialize(root,arr)
print(arr)

deserialize.index = 0
newRoot = deserialize(arr)

inorder(newRoot)