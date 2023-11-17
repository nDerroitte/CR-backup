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

By default, every update, the quality decreases by 1. However, there are some exceptions for specific item rules as mentionned beneath.

** Item quality to Sell-in relationship **

By default, every update, the sell-in decreases by 1 except for the Sulfuras.

** About specific item rules **

- Sulfuras is legendary which means the quality and the sell_in doesn't change.
- Aged Brie & Backstage passes increase in quality every day.
	-Aged Brie increases quality by 1 every day
	-Backstage increases by 1 if you have to sell it in 6-10 days and by 2 if you have to sell it in 5 or less days
- Conjured items incxreases in quality twice every day.

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
