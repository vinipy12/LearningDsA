class Stack:

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop(-1)
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    