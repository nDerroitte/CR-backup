# -*- coding: utf-8 -*-

from modules.ItemFactory import ItemFactory

class GildedRose(object):

#Special Items
#   Sulfuras: does never change
#   Aged Brie: quality increases
#   Backstage: if 6 <= sell_in < 11, quality increases by 1,
#               if sell_in < 6, quality increases by 2
#               if sell_in < 0, quality drops to 0
#   Conjured: +2 for quality and sell

#Other rules:
# -quality within 0 and 50
# -sell_in >0, quality -2

    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        factory = ItemFactory()
        for item in self.items:
            new_item = factory.create_item(item)
            new_item.update_quality()

            #Sulfuras cannot change
            #if "Sulfuras" not in item.name:

                #Every item will have his sell-in that decreases by 1
            #    item.sell_in -= 1  

                #If not a special item
            #    if item.name != "Aged Brie" and "Backstage" not in item.name:
            #        if item.quality > 0:
            #            item.quality -= 1
            #        if item.sell_in < 0 and item.quality > 0:
            #            item.quality -= 1

                #For Aged Brie and Backstage
            #    else:
            #        if item.quality < 50:
            #            item.quality += 1
            #            if item.sell_in < 0 and item.quality <50:
            #                item.quality += 1

            #        if "Backstage" in item.name:
            #            if 6 < item.sell_in < 11 and item.quality < 50:
            #                    item.quality += 1
            #            elif 0 < item.sell_in < 6 and item.quality < 50:
            #                    item.quality += 2
            #            elif item.sell_in < 0:
            #                    item.quality = 0