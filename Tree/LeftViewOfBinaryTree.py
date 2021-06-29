import myBinaryTree

def leftView(root,level,maxLevel):
    if root == None:
        return
    if maxLevel[0] < level:
        print(root.data,end=' ')
        maxLevel[0] = level
    leftView(root.left,level+1,maxLevel)
    leftView(root.right,level+1,maxLevel)

# # Iterative solution

def leftView2(root):
    if root == None:
        return
    queue = []
    queue.append(root)
    while len(queue) != 0:
        count = len(queue)
        for i in range(count):
            current = queue[0]
            queue = queue[1:]
            if i == 0:
                print(current.data,end=' ')
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

root = myBinaryTree.Node(10)
root.left = myBinaryTree.Node(20)
root.right = myBinaryTree.Node(30)
root.right.left = myBinaryTree.Node(40)
root.right.right = myBinaryTree.Node(50)

print('Recursive solution...')
maxLevel = [0]
leftView(root,1,maxLevel)

print()

print('Iterative solution...')
leftView2(root)