from modules.item import Item


class Conjured(Item):
    def update_quality(self):
        self.quality = max(self.quality - 1, 0)
        self.sell_in -= 2
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = max(self.quality - 2, 0)