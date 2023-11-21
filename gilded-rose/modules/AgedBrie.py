from modules.Item import Item

class AgedBrie(Item):
     def update_quality(self):
        self.sell_in = self.sell_in - 1
        self.quality = min(50, self.quality + 1)
        if self.sell_in < 0:
            self.quality = min(50, self.quality + 1)