#class as queue 

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

#creating a queue

queue = []

#enqueue

queue.append('Q')
queue.append('U')
queue.append('E')
queue.append('U')
queue.append('E')
print(queue)

#peek

front = queue[0]
print("Peek = ", front)

#dequeue

pop = queue.pop(0)
print("Dequeue = ",pop)
print("Queue after dequeue: ", queue)

#isempty

isEmpty = not bool(queue)
print("IsEmpty: ", isEmpty)

#size

print("Size: ", len(queue))