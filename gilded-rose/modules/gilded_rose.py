# -*- coding: utf-8 -*-

class ItemFactory:
    def new_Item(self, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        else:
            return OtherItem(name, sell_in, quality)
        
        
class GildedRose(object):

    def __init__(self, items):
        self.items = items
        
    def behavior(self):
       for ind, item in enumerate(self.items):
            if item.name == "Aged Brie":
                self.items[ind] = AgedBrie(item.name, item.sell_in, item.quality)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.items[ind] = BackstagePass(item.name, item.sell_in, item.quality)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.items[ind] = Sulfuras(item.name, item.sell_in, item.quality)
            else:
                self.items[ind] = OtherItem(item.name, item.sell_in, item.quality)
         
    def update_quality(self):
        for item in self.items:
            item.update_quality()
            
    def update_quality_multiple_day(self, n_days):
        for item in self.items:
            for i in range(n_days):
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
        if self.quality < 50:
            self.quality += 1
                
        if (self.sell_in < 0) and (self.quality < 50): # Double increase if negative sell_in
            self.quality += 1
                
        self.sell_in -= 1
            
    def update_quality_multiple_day(self, n_days):
        for i in range(n_days):
            self.update_quality()
            
class BackstagePass(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
                
        if (self.sell_in < 11) and (self.quality < 50): # Double increase if sell_in lower than 11
            self.quality += 1
                                
        if (self.sell_in < 6) and (self.quality < 50): # Triple increase if sell_in lower than 6
            self.quality += 1
                                
        if self.sell_in < 0: # If sell_in negative for Backstage passes, quality = 0
            self.quality = 0
                
        self.sell_in -= 1
            
            
    def update_quality_multiple_day(self, n_days):
        for i in range(n_days):
            self.update_quality()
              
class OtherItem(Item):
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
                
        if (self.sell_in < 0) and (self.quality > 0): # Double decrease if negative sell_in
            self.quality -= 1
                
        if ("Conjured" in self.name) and (self.quality > 0): # Double decrease for Conjured Items
            self.quality -= 1
            
        self.sell_in -= 1
                
    def update_quality_multiple_day(self, n_days):
        for i in range(n_days):
            self.update_quality()
            
class Sulfuras(Item):
    def update_quality(self):
        pass
    
    def update_quality_multiple_day(self, n_days):
        pass
        

