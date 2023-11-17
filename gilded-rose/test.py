# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

test_case = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured Mana Cake", sell_in=3, quality=7),
    Item(name="Apple", sell_in=999, quality=12),
    Item(name="Peer", sell_in=-2350, quality=48),
    Item(name="Banana", sell_in=78, quality=45)
]


class GildedRoseTest(unittest.TestCase):

    def test_sulfuras(self):
        for item in test_case:
            if item.name == "Sulfuras, Hand of Ragnaros":
                self.assertEqual(item.quality, 80)

    def test_quality(self):
        gilded_rose = GildedRose(test_case)
        for i in range(30):
            gilded_rose.update_quality()
            for item in gilded_rose.items:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self.assertLess(item.quality, 51)
                    self.assertGreaterEqual(item.quality, 0)

    def test_quality_decrease(self):
        gilded_rose = GildedRose(test_case)
        for i in range(10):
            gilded_rose.update_quality()
            for item in gilded_rose.items:
                if item.name == "Banana":
                    print(item.name, item.quality)
        for item in gilded_rose.items:
            if item.name == "Banana":
                self.assertEqual(item.quality, 36)
            # elif item.name == "Aged Brie":
            #     self.assertEqual(item.quality, 16)


if __name__ == '__main__':
    unittest.main()
