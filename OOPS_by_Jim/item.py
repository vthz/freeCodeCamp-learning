import csv


class Item:
    pay_rate = 0.8  # the pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quant=0):  # python executes this, an instance is called , here Item()
        # run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quant >= 0, f"Quantity {quant} is not greater than zero"

        # assign to self object
        self.__name = name
        self.price = price
        self.quant = quant

        # actions to execute
        Item.all.append(self)

    @property  # makes things read only ENCAPSULATION
    # property decorator= read- only attribute
    def name(self):
        return self.__name

    @name.setter  # can still change the value
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long! ")
        self.__name = value

    def calculate_total_price(self, ):
        return self.price * self.quant

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        # return f"Item('{self.name}','{self.price}',{self.quant})"
        return f"{self.__class__.__name__}('{self.name}','{self.price}',{self.quant})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quant=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
