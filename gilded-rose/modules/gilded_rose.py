# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Quality
            # Sulfuras
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality += 0
            # Other products
            elif item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"] and item.quality > 0:
                item.quality -= 1
            else: # Brie and backstage passes
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11 and item.quality < 50:
                            item.quality += 1
                        if item.sell_in < 6 and item.quality < 50:
                            item.quality += 1
            # Decrease sell-in by -1 for every item except Sulfuras
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

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
