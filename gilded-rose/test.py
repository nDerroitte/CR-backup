# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Coffee", 0, 5),
                 Item("Sulfuras, Hand of Ragnaros", 4, 80),
                 Item("Cheese Sandwich", 14, 35),
                 Item("Aged Brie", 20, 50),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
                 Item("Backstage passes to a TAFKAL80ETC concert", 0, 40),
                 Item("Aged Brie", -1, 40),
]
        gilded_rose = GildedRose(items)
        self.assertEquals(4, items[1].sell_in)
        self.assertEquals(35, items[2].quality)
        gilded_rose.update_quality()
        self.assertEquals("Coffee", items[0].name)
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[1].name)
        self.assertEquals(80, items[1].quality)
        self.assertEquals(34, items[2].quality)
        self.assertEquals(0, items[5].quality)
        self.assertEquals(3, items[0].quality)
        self.assertEquals(42, items[6].quality)



if __name__ == '__main__':
    unittest.main()
