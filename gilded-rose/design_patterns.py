# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

# Implement a dynamic wrapper around the Item object which limits the values that quality can take
# https://python-patterns.guide/gang-of-four/decorator-pattern/

class ItemWrapper:
    def __init__(self, name, sell_in, quality) -> None:
        self._item = Item(name, sell_in, quality)

    @property
    def quality(self):
        return self._item.quality
    
    @quality.setter
    def quality(self, value):
        if value > 50:
            self._item.quality = 50

        elif value < 0:
            self._item.quality = 0

        else:
            self._item.quality = value

    def __getattr__(self, name):
        return getattr(self.__dict__['_item'], name)

    def __setattr__(self, name, value):
        setattr(self.__dict__['_item'], name, value)

    def __delattr__(self, name):
        delattr(self.__dict__['_item'], name)
        