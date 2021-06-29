class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def treeTraversal(root):
    if root == None:
        return
    print(root.data,end=': ')
    if root.left != None:
        print('Left ->',root.left.data,end=', ')
    if root.right != None:
        print('Right ->',root.right.data,end='')
    print()
    treeTraversal(root.left)
    treeTraversal(root.right)

# # Time: O(height), Space: O(height)

def insertInBST(root,key):
    if root == None:
        return Node(key)
    if root.data < key:
        root.right = insertInBST(root.right,key)
    elif root.data > key:
        root.left = insertInBST(root.left,key)
    return root

# # Time: O(height), Space: O(1)

def insertInBST_2(root,key):
    temp = Node(key)
    parent = None
    cur = root
    while cur != None:
        parent = cur
        if cur.data > key:
            cur = cur.left
        elif cur.data < key:
            cur = cur.right
        else:
            return root
    if parent == None:
        return temp
    if parent.data > key:
        parent.left = temp
    else:
        parent.right = temp
    return root


root = None
root = Node(20)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(12)
root.left.right = Node(18)
root.left.left.left = Node(7)
root.right.right = Node(40)
root.right.right.left = Node(35)
root.right.right.right = Node(50)
root.right.right.right.right = Node(80)

treeTraversal(root)
print()

key = 70
root = insertInBST_2(root,key)

treeTraversal(root)