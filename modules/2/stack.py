class Stack:
    def __init__(self, size):
        self.stack = []
        if size < 0:
            size = 0
        self.size = size

    def push(self, n):
        if len(self.stack) < self.size:
            self.stack.append(n)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(-1)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.size

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def __str__(self):
        s = "["
        for i in range(len(self.stack)):
            s += str(self.stack[i])+", "
        return s+"]"

if __name__ == "__main__":
    print("You are trying to run a module!")
