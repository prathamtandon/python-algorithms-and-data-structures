class Stack:

    def __init__(self):
        self.top = -1
        self.stack = []

    def empty(self):
        return self.top == -1

    def push(self, x):
        self.top += 1
        self.stack.append(x)

    def peek(self):
        if(self.empty()):
            raise Exception("underflow")
        else:
            return self.stack[self.top]

    def pop(self):
        if(self.empty()):
            raise Exception("underflow")
        else:
            self.top -= 1
            return self.stack[self.top + 1]

