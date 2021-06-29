class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# # Recursive Solution
# # Time: O(height), Space: O(height)

def searchInBST(root,key):
    if root == None:
        return False
    if root.data == key:
        return True
    if root.data > key:
        return searchInBST(root.left,key)
    else:
        return searchInBST(root.right,key)

# # Iterative Solution
# # Time: O(height), Space: O(1)

def searchInBST_2(root,key):
    while root != None:
        if root.data == key:
            return True
        elif root.data < key:
            root = root.right
        else:
            root = root.left
    return False

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

key = 35
print(searchInBST(root,key))
print(searchInBST_2(root,key))