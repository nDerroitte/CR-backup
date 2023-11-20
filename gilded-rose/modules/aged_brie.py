from modules.item import Item


class AgedBrie(Item):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in >= 0:
            self.quality = min(self.quality + 1, 50)
        elif self.sell_in < 0:
            self.quality = min(self.quality + 2, 50)
