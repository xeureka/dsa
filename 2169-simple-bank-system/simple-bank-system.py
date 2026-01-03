class Bank:

    def __init__(self, balance):
        self.balance = balance

    def transfer(self, account1, account2, money):
        if self.in_range(account1) and self.in_range(account2) and self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account, money):
        if self.in_range(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account, money):
        if self.in_range(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False

    def in_range(self, account):
        return 1 <= account <= len(self.balance)
