def is_prime(n):
    if n<2: return False
    if n<4: return True
    if n%2 == 0 or n%3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
             return False
        i += 6
    return True

def fibonacci_range(start=10, end=50):
    series = []
    a=0
    b=1
    while (c:=a+b) <= end:
        a = b
        b = c
        if c >= start and is_prime(c):
            series.append(c)
    return series

i = int(input("Enter start number: "))
j = int(input("Enter end number: "))
print("All prime fibonacci numbers are: ", end="")
print(*fibonacci_range(start=i, end=j), sep=", ")