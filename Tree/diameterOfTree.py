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

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def getDiameter(root):
    if root == None:
        return 0
    d1 = 1 + height(root.left) + height(root.right)
    d2 = getDiameter(root.left)
    d3 = getDiameter(root.right)
    return max(d1,d2,d3)

def height2(root):
    if root == None:
        return 0
    lh = height2(root.left)
    rh = height2(root.right)
    height2.res = max(height2.res, 1+lh+rh)
    return (1+max(lh,rh))
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

height2.res = 0
height2(root)
print(height2.res)