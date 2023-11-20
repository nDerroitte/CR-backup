class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increase_quality(self, coef):
        """
        Increase the quality of the item by the coef to a max value of 50

        :param coef: numeric value to increase the quality
        :return: Nothing
                > Modified item object
        """
        if self.quality < 50:
            self.quality = min(self.quality + coef, 50)

    def decrease_quality(self, coef):
        """
        Decrease the quality of the item by the coef to a max value of 0

        :param coef: numeric value to decrease the quality
        :return: Nothing
                > Modified item object
        """
        if self.quality > 0:
            self.quality = max(self.quality - coef, 0)

    def decrease_sellin(self, coef):
        """
        Decrease the SellIn of the item by the coef

        :param coef: numeric value to decrease the SellIn
        :return: Nothing
                > Modified item object
        """
        self.sell_in -= coef