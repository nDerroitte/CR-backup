# -*- coding: utf-8 -*-
import unittest

from modules.gilded_rose import Item, GildedRose



items_dict = {
"it": [Item(name="Sulfuras", sell_in=5, quality=5),
    Item(name="Dexterity", sell_in=5, quality=5),
    Item(name="Cake", sell_in=5, quality=5), 
    Item(name="Elixir", sell_in=5, quality=5),
    Item(name="TAFKAL", sell_in=-5, quality=5),
    Item(name="TAFKAL", sell_in=5, quality=5),
    Item(name="TAFKAL", sell_in=10, quality=5),
    Item(name="TAFKAL", sell_in=15, quality=5),
    Item(name="Brie", sell_in=-5, quality=5),
    Item(name="Brie", sell_in=5, quality=5)],
"expected_quality" : [5,4,4,4,0,8,7,6,7,6],
"expected_dayin" : [5,4,4,4,-6,4,9,14,-6,4]
}

class GildedRoseTest(unittest.TestCase):
    def test_one_day(self):
        items = items_dict["it"]
        item_qual = items_dict["expected_quality"]
        item_dayin = items_dict["expected_dayin"]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for index, item in enumerate(gilded_rose.items):
            self.assertEquals(item.quality, item_qual[index])
            self.assertEquals(item.sell_in, item_dayin[index])

if __name__ == '__main__':
    unittest.main()       





    
    
    



