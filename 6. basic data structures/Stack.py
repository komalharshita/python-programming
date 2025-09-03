#using python list as stack

stack = []

#creating stack using class

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size (self):
        return len(self.stack)
    
#creating 

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')
print(myStack)
print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())


#push

stack.append('a')
stack.append('b')
stack.append('c')
print("Stack: ", stack)

#peek

topelement = stack[-1]
print("Peek =", topelement)

#pop

popelement = stack.pop()
print("Pop= ", popelement)
print("Stack after pop = ", stack)

#size

print("Size of stack = ", len(stack))

#other operations

isEmpty = not bool(stack)
print("Is stack empty? : ", isEmpty)