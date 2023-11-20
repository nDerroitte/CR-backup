# -*- coding: utf-8 -*-
from modules.items.age_brie_item import ageBrieItem
from modules.items.concert_item import concertItem
from modules.items.general_item import general_item
from modules.items.conjured_item import conjuredItem
from modules.items.sulfuras_item import sulfurasItem


class itemFactory(object):
    def __init__(self):
        self.brie_name = "Aged Brie"
        self.concert_name = "Backstage passes to a TAFKAL80ETC concert"
        self.sulfuras_name = "Sulfuras, Hand of Ragnaros"


    def create_item_object(self, item):
        """
        Create an object item

        :param item: Item object to create
        :return: x_item object where x corresponds to the item name
        """
        
        if item.name == self.brie_name:
            return ageBrieItem(item.name, item.sell_in, item.quality)
        elif item.name == self.sulfuras_name:
            return sulfurasItem(item.name, item.sell_in, item.quality)
        elif item.name == self.concert_name:
            return concertItem(item.name, item.sell_in, item.quality)
        elif "conjured" in item.name.lower():
            return conjuredItem(item.name, item.sell_in, item.quality)
        else:
            return general_item(item.name, item.sell_in, item.quality)
