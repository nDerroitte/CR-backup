# -*- coding: utf-8 -*-

from main.ItemFactory import ItemFactory


class GildedRose:

    def __init__(self, items: list):
        # Create Store from items
        itemfactory = ItemFactory()
        self.items = []
        for item in items:
            self.items.append(itemfactory.createObject(item))

    def update_quality(self):
        '''
        Handles the quality and sell-in of all items. Updates 1 day
        :return: None
        '''
        for item in self.items:
            item.update()
