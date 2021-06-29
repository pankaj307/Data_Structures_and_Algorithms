import my_LinkedList

l1 = my_LinkedList.LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)



print("Iterative print")
def printElements(l1):
    currentHead = l1.head
    while currentHead:
        print(currentHead.data)
        currentHead = currentHead.next
printElements(l1)


print()
print('Recursive print')
def printRecursive(currentHead):
    if currentHead is None:
        return
    print(currentHead.data)
    printRecursive(currentHead.next)
printRecursive(l1.head)