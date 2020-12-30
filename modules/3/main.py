from queue import Queue

size = int(input("Enter size of queue: "))
q = Queue(size)
for i in range(20):
    n = int(input("Enter number_%d: "%(i+1)))
    if not q.isFull():
        q.insert(n)
        print(n, "inserted into queue")
    else:
        print("Queue is already full")

elm = int(input("Enter element to search: "))
if q.peek() == elm:
    print(elm, "is the current element")
else:
    print(elm, "is not the current element")

for i in range(5):
    if not q.isEmpty():
        elm = q.delete()
        print(elm, "deleted from queue")
    else:
        print("Queue is empty")

print("Remaining Elements:", q)
