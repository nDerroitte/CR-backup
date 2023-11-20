# -*- coding: utf-8 -*-

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
            
#         for item in self.items:
#             # For Sulfuras, nothing changes
#             if item.name != "Sulfuras, Hand of Ragnaros": 
                           
#                 # Consider the normal items
#                 if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                     if item.quality > 0:
#                         item.quality = item.quality - 1
#                         # Quality of Conjured Items decreases twice as fast
#                         if ("Conjured" in item.name) and (item.quality > 0):
#                             item.quality = item.quality - 1
#                         # Additional quality decrease if negative sell_in
#                         if (item.sell_in < 0) and (item.quality > 0):
#                             item.quality = item.quality - 1
                            
#                     item.sell_in = item.sell_in - 1
                            
#                 # Specific items    
#                 else:
#                     # For Aged Brie or backstage passes, simple quality increase
#                     if item.quality < 50:
#                         item.quality = item.quality + 1
#                         # Special variation of quality depending on the sell_in value for passes
#                         if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                             # Double increase if sell_in lower than 11
#                             if (item.sell_in < 11) and (item.quality < 50):
#                                 item.quality = item.quality + 1
                                
#                             # Triple increase if sell_in lower than 6
#                             if (item.sell_in < 6) and (item.quality < 50):
#                                 item.quality = item.quality + 1
                            
#                             # If sell_in negative for Backstage passes, quality = 0    
#                             if item.sell_in < 0:
#                                 item.quality = item.quality - item.quality
                                
#                         if item.name == "Aged Brie":
#                             # Additional quality increase if negative sell_in
#                             if (item.sell_in < 0) and (item.quality < 50):
#                                 item.quality = item.quality + 1
                                                                
#                     # Sell_in value does not change for Sulfuras, if != decrease the sell_in
#                     item.sell_in = item.sell_in - 1    
    
    
#     # The same function but repeated n_days times                   
#     def update_quality_multiple_day(self, n_days):
#         for i in range(n_days):
#             self.update_quality()


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
        

