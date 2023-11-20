# -*- coding: utf-8 -*-

exception_objects = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _aged_brie(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.quality < 50 and item.sell_in >= 0:
                    item.quality = item.quality + 1
                elif item.quality < 49 and item.sell_in < 0:
                    item.quality = item.quality + 2

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self._aged_brie()
            elif item.name not in ["Sulfuras, Hand of Ragnaros", "Aged Brie"]:
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        if item.name == "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.name != "Aged Brie":
                        if item.name != "Backstage passes to a TAFKAL80ETC concert":
                            if item.quality > 0:
                                item.quality = item.quality - 1
                        else:
                            item.quality = item.quality - item.quality
                    else:
                        if item.quality < 50:
                            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
