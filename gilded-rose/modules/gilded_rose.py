# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # not brie and Tafkal
            if item.name != "Brie" and item.name != "TAFKAL":
                if item.quality > 0:
                    if item.name != "Sulfuras":
                        item.quality = item.quality - 1
                        # Dexterity: -1
                        # Elixir -1
                        # Cake -1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    # Brie +1
                    #TAFKAL +1
                    if item.name == "TAFKAL":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                                #TAFKAL +1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                                #TAFKAL +1
            if item.name != "Sulfuras":
                item.sell_in = item.sell_in - 1
                # Dexterity: -1
                # Elixir -1
                # Cake -1
                # Sulfuras 0
                # Tafkas -1
                # Brie -1
            if item.sell_in < 0:
                if item.name != "Brie":
                    if item.name != "TAFKAL":
                        if item.quality > 0:
                            if item.name != "Sulfuras":
                                item.quality = item.quality - 1
                                #Dexterity: -1
                                # Elixir -1
                                # Cake -1

                    else:
                        item.quality = item.quality - item.quality
                        #TAFKAL -item quality
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
