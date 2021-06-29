class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# # Time: O(height), Space: O(1)

def floorInBST(root,key):
    res = None
    while root != None:
        if root.data == key:
            return root
        elif root.data > key:
            root = root.left
        else:
            res = root
            root = root.right
    return res


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


key = 55
res = floorInBST(root,key)
if res != None:
    print(res.data)
else:
    print(res)