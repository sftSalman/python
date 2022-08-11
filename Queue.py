class Queue:
    def __init__(self):
        self.queue = list()
    def add(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def size(self):
        return len(self.queue)


    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ('no element')

q = Queue()
q.add('salman')
q.remove()

print(q.size())
print(q.remove())
print(q)

