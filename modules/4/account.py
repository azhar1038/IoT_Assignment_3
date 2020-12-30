class Account:
    def __init__(self, initial=0, minimum=0):
        if minimum < 0:
            minimum = 0
        if initial < minimum:
            initial = minimum
        self.balance = initial
        self.minimum = minimum

    def deposit(self, amount):
        self.balance += amount
        print("Deposited", amount, "successfully!")

    def withdraw(self, amount):
        after = self.balance-amount
        if after >= self.minimum:
            print("Withdrawn", amount, "successfully")
            self.balance = after
        else:
            print("Insufficient balance")
    
    def check_balance(self):
        return self.balance

    def set_minimum(self, minimum):
        self.minimum = minimum

    def get_minimum(self):
        return self.minimum

if __name__ == "__main__":
    print("You are trying to run a module!")