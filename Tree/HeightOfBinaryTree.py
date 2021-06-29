import myBinaryTree

def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(8)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)
root.right.right.left = myBinaryTree.Node(50)

print(height(root))