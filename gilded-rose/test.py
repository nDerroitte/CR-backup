# -*- coding: utf-8 -*-
import unittest

from module.gilded_rose import  GildedRose
from module.factory_item import *

itemsFactoryValue = [
    Item("Regular Item", 5, 10),
    Item("Aged Brie", 3, 10),
    Item("Aged Brie", -1, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 6, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 3, 10),
    Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Regular Item", -1, 10),
    Item("Regular Item", 5, 0),
    Item("Regular Item", 5, 50),
    Item("Backstage passes to a TAFKAL80ETC concert", -1, 10)
]

itemsFactoryAnswer = [
    Item("Regular Item", 4, 9),
    Item("Aged Brie", 2, 11),
    Item("Aged Brie", -2, 12),
    Item("Backstage passes to a TAFKAL80ETC concert", 5, 12),
    Item("Backstage passes to a TAFKAL80ETC concert", 2, 13),
    Item("Backstage passes to a TAFKAL80ETC concert", 14, 21),
    Item("Sulfuras, Hand of Ragnaros", 0, 80),
    Item("Regular Item", -2, 8),
    Item("Regular Item", 4, 0),
    Item("Regular Item", 4, 49),
    Item("Backstage passes to a TAFKAL80ETC concert", -2, 0)
]

# Iterate over the test cases


class GildedRoseTest(unittest.TestCase):
    def test_itemfactorytest(self):
        gilded_rose = GildedRose(itemsFactoryValue)
        print("Before update_quality:")
        for item in gilded_rose.items:
            print(item.name, item.quality, item.sell_in)

        gilded_rose.update_quality()

        print("After update_quality:")
        for item in gilded_rose.items:
            print(item.name, item.quality, item.sell_in)

        for input_values, expected_output_values in zip(gilded_rose.items, itemsFactoryAnswer):

            print(input_values.name," ",input_values.quality," ", expected_output_values.quality)
            # Check if the actual result matches the expected result
            assert input_values.name == expected_output_values.name
            assert input_values.quality == expected_output_values.quality
            assert input_values.sell_in == expected_output_values.sell_in
            print("fin")

if __name__ == '__main__':
    unittest.main()
