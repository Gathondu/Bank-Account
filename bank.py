class Bank(object):

    def account():
        pass

    def deposit():
        pass

    def withdraw():
        pass


class CurrentAccount(Bank):

    def __init__(self):
        self.amount = 500

    def deposit(self, amnt):
        if amnt > 0:
            self.amount += amnt

    def withdraw(self, amnt):
        if amnt > 0 and (self.amount - amnt) >= 500:
            self.amount -= amnt

    def withdraw_limit(self):
        result = self.amount - 500
        if result > 0:
            return result
        else:
            return 0


class SavingAccount(Bank):

    def __init__(self):
        self.amount = 0

    def deposit(self, amnt):
        if amnt > 0:
            self.amount += amnt

    def withdraw(self, amnt):
        if self.amount - amnt >= 0:
            self.amount -= amnt
        else:
            return "You cannot withdraw beyond minimum balance"

