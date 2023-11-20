# -*- coding: utf-8 -*-
from modules.object_factory import ObjectFactory


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        for idx, item in enumerate(self.items):
            self.items[idx] = ObjectFactory.create_object(item.name, item.sell_in, item.quality)

    def update_quality(self):
        for item in self.items:
            item.update_quality()
