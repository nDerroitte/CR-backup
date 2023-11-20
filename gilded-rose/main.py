# -*- coding: utf-8 -*-
from __future__ import print_function

from modules.gilded_rose import Item, GildedRose

if __name__ == "__main__":
    items = [
        Item(name="Sulfuras", sell_in=5, quality=5),
        Item(name="Dexterity", sell_in=5, quality=5),
        Item(name="Cake", sell_in=5, quality=5), 
        Item(name="Elixir", sell_in=5, quality=5),
        Item(name="TAFKAL", sell_in=-5, quality=5),
        Item(name="TAFKAL", sell_in=5, quality=5),
        Item(name="TAFKAL", sell_in=10, quality=5),
        Item(name="TAFKAL", sell_in=15, quality=5),
        Item(name="Brie", sell_in=-5, quality=5),
        Item(name="Brie", sell_in=5, quality=5), 
    ]

    days = 2
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()  
