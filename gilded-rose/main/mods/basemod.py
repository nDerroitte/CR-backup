from main.mods.IMod import IMod
class BaseMod(IMod):
    """
    Base Mod : Returns value 1 to 1
    """
    def update_value(self, val: int):
        """
        :param int val: value to be modified by the mod object
        """
        return val