# -*- coding: utf-8 -*-
from .factory_item import ItemFactory
class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.update_factory=ItemFactory()
        updated_items = []
        for item in self.items:
            # Create a new item with updated values
            updated_item = self.update_factory.create_item(item)
            updated_items.append(updated_item)

        self.items = updated_items
        print(self.items)
    def update_quality(self):


        for item in self.items:
            item.update_item()



        print(self.items)
