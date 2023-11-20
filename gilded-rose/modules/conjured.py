from modules.plain_object import PlainObject


class Conjured(PlainObject):
    def update_quality(self):
        super().update_quality()
        super().update_quality()
        self.sell_in += 1
