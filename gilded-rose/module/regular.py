from .Item import Item
class RegularItem(Item):
    def __init__(self, name, sell_in, quality):
        self.item_quality_upper_limit= 50
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    def update_item(self):
        self.update_sellin()
        if self.quality > 0 :
            self.quality -= 1

        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1
    def update_sellin(self):
        self.sell_in -= 1