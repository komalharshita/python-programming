class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popnode = self.head
        self.head = self.head.next
        self.size -= 1
        return popnode.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value 
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size 
    
    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end = " -> ")
            currentNode = currentNode.next
        print()

myStack = Stack()
myStack.push("mango")
myStack.push("apple")
myStack.push("cherry")
myStack.push("lemon")

print("Linked List: ", end="")
myStack.traverse()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("Linked List after Pop: ", end="")
myStack.traverse()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())