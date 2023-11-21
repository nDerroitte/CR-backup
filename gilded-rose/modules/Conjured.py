from modules.GeneralItem import GeneralItem

class Conjured(GeneralItem):
    def update_quality(self):
        super().update_quality()
        super().update_quality()
        self.sell_in += 1