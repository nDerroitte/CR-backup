from modules.Item import Item

class Conjured(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.quality > 0:
            self.quality -= 2
        if self.quality > 0 and self.sell_in < 0:
            self.quality -= 2