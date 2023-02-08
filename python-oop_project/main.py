from item import Item
from phone import Phone

Item.instance_from_csv()

for item in Item.all:
    print(item.name)
