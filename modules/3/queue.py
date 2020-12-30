class Queue:
    def __init__(self, size):
        self.queue = []
        if size < 0:
            size = 0
        self.size = size

    def insert(self, n):
        if len(self.queue) < self.size:
            self.queue.append(n)

    def delete(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]

    def __str__(self):
        s = "["
        for i in range(len(self.queue)):
            s += str(self.queue[i])+", "
        return s+"]"

if __name__ == "__main__":
    print("You are trying to run a module!")
