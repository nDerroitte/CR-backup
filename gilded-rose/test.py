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
                 Item("Backstage passes to a TAFKAL80ETC concert", 2, 48),
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
        self.assertEquals(50, items[5].quality)
        self.assertEquals(3, items[0].quality)
        self.assertEquals(42, items[6].quality)
        self.assertEquals(4, items[1].sell_in)
        self.assertEquals("Coffee, -1, 3", items[0].__repr__())
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        self.assertEquals(50, items[5].quality)
        self.assertEquals(4, items[1].sell_in)
        self.assertEquals(16, items[4].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        self.assertEquals(4, items[1].sell_in)
        self.assertEquals(19, items[4].quality)






if __name__ == '__main__':
    unittest.main()
