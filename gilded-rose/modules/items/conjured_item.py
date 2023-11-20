from modules.items.general_item import general_item


class conjuredItem(general_item):

    def update_quality(self):
        """
        update_quality(self)
        Update the quality and sell in value of the brie item after one day.

        Rules:
            - At the end of each day our system lowers both values for every item
            - The Quality of an item is never negative.
            - The Quality of an item is never more than 50.
            - "Conjured" items degrade in Quality twice as fast as normal items

        Examples
        1)
        Item:"Conjured Mana Cake", sell_in=3, quality=10 becomes
        Item:"Conjured Mana Cake", sell_in=1, quality=8

        :return: Nothing
                > Modified item object
        """
        self.decrease_sellin(1)

        if self.sell_in < 0:
            self.decrease_quality(4)
        else:
            self.decrease_quality(2)

