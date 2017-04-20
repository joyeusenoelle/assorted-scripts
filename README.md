## Assorted Scripts

Sometimes you just need a place to stick random code that doesn't have anywhere else to live. Most of this stuff is one-off toys that I made on a whim; they might be incorporated into larger projects later but for now I'm satisfied to let them stand alone.

#### Blackwell's Bet

    blackwellsbet.dart

Showing off a strange, unintuitive mathematical principle. Say you have two integers, *x* and *y*. You know the value of x, but not the value of y, and are asked to guess whether y is larger or smaller than x. This seems like a situation where the best you can do is 50/50, but it turns out that there's a way to improve your odds: create a random number *d*. If d is greater than x, guess that y is greater; if d is less than x, guess that y is less. This significantly improves your odds of guessing correctly - in fact, if the ranges from which x, y, and d are picked are all the same (this code defaults to 0-9999), your odds improve to 66% if you use d as a pseudo-predictive tool.

[Here's more information about it.](https://www.futilitycloset.com/2016/06/28/blackwells-bet/)
