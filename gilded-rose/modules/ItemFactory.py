from modules.Sulfuras import Sulfuras
from modules.AgedBrie import AgedBrie
from modules.Backstage import Backstage

class ItemFactory():
    def create_item(self,current_item):
        if "Sulfuras" in current_item.name:
            return Sulfuras(current_item.name, current_item.sell_in, current_item.quality)
        elif current_item.name == "Aged Brie":
             return AgedBrie(current_item, current_item.sell_in, current_item.quality)
        elif "Backstage" in current_item.name:
             return Backstage(current_item, current_item.sell_in, current_item.quality)
        else:
            return current_item