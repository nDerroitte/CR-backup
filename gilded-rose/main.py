# -*- coding: utf-8 -*-
from __future__ import print_function

from modules.gilded_rose import GildedRose, Item

if __name__ == "__main__":
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=7),
        Item(name="Apple", sell_in=999, quality=12),
        Item(name="Peer", sell_in=-2350, quality=48),
        Item(name="Banana", sell_in=78, quality=45),
        Item(name="Conjured", sell_in=5, quality=36)
    ]

    days = 10
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
