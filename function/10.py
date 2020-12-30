add = lambda x,y : x+y
subtract = lambda x,y : x-y
multiply = lambda x,y : x*y
divide = lambda x,y : x/y

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("%d + %d = %d"%(x, y, add(x, y)))
print("%d - %d = %d"%(x, y, subtract(x, y)))
print("%d * %d = %d"%(x, y, multiply(x, y)))
print("%d / %d = %f"%(x, y, divide(x, y)))