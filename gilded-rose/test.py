# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose


test_cases_one_day = {
    "it": [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=10, quality=50),
        Item(name="Elixir of the Mongoose", sell_in=-5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=30),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=10),
        Item(name="Aged Brie", sell_in=3, quality=6),
        Item(name="Aged Brie", sell_in=-3, quality=6),
        Item(name="Conjured item", sell_in=15, quality=8)],
    "expect_qual": [19, 49, 5, 80, 21, 32, 13, 0, 7, 8, 6],
    "expect_sellin": [9, 9, -6, 0, 14, 9, 4, -6, 2, -4, 14]
}

test_cases_one_week = {
    "it": [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="+5 Dexterity Vest", sell_in=10, quality=50),
        Item(name="Elixir of the Mongoose", sell_in=-5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=30),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=10),
        Item(name="Aged Brie", sell_in=3, quality=6),
        Item(name="Aged Brie", sell_in=-3, quality=6)],
    "expect_qual": [13, 43, 0, 80, 29, 46, 0, 0, 17, 20],
    "expect_sellin": [3, 3, -12, 0, 8, 3, -2, -12, -4, -10]
}

class GildedRoseTest(unittest.TestCase):
    
    # Unit Test 1
    def test_quality_day_one(self):
        gilded_rose = GildedRose(test_cases_one_day["it"])
        gilded_rose.update_quality()
        
        for i, expected in enumerate(test_cases_one_day["expect_qual"]):
            self.assertEquals(expected, gilded_rose.items[i].quality)
            
        for j, expected in enumerate(test_cases_one_day["expect_sellin"]):
            self.assertEquals(expected, gilded_rose.items[j].sell_in)
            
    # Unit Test 2
    def test_quality_week_one(self):
        gilded_rose = GildedRose(test_cases_one_week["it"])
        gilded_rose.update_quality_multiple_day(7)
        
        for i, expected in enumerate(test_cases_one_week["expect_qual"]):
            self.assertEquals(expected, gilded_rose.items[i].quality)
            
        for j, expected in enumerate(test_cases_one_week["expect_sellin"]):
            self.assertEquals(expected, gilded_rose.items[j].sell_in)
        

if __name__ == '__main__':
    unittest.main()
