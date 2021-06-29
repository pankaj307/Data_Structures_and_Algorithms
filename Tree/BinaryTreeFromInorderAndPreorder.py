import myBinaryTree

def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None
    tNode = myBinaryTree.Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    if inStrt == inEnd:
        return tNode
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)
    tNode.left = buildTree(inOrder,preOrder,inStrt,inIndex-1) 
    tNode.right = buildTree(inOrder,preOrder,inIndex+1,inEnd)
    return tNode
  
def search(arr,start,end,value): 
    for i in range(start,end+1):
        if arr[i] == value:
            return i

inOrder = [20,10,40,30,50] 
preOrder = [10,20,30,40,50] 

buildTree.preIndex = 0
root = buildTree(inOrder,preOrder,0,len(inOrder)-1) 

print("Inorder traversal of the constructed tree is")
myBinaryTree.inorder(root)