import myBinaryTree

def printKDist(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data,end=' ')
    else:
        printKDist(root.left,k-1)
        printKDist(root.right,k-1)

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.left.left = myBinaryTree.Node(40)
root.left.right = myBinaryTree.Node(50)
root.right.right = myBinaryTree.Node(70)
root.right.right.right = myBinaryTree.Node(80)

printKDist(root,2)