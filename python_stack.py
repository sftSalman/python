class Stack:
    def __init__(self):
        self.stack = []
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def look(self):
        return self.stack[-1]


    def reomve(self):
        if len(self.stack)<=0:
            return print('no element in the array')
        else:
            return self.stack.pop()


a = Stack()
a.add('salman')
a.add('farshi')
a.add('taufique')
print(a.look())
print(a.reomve())
