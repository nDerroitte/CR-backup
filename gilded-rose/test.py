# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import GildedRose
from modules.Item import Item

class GildedRoseTest(unittest.TestCase):
    def test_exceptions_d1(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="+5 Dexterity Vest", sell_in=-2, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=9),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        testcases = [Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
            Item(name="+5 Dexterity Vest", sell_in=-3, quality=18),
            Item(name="Aged Brie", sell_in=1, quality=1),
            Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-6, quality=0),
            Item(name="Conjured Mana Cake", sell_in=2, quality=5),]

        for item, test in zip(items, testcases):
            self.assertEquals(item.name, test.name)
            self.assertEquals(item.sell_in, test.sell_in)
            self.assertEquals(item.quality, test.quality)

    def test_exceptions_d7(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                Item(name="+5 Dexterity Vest", sell_in=-2, quality=20),
                Item(name="Aged Brie", sell_in=2, quality=0),
                Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=9),
                Item(name="Conjured Mana Cake", sell_in=3, quality=6),]
        
        gilded_rose = GildedRose(items)
        for i in range(7):
            gilded_rose.update_quality()

        testcases = [Item(name="+5 Dexterity Vest", sell_in=3, quality=13),
                Item(name="+5 Dexterity Vest", sell_in=-9, quality=6),
                Item(name="Aged Brie", sell_in=-5, quality=12),
                Item(name="Elixir of the Mongoose", sell_in=-2, quality=0),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=30),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=50),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-2, quality=0),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-12, quality=0),
                Item(name="Conjured Mana Cake", sell_in=-4, quality=0),]

        for item, test in zip(items, testcases):
            self.assertEquals(item.name, test.name)
            self.assertEquals(item.sell_in, test.sell_in)
            self.assertEquals(item.quality, test.quality)

if __name__ == '__main__':
    unittest.main()
