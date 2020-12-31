def factorial_while(num):
    n = num
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print("Factorial of %d using WHILE loop: %d"%(num, fact))

def factorial_for(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("Factorial of %d using FOR loop: %d"%(num, fact))

def factorial_do_while(num):
    fact = 1
    n = num
    while True:
        if n <= 0:
            break
        fact *= n
        n -= 1
    print("Factorial of %d using EMULATED DO WHILE loop: %d"%(num, fact))
    
n = int(input("Enter a number: "))
factorial_while(num=n)
factorial_for(num=n)
factorial_do_while(num=n)