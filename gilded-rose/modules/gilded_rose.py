# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        for idx, item in enumerate(self.items):
            self.items[idx] = ObjectFactory.create_object(item.name, item.sell_in, item.quality)

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class ObjectFactory:
    def create_object(name: str, sell_in: int, quality: int):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        elif name == "Conjured":
            return Conjured(name, sell_in, quality)
        else:
            return PlainObject(name, sell_in, quality)


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


class Conjured(Item):
    def update_quality(self):
        self.quality = max(self.quality - 1, 0)
        self.sell_in -= 2
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = max(self.quality - 2, 0)
