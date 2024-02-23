from unittest import TestCase

from Bank_App.Account1 import Account


class Account1(TestCase):




    def test_that_account_has_0_balance(self):
        account = Account()
        self.assertEqual(0, account.checkBalance("2222"))


    def test_that_accout_can_deposit(self):
        account = Account()
        self.assertEqual(0, account.checkBalance("2222"))
        account.deposit(2_000)
        self.assertEqual(2_000, account.checkBalance("2222"))

    def test_that_accout_can_deposit_5000_withdraw_3000(self):
        account = Account()
        self.assertEqual(0, account.checkBalance("2222"))
        account.deposit(5_000)
        account.withdraw(3_000)
        self.assertEqual(2_000, account.checkBalance("2222"))

    def test_that_accout_can_deposit_5000_withdraw_(self):
        account = Account()
        self.assertEqual(0, account.checkBalance("2222"))
        account.deposit(2_000)
        self.assertEqual(2_000, account.checkBalance("2222"))

