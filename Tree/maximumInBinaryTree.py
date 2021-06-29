import myBinaryTree

def getMax(root):
    if root == None:
        return float('-inf')
    return max(root.data, getMax(root.left), getMax(root.right))

root = myBinaryTree.Node(20)
root.left = myBinaryTree.Node(80)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

print(getMax(root))