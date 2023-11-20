from .Item import Item
class BackstageItem(Item):
    def __init__(self, name, sell_in, quality):
        self.item_quality_upper_limit= 50
        self.backstage_Sellin_First_Upper_limit=6
        self.backstage_Sellin_Second_Upper_limit=11
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    def update_item(self):
        if self.sell_in < self.backstage_Sellin_First_Upper_limit and self.quality < self.item_quality_upper_limit:
            self.quality += 3
        elif self.sell_in < self.backstage_Sellin_Second_Upper_limit and self.quality < self.item_quality_upper_limit:
            self.quality = self.quality + 2
        elif self.quality < self.item_quality_upper_limit and self.quality < self.item_quality_upper_limit:
            self.quality = self.quality + 1

        self.update_sellin()
        if self.sell_in < 0:
            self.quality = 0
    def update_sellin(self):
        self.sell_in -= 1
