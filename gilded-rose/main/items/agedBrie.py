# -*- coding: utf-8 -*-

from main.Item import Item
from main.mods.basemod import BaseMod

class AgedBrie(Item):
    """
    The item may have multiple modifiers, each affecting its parameters in some way
    """

    def __init__(self, name, sell_in, quality, sell_in_mod=BaseMod(), quality_mod=BaseMod()):
        super().__init__(name, sell_in, quality)
        self.sell_in_mod = sell_in_mod
        self.quality_mod = quality_mod        

    def update(self):
        '''
        :param item: Item of type Aged Brie
        :return: None
        Decreases sell in and handles quality variations
        '''

        # Update Sell in
        self.sell_in -= self.sell_in_mod.update_value(1)
        
        # Update Quality
        if self.sell_in < 0:
            self.quality += self.quality_mod.update_value(2)
        else:
            self.quality += self.quality_mod.update_value(1)

        # Check bounded values
        if self.quality > 50:
            self.quality = 50

        elif self.quality < 0:
            self.quality = 0 