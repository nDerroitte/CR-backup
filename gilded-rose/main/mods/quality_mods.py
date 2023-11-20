# Quality is impacted twice as much as a usual item

from main.mods.IMod import IMod

class ConjuredMod(IMod):

    def update_value(self,val: int) -> int:
        """
        Returns modified value
        """
        return val * 2

class HighQualityMod(IMod):

    def update_value(self,val: int) -> int:
        """
        Returns modified value
        """
        if val < 0:
            return int(val/2)
        else:
            return val