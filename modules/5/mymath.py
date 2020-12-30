def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def gcd(a, b):
    if a==0: return b
    return gcd(b%a, a)

def lcm(a, b):
    hcf = gcd(a, b)
    return a*b//hcf

def sqrt(n):
    return n**(1/2)


if __name__ == "__main__":
    print("You are trying to run a module!")