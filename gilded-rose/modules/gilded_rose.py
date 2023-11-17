# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.item_quality_upper_limit= 50
        self.backstage_Sellin_First_Upper_limit=6
        self.backstage_Sellin_Second_Upper_limit=11

    def is_backstage (self, item) -> bool:
        return item.name=="Backstage passes to a TAFKAL80ETC concert"
    def is_aged_brie(self, item) -> bool:
        return item.name == "Aged Brie"

    def update_backstage_quality(self, item):
        if item.quality < self.item_quality_upper_limit:
            item.quality += 1
            if item.sell_in < self.backstage_Sellin_Second_Upper_limit:
                if item.quality < self.item_quality_upper_limit:
                    item.quality = item.quality + 1
            if item.sell_in < self.backstage_Sellin_First_Upper_limit:
                if item.quality < self.item_quality_upper_limit:
                    item.quality = item.quality + 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

    def update_regular_item_quality(self, item):
        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality -= 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1
    def update_aged_brie_quality(self,item):
        if item.quality < self.item_quality_upper_limit:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < self.item_quality_upper_limit:
            item.quality = item.quality + 1
    def update_quality(self):
        for item in self.items:
          if self.is_backstage(item):
              self.update_backstage_quality(item)
          elif self.is_aged_brie(item):
              self.update_aged_brie_quality(item)
          else:
              self.update_regular_item_quality(item)
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
