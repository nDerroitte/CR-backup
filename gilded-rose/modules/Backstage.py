from modules.Item import Item

class Backstage(Item):
    def update_quality(self): 
        if self.quality < 50:
                self.quality += 1

        if 6 < self.sell_in < 11 and self.quality < 50:
                self.quality += 1
        elif 0 < self.sell_in < 6:
            if self.quality < 49:
                self.quality += 2
            else:
                self.quality = 50
        elif self.sell_in < 0:
            self.quality = 0