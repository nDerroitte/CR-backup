from main.items.agedBrie import AgedBrie
from main.items.backstagePasses import BackstagePasses
from main.items.generalItems import GeneralItem
from main.items.sulfuras import Sulfuras

from main.mods.basemod import BaseMod
from main.mods.quality_mods import *
from main.mods.sell_in_mods import *

class ItemFactory():

    def __init__(self) -> None:
        self.quality_mod_map = {
            "conjured" : ConjuredMod(),
            "high_quality" : HighQualityMod()
        }

        self.sell_in_mod_map = {
            "timeless": TimelessMod(),
            "puzzling": PuzzlingMod()
        }

    def parseName(self, name):
        """
        Map string name to Mod class
        """

        if "/" not in name:
            return {"sell_in_mod" : BaseMod(), "quality_mod": BaseMod()}
        
        mods = name.split("/")[1:]
        mods = [mod.strip().lower() for mod in mods]
        # Find sell in mods which matches with any part of the name
        sell_in_mod = [self.sell_in_mod_map[x] for x in mods if x in self.sell_in_mod_map]

        # Find quality mods which matches with any part of the name
        quality_mod = [self.quality_mod_map[x] for x in mods if x in self.quality_mod_map]


        return {"sell_in_mod": sell_in_mod[0] if sell_in_mod else BaseMod(),
                "quality_mod": quality_mod[0] if quality_mod else BaseMod()}


    def createObject(self,item):
        mods = self.parseName(item.name)
        basename = item.name.split("/")[0].strip()
        if basename == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePasses(item.name,item.sell_in, item.quality, mods["sell_in_mod"], mods["quality_mod"])

        elif basename == "Aged Brie":
            return AgedBrie(item.name,item.sell_in, item.quality, mods["sell_in_mod"], mods["quality_mod"])

        elif basename == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(item.name,item.sell_in, item.quality, mods["sell_in_mod"], mods["quality_mod"])

        else:
            return GeneralItem(item.name,item.sell_in, item.quality, mods["sell_in_mod"], mods["quality_mod"])