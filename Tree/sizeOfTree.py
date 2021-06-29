import myBinaryTree


# # Time: O(n), Space: O(h)
def getSize(root):
    if root == None:
        return 0
    return 1 + getSize(root.left) + getSize(root.right)

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

print(getSize(root))