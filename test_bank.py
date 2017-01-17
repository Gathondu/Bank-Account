import unittest

from bank import CurrentAccount, SavingAccount


class TestBank(unittest.TestCase):

    def setUp(self):
        self.c = CurrentAccount()
        self.s = SavingAccount()

    def test_current_account_deposits(self):
        self.c.deposit(500)
        self.assertEqual(self.c.amount, 1000, "Invalid Deposit")

    def test_invalid_current_account_withdraw_fails(self):
        amount = self.c.amount
        self.c.withdraw(600)
        self.assertEqual(amount, 500, 'Withdraw method makes invalid withdraws')

    def test_saving_account_deposits(self):
        self.s.deposit(1500)
        self.assertEqual(self.s.amount, 1500, "Invalid Deposit")

    def test_invalid_saving_account_withdraw_fails(self):
        self.assertEqual(self.s.withdraw(5), 'You cannot withdraw beyond minimum balance', 'Withdraw method makes invalid withdraws')