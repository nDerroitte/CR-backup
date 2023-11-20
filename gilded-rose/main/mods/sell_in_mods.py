# Sell-in values are decreased twice as fast
from main.mods.IMod import IMod
import random

class PuzzlingMod(IMod):

    def update_value(self, val):
        r = random.randint(1,10)
        if r == 1:
            return val
        
        elif r >= 2 and r<=5:
            return val - 1
        
        else:
            return val + 1
        

class TimelessMod(IMod):

    def update_value(self, val):
        return 0