class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0] if not self.is_empty() else None


q = Queue()
q.enqueue('First')
q.enqueue('Second')
print(q.dequeue())
