import mymath

n = int(input("Enter a number to find factorial: "))
print("%d! = %d"%(n, mymath.factorial(n)))

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD of %d, %d = %d"%(a, b, mymath.gcd(a, b)))
print("LCM of %d, %d = %d"%(a, b, mymath.lcm(a, b)))

n = int(input("Enter a number to find square root: "))
print("Square root of %d is %f"%(n, mymath.sqrt(n)))
