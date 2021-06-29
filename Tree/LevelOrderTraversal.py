import myBinaryTree

def levelOrder(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    queue.append(None)
    while len(queue) > 1:
        current = queue[0]
        queue = queue[1:]
        if current == None:
            print()
            queue.append(None)
            continue
        print(current.data,end=' ')
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)


# #-------------------------------------------------------

# # Method 2


def levelOrder2(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) != 0:  
        count = len(queue)
        for _ in range(count):
            cur = queue[0]
            queue = queue[1:]
            print(cur.data,end=' ')
            if cur.left != None:
                queue.append(cur.left)
            if cur.right != None:
                queue.append(cur.right)
        print()




root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.left.left = myBinaryTree.Node(40)
root.left.right = myBinaryTree.Node(50)
root.right.right = myBinaryTree.Node(60)

levelOrder2(root)