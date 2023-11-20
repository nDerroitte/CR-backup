# -*- coding: utf-8 -*-

exception_objects = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _aged_brie(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.sell_in >= 0:
                    item.quality = min(item.quality + 1, 50)
                elif item.sell_in < 0:
                    item.quality = min(item.quality + 2, 50)

    def _backstage_passes(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.sell_in = item.sell_in - 1
                if item.quality <= 50:
                    if item.sell_in > 10:
                        item.quality = min(item.quality + 1, 50)
                    elif 5 < item.sell_in <= 10:
                        item.quality = min(item.quality + 2, 50)
                    elif -1 < item.sell_in <= 5:
                        item.quality = min(item.quality + 3, 50)
                    elif item.sell_in < 0:
                        item.quality = 0

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._aged_brie()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._backstage_passes()
            elif item.name not in ["Sulfuras, Hand of Ragnaros", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
                if item.quality > 0:
                    item.quality = item.quality - 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
