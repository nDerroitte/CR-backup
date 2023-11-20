# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose


def get_test_case():
    test_case = [
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
    return test_case


class GildedRoseTest(unittest.TestCase):

    def test_sulfuras(self):
        test_case = get_test_case()
        for item in test_case:
            if item.name == "Sulfuras, Hand of Ragnaros":
                self.assertEqual(item.quality, 80)

    def test_quality(self):
        test_case = get_test_case()
        gilded_rose = GildedRose(test_case)
        for i in range(30):
            gilded_rose.update_quality()
            for item in gilded_rose.items:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self.assertLess(item.quality, 51)
                    self.assertGreaterEqual(item.quality, 0)

    def test_quality_decrease(self):
        test_case = get_test_case()
        gilded_rose = GildedRose(test_case)
        for i in range(10):
            gilded_rose.update_quality()
        for item in gilded_rose.items:
            if item.name == "Banana":
                self.assertEqual(item.quality, 35)
            elif item.name == "Aged Brie":
                self.assertEqual(item.quality, 18)

    def test_backstage_passes(self):
        test_case = get_test_case()
        gilded_rose = GildedRose(test_case)
        for i in range(10):
            gilded_rose.update_quality()
        for item in gilded_rose.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 0:
                self.assertEqual(item.quality, 0)
            if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in > 0:
                self.assertEqual(item.quality, 35)

    def test_conjured(self):
        test_case = get_test_case()
        gilded_rose = GildedRose(test_case)
        for i in range(10):
            gilded_rose.update_quality()
        for item in gilded_rose.items:
            if item.name == "Conjured":
                self.assertEqual(item.quality, 10)


if __name__ == '__main__':
    unittest.main()
