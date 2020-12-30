def is_palindrome(number):
    if int(number)%15 == 0:
        rev = number[::-1]
        return True if rev == number else False
    else: return False

num = input("Enter a number to check palindrome: ")
if is_palindrome(number=num):
    print(num, "is a Palindrome divisible by 3 and 5")
else:
    print(num, "is not Palindrome divisible by 3 and 5")