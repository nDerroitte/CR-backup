======================================
Gilded Rose Requirements Specification
======================================

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We
have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:

	- All items have a SellIn value which denotes the number of days we have to sell the item
	- All items have a Quality value which denotes how valuable the item is
	- At the end of each day our system lowers both values for every item

Pretty simple, right? Well this is where it gets interesting: Leeroy didn't document everything properly,
we are now left in quite the mess ! Here's what he left
```

** About Item Quality **

Item quality denotes how valuable the item is. An item quality can never be above 50.

** Item quality to Sell-in relationship **

The item quality degrades by 1 point for every day that they are approaching the sell-in date.

** About specific item rules **

- Sulfuras is legendary which means that the quality is 80 and it never alters.
- Aged Brie & Backstage passes do something special, although not the same thing
When the quality of Aged Brie is below 50, the quality increases for every day that they are approaching the sell-in date. For backstage passes, if the item quality is below 50 and the sell-in date is within 11 days, it increases the quality by 2. If it is within 6 days, it increases by 3.

```
We have recently signed a supplier of conjured items. This requires an update to our system:

- "Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes to the method and add any new code as long as everything
still works correctly. However, do not alter the Item class or Items property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover
for you).

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
legendary item and as such its Quality is 80 and it never alters.
