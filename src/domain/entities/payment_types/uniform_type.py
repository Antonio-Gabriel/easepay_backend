from decimal import Decimal


class UniformType:
    def __init__(self, price: Decimal, type_uniform: str, id: int = None):
        self.id = id
        self.price = price
        self.type_uniform = type_uniform
