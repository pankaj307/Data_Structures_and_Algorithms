import myBinaryTree

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def preorderIterative(root):
    if root is None:
        return
    stack = []
    # res = []
    stack.append(root)
    while(len(stack) > 0):
        node = stack.pop()
        # res.append(node.data)
        print(node.data,end=' ')
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    # return res

def preOrderOptimized(root):
    if root == None:
        return
    stack = []
    stack.append(root)
    current = root
    while len(stack) > 0:
        while current != None:
            print(current.data,end=' ')
            if current.right != None:
                stack.append(current.right)
            current = current.left
        current = stack.pop()

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

preorder(root)
print()
preorderIterative(root)
print()
preOrderOptimized(root)