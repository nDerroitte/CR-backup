# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

if __name__ == '__main__':
    unittest.main()

class test_cases_one_day(unittest.TestCase):
    def test_oneday(self):
    items = [
        Item(name="Sulfuras", sell_in=0, quality=80),
        Item(name="Dexterity", sell_in=10, quality=20),
        Item(name="Cake", sell_in=3, quality=6), 
        Item(name="Elixir", sell_in=5, quality=7),
        Item(name="TAFKAL", sell_in=15, quality=20),
        Item(name="TAFKAL", sell_in=10, quality=49),
        Item(name="TAFKAL", sell_in=5, quality=49),
        Item(name="TAFKAL", sell_in=5, quality=49),
        Item(name="Brie", sell_in=2, quality=0),
        Item(name="Brie", sell_in=2, quality=0),
    ]



