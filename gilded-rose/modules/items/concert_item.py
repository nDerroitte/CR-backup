from modules.item import Item


class concertItem(Item):

    def update_quality(self):
        """
        update_quality(self)
        Update the quality and sell in value of the brie item after one day.

        Rules:
            - At the end of each day our system lowers the SellIn value
            - The Quality of an item is never negative.
            - The Quality of an item is never more than 50.
            - "Backstage passes" increases in Quality as its SellIn value approaches
            - Quality increases by 2 when there are 10 days or less
            - Quality increases by 3 when there are 5 days or less
            - Quality drops to 0 after the concert

        Examples
        1)
        Item:"Backstage passes to a TAFKAL80ETC concert, sell_in=15, quality=20" becomes
        Item:"Backstage passes to a TAFKAL80ETC concert, sell_in=14, quality=21"
        2)
        Item:"Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=30 becomes
        Item:"Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=33,

        :return: Nothing
                > Modified item object
        """
        self.decrease_sellin(1)

        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.increase_quality(3)
        elif self.sell_in < 10:
            self.increase_quality(2)
        else:
            self.increase_quality(1)
