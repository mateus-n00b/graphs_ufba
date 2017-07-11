class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop()
    def isEmpty(self):
        return len(self.queue) != 0
