# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("fixme", 0, 0),
                 Item("Sulfuras, Hand of Ragnaros", 4, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEquals(80, items[1].quality)

if __name__ == '__main__':
    unittest.main()
