import myBinaryTree

def isBalance(root):
    if root == None:
        return 0
    leftHeight = isBalance(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalance(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight) > 1:
        return -1
    else:
        return max(leftHeight,rightHeight)+1


def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)
    h = 1 + max(lh, rh)
    if abs(lh-rh) > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False


root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(8)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

print(isBalance(root))
print(getHeightAndCheckBalanced(root))