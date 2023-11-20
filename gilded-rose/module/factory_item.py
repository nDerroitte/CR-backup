from .agedbrie import *
from .backstage import *
from .sulfura import *
from .Item import Item
from .regular import RegularItem
from .conjured import ConjuredItem
class ItemFactory:
    def create_item(self,item:Item):
       if item.name== "Backstage passes to a TAFKAL80ETC concert":
           return BackstageItem(item.name,item.sell_in, item.quality)
       elif item.name=="Aged Brie":
           return AgedBrieItem(item.name,item.sell_in, item.quality)
       elif item.name=="Sulfuras, Hand of Ragnaros":
           return Sulfura(item.name,item.sell_in, item.quality)
       elif "Conjured" in item.name:
           return ConjuredItem(item.name,item.sell_in, item.quality)
       return RegularItem(item.name,item.sell_in, item.quality)

