from modules.Sulfuras import Sulfuras
from modules.AgedBrie import AgedBrie
from modules.Backstage import Backstage
from modules.GeneralItem import GeneralItem
from modules.Conjured import Conjured

class ItemFactory():
    def create_item(self,current_item):
        if "Sulfuras" in current_item.name:
            return Sulfuras(current_item.name, current_item.sell_in, current_item.quality)
        elif current_item.name == "Aged Brie":
            return AgedBrie(current_item.name, current_item.sell_in, current_item.quality)
        elif "Backstage" in current_item.name:
            return Backstage(current_item.name, current_item.sell_in, current_item.quality)
        elif "Conjured" in current_item.name:
            return Conjured(current_item.name, current_item.sell_in, current_item.quality)
        else:
            return GeneralItem(current_item.name, current_item.sell_in, current_item.quality)