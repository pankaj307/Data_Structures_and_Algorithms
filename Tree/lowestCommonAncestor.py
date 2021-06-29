class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=' ')
        inOrder(root.right)

# # Time: θ(n)

def findPath(root,path,n):
    if root == None:
        return False
    path.append(root)
    if root.data == n:
        return True
    if findPath(root.left,path,n) or findPath(root.right,path,n):
        return True
    path.pop()
    return False

def lca(root,n1,n2):
    path1, path2 = [], []
    if findPath(root,path1,n1) == False or findPath(root,path2,n2) == False:
        return None
    i = 0
    while i<len(path1) and i<len(path2):
        if path1[i+1] != path2[i+1]:
            return path1[i]
        i += 1
    return None

# # Efficient way

def lca2(root,n1,n2):
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    lca1 = lca(root.left,n1,n2)
    lca2 = lca(root.right,n1,n2)
    if lca1 != None and lca2 != None:
        return root
    if lca1 != None:
        return lca1
    else:
        return lca2


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

res = lca2(root,4,5)
print(res.data)