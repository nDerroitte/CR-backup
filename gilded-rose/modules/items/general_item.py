from modules.item import Item


class general_item(Item):

    def update_quality(self):
        """
        update_quality(self)
        Update the quality and sell in value of the brie item after one day.

        Rules:
            - At the end of each day our system lowers both values for every item
            - The Quality of an item is never negative.
            - The Quality of an item is never more than 50.

        Examples
        1)
        Item:"+5 Dexterity Vest", sell_in=10, quality=20 becomes
        Item:"+5 Dexterity Vest", sell_in=9, quality=19
        2)
        Item:"Elixir of the Mongoose", sell_in=-5, quality=7 becomes
        Item:"Elixir of the Mongoose", sell_in=-6, quality=5

        :return: Nothing
                > Modified item object
        """
        self.decrease_sellin(1)

        if self.sell_in < 0:
            self.decrease_quality(2)
        else:
            self.decrease_quality(1)

