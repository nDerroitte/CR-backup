# -*- coding: utf-8 -*-
from modules.item_classes import *
from modules.type_factory import *

class GildedRose(object):

    def __init__(self, items):
        factory = TypeFactory()
        items_new =[]
        for item in items:
            element = factory.create_item(item) 
            items_new.append(element)
        self.items = items_new


    def update_quality(self):
        for item in self.items:
            item.update_quality() 
            
            

        