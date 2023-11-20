from modules.item import Item


class BackstagePasses(Item):
    def update_quality(self):
        self.sell_in += - 1
        if self.sell_in >= 10:
            self.quality = min(self.quality + 1, 50)
        elif 5 <= self.sell_in < 10:
            self.quality = min(self.quality + 2, 50)
        elif -1 < self.sell_in < 5:
            self.quality = min(self.quality + 3, 50)
        elif self.sell_in < 0:
            self.quality = 0
