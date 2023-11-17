# -*- coding: utf-8 -*-
from __future__ import print_function

from modules.gilded_rose import 

if __name__ == "__main__":
    items = [
        Item(name="Dexterity", sell_in=10, quality=20),
        Item(name="Brie", sell_in=2, quality=0),
        Item(name="Elixir", sell_in=5, quality=7),
        Item(name="Sulfuras", sell_in=0, quality=80),
        Item(name="Sulfuras", sell_in=-1, quality=80),
        Item(name="TAFKAL", sell_in=15, quality=20),
        Item(name="TAFKAL", sell_in=10, quality=49),
        Item(name="TAFKAL", sell_in=5, quality=49),
        Item(name="Cake", sell_in=3, quality=6), 
    ]

    days = 2
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
