# -*- coding: utf-8 -*-
from modules.item_factory import itemFactory


class GildedRose(object):
    def __init__(self, items):
        self.item_factory = itemFactory()
        self.items = [self.item_factory.create_item_object(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update_quality()
