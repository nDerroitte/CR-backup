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

Item Quality decays over days, for each day the quality of an item will decrease of one unity. 

However, there is an exception for items: "Aged Brie", "Backstage passes", and "Sulfuras items".


** Item quality to Sell-in relationship **

When the sell-in has passed it goes to minus two per day.

While the sell-in can be a negative value and will continue decrease over days, the quality can't go below zero and will decrease each days until it reaches zero. 

Also an item quality can't go above 50. Expected for the Sulfuras, 'Hand of Ragnaros' item.

** About specific item rules **

- Sulfuras is legendary which means that it sel_in value stays at its intital value, and the quality will always be equal to 80.

- Aged Brie item: It's quality increases each day until it arrives at a cap of 50. 

- Backstage passes item: It's quality will increase each day. When the sell_in date is within ten days, it's quality will increase of two each day.

When the sell_in date is within 5days, it's quality will increase of three each day. Once it passes sell-in it has a quality of zero. 

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
