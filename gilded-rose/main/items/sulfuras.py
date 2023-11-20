# -*- coding: utf-8 -*-

from main.Item import Item
from main.mods.basemod import BaseMod


class Sulfuras(Item):

    def __init__(self, name, sell_in, quality, sell_in_mod=BaseMod(), quality_mod=BaseMod()):
        super().__init__(name, sell_in, quality)
        self.sell_in_mod = sell_in_mod
        self.quality_mod = quality_mod

    def update(self):
        '''
        :param item: Item of type Aged Brie
        :return: None
        Sulfuras has fixed quality, fixed sell_in
        '''
        pass