# -*- coding: utf-8 -*-

class Item():
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class General(Item):
    def update_quality(self):
        if self.quality<= 50:
            if self.sell_in >= 0:
                self.quality = self.quality - 1
            else:
                self.quality = self.quality - 2
            self.sell_in = self.sell_in - 1

class Conjured(General):
    def update_quality(self):
        if self.quality<= 50:
            if self.sell_in >= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 4
            self.sell_in = self.sell_in - 1
    
class Brie(Item):
    def update_quality(self):
        if self.quality<= 50:
            if self.sell_in >= 0:
                self.quality = self.quality + 1
            else:
                self.quality = self.quality + 2
            
            self.sell_in = self.sell_in - 1

class Backstage(Item):
    def update_quality(self):
        if self.quality<= 50:
            if self.quality <=47 and self.sell_in < 6:
                self.quality = self.quality + 3
            elif self.quality <=48 and self.sell_in < 11:
                self.quality = self.quality + 2
            elif self.quality < 50:
                self.quality = self.quality + 1
            self.sell_in = self.sell_in - 1

class Sulfuras(Item):
    def update_quality(self):
        self.quality= self.quality
        self.sell_in= self.sell_in