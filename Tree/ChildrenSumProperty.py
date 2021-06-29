import myBinaryTree

def childernSum(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    sm = 0
    if root.left != None:
        sm += root.left.data
    if root.right != None:
        sm += root.right.data
    return root.data == sm and childernSum(root.left) and childernSum(root.right)


root = myBinaryTree.Node(20)
root.left = myBinaryTree.Node(8)
root.right = myBinaryTree.Node(12)
root.left.left = myBinaryTree.Node(3)
root.left.right = myBinaryTree.Node(5)

print(childernSum(root))