from modules.aged_brie import AgedBrie
from modules.backstage_passes import BackstagePasses
from modules.plain_object import PlainObject
from modules.sulfuras import Sulfuras
from modules.conjured import Conjured


class ObjectFactory:
    def create_object(name: str, sell_in: int, quality: int):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        elif "backstage passes" in name.lower():
            return BackstagePasses(name, sell_in, quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        elif "conjured" in name.lower():
            return Conjured(name, sell_in, quality)
        else:
            return PlainObject(name, sell_in, quality)
