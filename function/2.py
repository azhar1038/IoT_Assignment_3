def is_armstrong(number):
    n = len(number)
    summed = sum([int(i)**n for i in number])
    return True if int(number) == summed else False

num = input("Enter a number to check Armstrong: ")
if is_armstrong(number=num): print(num, "is Armstrong")
else: print(num, "is not Armstrong")