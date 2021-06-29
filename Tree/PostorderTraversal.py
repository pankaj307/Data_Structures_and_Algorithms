import myBinaryTree

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')

def postorderIterative(root):
    temp = root
    visited = set()
    # res = []
    while (temp and temp not in visited):
        if (temp.left and temp.left not in visited):
            temp = temp.left
        elif (temp.right and temp.right not in visited):
            temp = temp.right
        else:
            # res.append(temp.data)
            print(temp.data,end=' ')
            visited.add(temp)
            temp = root
    # return res

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

postorder(root)
print()
postorderIterative(root)