import myBinaryTree

def getWidth(root):
    if root == None:
        return 0
    queue = []
    queue.append(root)
    res = 0
    while len(queue) != 0:
        c = len(queue)
        res = max(res,c)
        for _ in range(c):
            current = queue[0]
            queue = queue[1:]
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
    return res


root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(8)
root.right = myBinaryTree.Node(30)
root.left.left = myBinaryTree.Node(2)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

print(getWidth(root))