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

def getSuccesor(cur):
    cur = cur.right
    while cur != None and cur.left != None:
        cur = cur.left
    return cur

# # Time: O(height), Space: O(height)

def deleteInBST(root,key):
    if root == None:
        return None
    if root.data > key:
        root.left = deleteInBST(root.left,key)
    elif root.data < key:
        root.right = deleteInBST(root.right,key)
    else:
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        else:
            succ = getSuccesor(root)
            root.data = succ.data
            root.right = deleteInBST(root.right,succ.data)
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

key = 20
root = deleteInBST(root,key)

treeTraversal(root)