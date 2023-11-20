# -*- coding: utf-8 -*-
import unittest

from main.gilded_rose import GildedRose
from main.Item import Item

import random

class GildedRoseTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        random.seed(10)
    def create_base_items(self):
        return [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=11),
            Item(name="+5 Dexterity Vest", sell_in=-1, quality=11),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=11),
            Item(name="Aged Brie", sell_in=-1, quality=11),
            Item(name="Aged Brie /Conjured /Timeless", sell_in=10, quality=10),
            Item(name="+5 Dexterity Vest /Puzzing /High_Quality", sell_in=10, quality=25)
        ]
        
    def test_1_day(self):
        items = self.create_base_items()
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        answers = [
            Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
            Item(name="Aged Brie", sell_in=1, quality=1),
            Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50),
            Item(name="Backstage passes to a TAKFAL80ETC concert", sell_in=3, quality=14),
            Item(name="+5 Dexterity Vest", sell_in=-2, quality=9),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-2, quality=0),
            Item(name="Aged Brie", sell_in=-2, quality=13),
            Item(name="Aged Brie /Conjured /Timeless", sell_in=10, quality=12),
            Item(name="+5 Dexterity Vest /Puzzing /High_Quality", sell_in=9, quality=24)
        ]

        for item, degraded in zip(gilded_rose.items, answers):
            #print(item, degraded)
            self.assertEqual(item.quality, degraded.quality)
            self.assertEqual(item.sell_in, degraded.sell_in)

    def test_2_days(self):
        items = self.create_base_items()

        answers = [
            Item(name="+5 Dexterity Vest", sell_in=8, quality=18),
            Item(name="Aged Brie", sell_in=0, quality=2),
            Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=22),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50),
            Item(name="Backstage passes to a TAKFAL80ETC concert", sell_in=2, quality=17),
            Item(name="+5 Dexterity Vest", sell_in=-3, quality=7),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-3, quality=0),
            Item(name="Aged Brie", sell_in=-3, quality=15),
            Item(name="Aged Brie /Conjured /Timeless", sell_in=10, quality=14),
            Item(name="+5 Dexterity Vest /Puzzing /High_Quality", sell_in=8, quality=23)
        ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        for item, degraded in zip(gilded_rose.items, answers):
            #print(item, degraded)
            self.assertEqual(item.quality, degraded.quality)
            self.assertEqual(item.sell_in, degraded.sell_in)

    def test_7_days(self):
        items = self.create_base_items()

        answers = [
            Item(name="+5 Dexterity Vest", sell_in=3, quality=13),
            Item(name="Aged Brie", sell_in=-5, quality=12),
            Item(name="Elixir of the Mongoose", sell_in=-2, quality=0),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=29),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-2, quality=0),
            Item(name="Backstage passes to a TAKFAL80ETC concert", sell_in=-3, quality=0),
            Item(name="+5 Dexterity Vest", sell_in=-8, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-8, quality=0),
            Item(name="Aged Brie", sell_in=-8, quality=25),
            Item(name="Aged Brie /Conjured /Timeless", sell_in=10, quality=24),
            Item(name="+5 Dexterity Vest /Puzzing /High_Quality", sell_in=3, quality=18)
        ]

        gilded_rose = GildedRose(items)
        for i in range(7):
            gilded_rose.update_quality()

        for item, degraded in zip(gilded_rose.items, answers):
            #print(item, degraded)
            self.assertEqual(item.quality, degraded.quality)
            self.assertEqual(item.sell_in, degraded.sell_in)

    def test_20_days(self):
        items = self.create_base_items()

        answers = [
            Item(name="+5 Dexterity Vest", sell_in=-10, quality=0),
            Item(name="Aged Brie", sell_in=-18, quality=38),
            Item(name="Elixir of the Mongoose", sell_in=-15, quality=0),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-10, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-15, quality=0),
            Item(name="Backstage passes to a TAKFAL80ETC concert", sell_in=-16, quality=0),
            Item(name="+5 Dexterity Vest", sell_in=-21, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-21, quality=0),
            Item(name="Aged Brie", sell_in=-21, quality=50),
            Item(name="Aged Brie /Conjured /Timeless", sell_in=10, quality=50),
            Item(name="+5 Dexterity Vest /Puzzing /High_Quality", sell_in=-10, quality=0)
        ]


        gilded_rose = GildedRose(items)
        for i in range(20):
            gilded_rose.update_quality()

        for item, degraded in zip(gilded_rose.items, answers):
            #print(item, degraded)
            self.assertEqual(item.quality, degraded.quality)
            self.assertEqual(item.sell_in, degraded.sell_in)


    def test_repr(self):
        self.assertEqual(str(Item(name="Sulfuras, Hand of Ragnaros", sell_in=50, quality=80)),"Sulfuras, Hand of Ragnaros, 50, 80")

if __name__ == '__main__':
    unittest.main()
