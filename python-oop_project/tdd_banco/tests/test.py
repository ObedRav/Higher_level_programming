import unittest
from core.Cuenta import Cuenta

class TestAccount(unittest.TestCase):

    def test_create_account(self):
        """While a account is created the ammount need to be 0"""
        new_account = Cuenta("Josefa")
        self.assertEqual(new_account.ammount, 0)

    def test_update_ammount(self):
        """While a account is updated the ammount
        need to be the initial ammount + the deposit"""
        new_account = Cuenta("Josefa")
        new_account.update_money(100)
        self.assertEqual(new_account.ammount, 100)

    def test_withdraw_money(self):
        """While a account is withdraw the ammount
        need to be the initial ammount - the amount to retire"""
        new_account = Cuenta("Josefa")
        new_account.update_money(100)
        new_account.withdraw_cash(20)
        self.assertEqual(new_account.ammount, 80)
