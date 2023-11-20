
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
class RegularItem(Item):

    def update_item(self):
        self.update_sellin()
        if self.quality > 0 :
            self.quality -= 1

        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1
    def update_sellin(self):
        self.sell_in -= 1
class BackstageItem(Item):

    item_quality_upper_limit= 50
    backstage_Sellin_First_Upper_limit=6
    backstage_Sellin_Second_Upper_limit=11
    def update_item(self):
        if self.sell_in < self.backstage_Sellin_First_Upper_limit:
            self.quality += 3
        elif self.sell_in < self.backstage_Sellin_Second_Upper_limit:
            self.quality = self.quality + 2
        elif self.quality < self.item_quality_upper_limit:
            self.quality = self.quality + 1

        self.update_sellin()
        if self.sell_in < 0:
            self.quality = 0
    def update_sellin(self):
        self.sell_in -= 1
class AgedBrieItem(Item):

    item_quality_upper_limit= 50

    def update_item(self):
        self.update_sellin()
        if self.quality < self.item_quality_upper_limit:
            self.quality = self.quality + 1

        if self.sell_in < 0 and self.quality < self.item_quality_upper_limit:
            self.quality = self.quality + 1
    def update_sellin(self):
        self.sell_in -= 1

class Sulfura(Item):
    def update_item(self):
       pass

class ItemFactory:
    def create_item( name,sell_in, quality):
       if name== "Backstage passes to a TAFKAL80ETC concert": return BackstageItem(name,sell_in, quality)
       elif name=="Aged Brie": return AgedBrieItem(name,sell_in, quality)
       elif name=="Sulfuras, Hand of Ragnaros": return Sulfura(name,sell_in, quality)
       return RegularItem(name,sell_in, quality)

