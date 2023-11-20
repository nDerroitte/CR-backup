from modules.item import Item

class Tafkal(Item):
    def tafkal_update_quality(self, name, sell_in, quality):
                    if quality < 50 and sell_in < 11 and sell_in >= 6:
                                quality = quality + 1
                                #TAFKAL +1
                    if quality < 50 and sell_in < 6:
                                quality = quality + 2
                                #TAFKAL +1
                    return quality