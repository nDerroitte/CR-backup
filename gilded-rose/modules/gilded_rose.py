# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            # Quality modification
            
            # Aged Brie and Backstage passes update not in the same way as other things
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    # Quality of Sulfuras does not change
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
                        # Quality of Conjured Items decreases twice as fast
                        if "Conjured" in item.name:
                            item.quality = item.quality - 1
                        
            else:
                # If quality is < 50, and we have Aged Brie or backstage passes, simple quality increase
                if item.quality < 50:
                    item.quality = item.quality + 1
                    
                    # Special variation of quality depending on the sell_in value for passes
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # Double increase if sell_in lower than 11
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                                
                        # Triple increase if sell_in lower than 6
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                                
            # Sell_in value modification
                                
            # Sell_in value does not change for Sulfuras, if != decrease the sell_in
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
                
            # Negative sell_in induces additional quality decrease if item != Aged Brie, Backstage passes and Sulfuras
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                                
                    # If sell_in negative for Backstage passes, quality = 0
                    else:
                        item.quality = item.quality - item.quality
                        
                # Negative sell_in for Aged Brie increases the quality by 1 if quality < 50
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
