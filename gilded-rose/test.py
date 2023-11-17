# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose


test_cases_qual = {
    "it": [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6)],
    "expect": [19, 1, 6, 80, 80, 21, 50, 50, 4]
}

#test_cases_sellin = {
    
#}

class GildedRoseTest(unittest.TestCase):
    
    # Unit Test 1
    def test_quality(self):
        gilded_rose = GildedRose(test_cases_qual["it"])
        gilded_rose.update_quality()
        
        for i, expected in enumerate(test_cases_qual["expect"]):
            self.assertEquals(expected, gilded_rose.items[i].quality)

if __name__ == '__main__':
    unittest.main()
