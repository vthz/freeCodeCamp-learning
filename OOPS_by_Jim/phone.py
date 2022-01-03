from item import Item


class Phone(Item):  # inheritance

    def __init__(self, name: str, price: float, quant=0, broken_phones=0):
        # call to super function to have access to all attributes/ methods of parent
        super().__init__(
            name, price, quant
        )
        # run validation to the received arguments
        assert broken_phones >= 0, f"Broken phone should not be negative"

        # assign to self object
        self.broken_phone = broken_phones
