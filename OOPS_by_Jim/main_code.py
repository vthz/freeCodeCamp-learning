# video tutorial-https://www.youtube.com/watch?v=Ej_02ICOIgs

from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
item1.name = "OtherName"
print(item1.name)

# classes have two types of attributes
# -Instance attribute: it belongs to instance
# -Class attributes: it belongs to class


# item1 = Item("Phone", 100, 5)
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item("Laptop", 1000, 3)
# item2.has_numPad = False

# print(item1.name, item1.price, item1.quant)
# print(item2.name, item2.price, item2.quant)

# print(Item.__dict__)  # all attribute at class level
# print(item1.__dict__)  # all attribute at instance level

"""
item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)"""

"""
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)  # for making output of this line friendly, we can use __repr__
for i in Item.all:
    print(i.name)

Item.instantiate_from_csv()
print(Item.all)
"""
