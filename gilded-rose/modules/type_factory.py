
from modules.item_classes import *
class TypeFactory():
    def create_item(self, item):
        if item.name.find('Brie')  !=-1:
            tf = Brie(item.name, item.sell_in, item.quality)
        elif item.name.find('Backstage') !=-1:
            tf = Backstage(item.name, item.sell_in, item.quality)
        elif  item.name.find('Sulfuras') !=-1:
            tf = Sulfuras(item.name, item.sell_in, item.quality)
        elif  item.name.find('Conjured') !=-1:
            tf = Conjured(item.name, item.sell_in, item.quality)
        else:
            tf = General(item.name, item.sell_in, item.quality)
        return tf 