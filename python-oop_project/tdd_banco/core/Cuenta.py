class Cuenta:
    def __init__(self, name: str, ammount=0):
        self.name = name
        self.ammount = ammount

    def update_money(self, money: float):
        if not isinstance(money, (int, float)):
            raise ValueError("money must be a float")

        self.ammount += money

    def withdraw_cash(self, money: float):
        if not isinstance(money, (int, float)):
            raise ValueError("money must be a float")

        if money > self.ammount:
            raise Exception("Imposible cash amount")

        self.ammount -= money
        
