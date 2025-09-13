# 🏦 Real‑world example: BankAccount class

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            return "Cannot deposit a negative amount."
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount < 0:
            return "Cannot withdraw a negative amount."
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds!"

if __name__ == "__main__":
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 500)

    print(acc1.deposit(200))
    print(acc2.withdraw(100))
    print(acc1.withdraw(5000))  # Not enough money