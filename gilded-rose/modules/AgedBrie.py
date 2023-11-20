from modules.Item import Item

class AgedBrie(Item):
     def update_quality(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1
        if self.quality < 50 and self.sell_in < 0:
            self.quality += 1