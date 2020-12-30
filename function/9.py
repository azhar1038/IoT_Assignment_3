swap = lambda x, y : (y,x)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x, y = swap(x, y)
print("First number:", x)
print("Second number:", y)