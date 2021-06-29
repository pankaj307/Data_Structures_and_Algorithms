import myBinaryTree


# # Not completed

prev = None
def BTtoDLL(root,prev):
    if root == None:
        return root
    head = BTtoDLL(root.left,prev)
    if prev == None:
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    BTtoDLL(root.right,prev)
    return head



root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(8)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

head = BTtoDLL(root,prev)