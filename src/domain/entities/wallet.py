class Wallet:    
    def __init__(self, amount: float = 0, id: int = None):
        self.id = id
        self.amount = amount
    
    def deposit(self, amount_to_deposit: float):
        """ Add ammount to the wallet"""

        self.amount += amount_to_deposit
        return self.amount

    def with_draw(self, amount_to_withdraw: float):
        """ remove amount to the wallet"""

        self.amount -= amount_to_withdraw
        return self.amount
