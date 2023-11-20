# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

test_cases = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=-1, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Aged Brie", sell_in=2, quality=60),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=50),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6), 
        Item(name="Conjured Mana Cake", sell_in=-1, quality=6),
        Item(name="Elixir of the Mongoose", sell_in=-4, quality=4),
    ]

class GildedRoseTest(unittest.TestCase):
    def test_name(self):
        gilded_rose = GildedRose(test_cases)
        items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=-1, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Aged Brie", sell_in=2, quality=60),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=50),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=40),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        Item(name="Conjured Mana Cake", sell_in=-1, quality=6), 
        Item(name="Elixir of the Mongoose", sell_in=-1, quality=4),
    ]
        
        for (idx, item )  in enumerate(  gilded_rose.items ) :
            self.assertEqual(item.name, items[idx].name)

    def test_quality(self):
        items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=19),
        Item(name="+5 Dexterity Vest", sell_in=-1, quality=18),
        Item(name="Aged Brie", sell_in=1, quality=1),
        Item(name="Aged Brie", sell_in=2, quality=60),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=6),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=50),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=21),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=50),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=43),
        Item(name="Conjured Mana Cake", sell_in=3, quality=4), 
        Item(name="Conjured Mana Cake", sell_in=-2, quality=2),
        Item(name="Elixir of the Mongoose", sell_in=-1, quality=2),
    ]
        gilded_rose = GildedRose(test_cases)
        gilded_rose.update_quality()
        for (idx, item )  in enumerate(  gilded_rose.items ) :
            self.assertEqual(item.quality, items[idx].quality)

    def test_sell_in(self):
            items = [
        Item(name="+5 Dexterity Vest", sell_in=9, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=-2, quality=20),
        Item(name="Aged Brie", sell_in=1, quality=0),
        Item(name="Aged Brie", sell_in=2, quality=60),
        Item(name="Elixir of the Mongoose", sell_in=4, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=50),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=14, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=40),
        Item(name="Conjured Mana Cake", sell_in=2, quality=6), 
        Item(name="Conjured Mana Cake", sell_in=-2, quality=2),
        Item(name="Elixir of the Mongoose", sell_in=-5, quality=4)
        ]
            gilded_rose = GildedRose(test_cases)
            gilded_rose.update_quality()
            for (idx, item )  in enumerate(  gilded_rose.items ) :
                self.assertEqual(item.sell_in, items[idx].sell_in)


if __name__ == '__main__':
    unittest.main()
