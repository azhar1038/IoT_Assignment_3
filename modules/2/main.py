from stack import Stack

size = int(input("Enter size of stack: "))
s = Stack(size)
for i in range(20):
    n = int(input("Enter number_%d: "%(i+1)))
    if not s.isFull():
        s.push(n)
        print(n, "pushed into stack")
    else:
        print("Stack is already full")

elm = int(input("Enter element to search: "))
if s.peek() == elm:
    print(elm, "is in the top of stack")
else:
    print(elm, "is not in the top of stack")

for i in range(5):
    if not s.isEmpty():
        elm = s.pop()
        print(elm, "popped off stack")
    else:
        print("Stack is empty")

print("Remaining Elements:", s)
