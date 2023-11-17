# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_regular_item(self):
        items = [Item("Regular Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)
    def test_item_repr_method(self):
        item= Item("Aged Brie", 3, 10)
        self.assertEqual("Aged Brie, 3, 10",item.__repr__())
    def test_update_quality_aged_brie(self):
        items = [Item("Aged Brie", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(11, items[0].quality)
    def test_update_quality_aged_brie_negative(self):
        items = [Item("Aged Brie", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_update_quality_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)


    def test_update_quality_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_update_quality_item_sell_in_negative(self):
        items = [Item("Regular Item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_update_quality_item_quality_null(self):
        items = [Item("Regular Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_update_quality_item_quality_upper_null(self):
        items = [Item("Regular Item", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(49, items[0].quality)

    def test_update_quality_item_quality_upper_null_forloop(self):
        items = [Item("Regular Item", 5, 50)]
        gilded_rose = GildedRose(items)
        for _ in range(10):
            gilded_rose.update_quality()
        self.assertEqual(-5, items[0].sell_in)
        self.assertEqual(35, items[0].quality)

    def test_update_quality_conjured_item(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
