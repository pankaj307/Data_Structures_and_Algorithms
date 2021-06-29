import myBinaryTree

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def inorderIterative(root):
    current = root
    stack = []
    # res = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack): 
            current = stack.pop()
            # res.append(current.data)
            print(current.data,end=' ')
            current = current.right  
        else: 
            break
    # return res

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

inorder(root)
print()
inorderIterative(root)