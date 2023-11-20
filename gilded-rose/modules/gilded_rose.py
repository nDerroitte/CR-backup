# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name.startswith("Conjured"):
                conjured_item = ConjuredItem(item.name, item.sell_in, item.quality)
                conjured_item.update_quality(item)
            elif item.name == "Aged Brie": 
                AgedBrie(item.name, item.sell_in, item.quality).update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert": 
                BackstagePass(item.name, item.sell_in, item.quality).update_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                NormalItem(item.name, item.sell_in, item.quality).update_quality(item)

            # if products past their sell in date    
            if item.sell_in < 0:
                if item.name == "Aged Brie" and item.quality < 50:
                    item.quality += 1
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = item.quality - item.quality
                    else:
                        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class BackstagePass(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1
        if item.sell_in < 6 and item.quality < 50:
            item.quality += 1

class AgedBrie(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1

class NormalItem(Item):
    def update_quality(self, item):
        item.sell_in -= 1
        item.quality -= 1

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self, item):
        item.sell_in -= 1
        item.quality -= 2