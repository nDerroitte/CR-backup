# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        factory = TypeFactory()

        for item in self.items:
            element = factory.create_item(item) 
            element.update_quality() 
            item.quality  = element.quality
            item.sell_in = element.sell_in
            
            
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

class TypeFactory:
    def create_item(self, item):
        if item.name.find('Brie')  !=-1:
            tf = Brie(item.name, item.sell_in, item.quality)
        elif item.name.find('Backstage') !=-1:
            tf = Backstage(item.name, item.sell_in, item.quality)
        elif  item.name.find('Sulfuras') !=-1:
            tf = Sulfuras(item.name, item.sell_in, item.quality)
        else:
            tf = General(item.name, item.sell_in, item.quality)
        return tf 

        