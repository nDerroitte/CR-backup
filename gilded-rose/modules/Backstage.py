from modules.Item import Item

class Backstage(Item):
    def update_quality(self): 
        self.sell_in = self.sell_in - 1
        self.quality = min(50, self.quality + 1)

        if 6 < self.sell_in < 11:
                self.quality = min(50, self.quality + 1)
        elif 0 < self.sell_in < 6:
                self.quality = min(50, self.quality + 2)
        elif self.sell_in < 0:
            self.quality = 0