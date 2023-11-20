# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        for idx, item in enumerate(self.items):
            if item.name == "Aged Brie":
                item = AgedBrie(item.name, item.sell_in, item.quality)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item = BackstagePasses(item.name, item.sell_in, item.quality)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item = Sulfuras(item.name, item.sell_in, item.quality)
            else:
                item = PlainObject(item.name, item.sell_in, item.quality)
            self.items[idx] = item

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.quality = min(self.quality + 1, 50)
        elif self.sell_in < 0:
            self.quality = min(self.quality + 2, 50)


class BackstagePasses(Item):
    def update_quality(self):
        self.sell_in += - 1
        if self.sell_in >= 10:
            self.quality = min(self.quality + 1, 50)
        elif 5 <= self.sell_in < 10:
            self.quality = min(self.quality + 2, 50)
        elif -1 < self.sell_in < 5:
            self.quality = min(self.quality + 3, 50)
        elif self.sell_in < 0:
            self.quality = 0


class PlainObject(Item):
    def update_quality(self):
        self.quality = max(self.quality - 1, 0)
        self.sell_in -= 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality -= 1


class Sulfuras(Item):
    def update_quality(self):
        self.quality = self.quality
        self.sell_in = self.sell_in