class Account:
    balance = 0

    def checkBalance(self, pin):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
