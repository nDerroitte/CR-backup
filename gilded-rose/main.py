# -*- coding: utf-8 -*-
from __future__ import print_function

from module.gilded_rose import *

if __name__ == "__main__":
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6), 
    ]

    days = 2
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
        print(items)

    itemsFactoryValue = [
        ItemFactory.create_item("Regular Item", 5, 10),
        ItemFactory.create_item("Aged Brie", 3, 10),
        # ... add more items as needed
    ]

    # Create a GildedRose instance with initial items
    gilded_rose = GildedRose(itemsFactoryValue)

    # Update the quality
    gilded_rose.update_quality()

    # Access the updated items directly from the instance
    updated_items = gilded_rose.items

    # Perform further checks or print the updated items
    for updated_item in (updated_items):

        print(updated_item.name, updated_item.quality, updated_item.sell_in)