class Stack():
    def __init__(self):
        self.stack = []
        self.length = 0
    def size(self):
        return self.length
    def top(self):
        if self.length > 0:
            return self.stack[self.length - 1]
        else:
            return None
    def empty(self):
        if self.length > 0:
            return 1
        return 0
    def pop(self):
        del self.stack[-1]
        self.length -= 1
    def push(self, x):
        self.stack.append(x)
        self.length += 1