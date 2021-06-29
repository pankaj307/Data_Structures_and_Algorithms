class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def showTree(root):
    if root == None:
        return None
    print(root.data, end=': ')
    if root.left != None:
        print('L ->', root.left.data, end=', ')
    if root.right != None:
        print('R ->', root.right.data,end=' ')
    print()
    showTree(root.left)
    showTree(root.right)


import queue
def treeInput():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)
    while not(q.empty()):
        curNode = q.get()
        print('Enter left child of', curNode.data)
        leftChild = int(input())
        if leftChild != -1:
            curNode.left = Node(leftChild)
            q.put(curNode.left)
        print('Enter right child of', curNode.data)
        rightChild = int(input())
        if rightChild != -1:
            curNode.right = Node(rightChild)
            q.put(curNode.right)
    return root



# # Method 1
# # Time: O(n log(n)) {if Tree is complete tree}
# # Time: O(n^2) {if Tree is skewed}

def maxTree(root):
    if root == None:
        return float('-inf')
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)

def minTree(root):
    if root == None:
        return float('inf')
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)

def isBST(root):
    if root == None:
        return True
    
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.data <= leftMax:
        return False
    
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST



# # Method 2
# # Time: O(n)

def isBST2(root):
    if root == None:
        return float('inf'), float('-inf'), True
    
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isRightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximum = max(leftMax, rightMax, root.data)
    isTreeBST = True
    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False
    return minimum, maximum, isTreeBST


# # Method 3

def isBST3(root, mn_range, mx_range):
    if root == None:
        return True
    if root.data < mn_range or root.data > mx_range:
        return False
    isLeftWithinConstraints = isBST3(root.left, mn_range, root.data-1)
    isRightWithinConstraints = isBST3(root.right, root.data, mx_range)
    return isLeftWithinConstraints and isRightWithinConstraints

root = Node(10)
root.left = Node(5)
root.right = Node(15)   
root.left.left = Node(3)
root.left.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(18)

# showTree(root)
# root = formBST([1,2,3,4,5,6,7,8])
# showTree(root)

root = treeInput()
print(isBST2(root))