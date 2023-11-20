from modules.item import Item


class ageBrieItem(Item):
    """
    ageBrieItem extends abstractItem

    Class related to the items of Age Brie.
    """

    def update_quality(self):
        """
        update_quality(self)
        Update the quality and sell in value of the brie item after one day.

        Rules:
            - At the end of each day our system lowers the SellIn value
            - "Aged Brie" actually increases in Quality the older it gets.
            - The Quality of an item is never negative.
            - The Quality of an item is never more than 50.
        Example:
        1)
        Item: "Aged Brie, sellIn=2, quality=0" becomes
        Item:"Aged Brie, sellIn=1, 1"
        2)
        Item:"Aged Brie, sellIn=-2, quality=40" becomes
        Item:"Aged Brie, sellIn=-3, quality=42"


        :return: Nothing
                > Modified item object
        """
        self.decrease_sellin(1)

        if self.sell_in < 0:
            self.increase_quality(2)
        else:
            self.increase_quality(1)
