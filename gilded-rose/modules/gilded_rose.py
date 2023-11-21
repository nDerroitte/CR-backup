# -*- coding: utf-8 -*-

from modules.ItemFactory import ItemFactory

class GildedRose(object):
    def __init__(self, items):
        factory = ItemFactory()
        self.items = [factory.create_item(item) for item in items]
    
    def update_quality(self):
        for i in self.items:
            i.update_quality()