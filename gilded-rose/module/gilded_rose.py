# -*- coding: utf-8 -*-
from .factory_item import *
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        updated_items = []
        for item in self.items:
            # Create a new item with updated values
            updated_item = ItemFactory.create_item(item.name, item.sell_in, item.quality)
            updated_item.update_item()
            updated_items.append(updated_item)
            print("lalallalallallallalall",updated_item)
        self.items=updated_items

