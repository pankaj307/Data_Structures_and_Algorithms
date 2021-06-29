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

def countNode(root):
    leftHeight, rightHeight = 0, 0
    cur = root
    while cur != None:
        leftHeight += 1
        cur = cur.left
    cur = root
    while cur != None:
        rightHeight += 1
        cur = cur.right
    if leftHeight == rightHeight:
        return (2**leftHeight)-1
    return 1+countNode(root.left)+countNode(root.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
root.left.left.left = Node(80)
root.left.left.right = Node(90)
root.left.right.left = Node(100)
root.left.right.right = Node(110)
root.right.left.left = Node(120)

print(countNode(root))