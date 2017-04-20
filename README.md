## Assorted Scripts

Sometimes you just need a place to stick random code that doesn't have anywhere else to live. Most of this stuff is one-off toys that I made on a whim; they might be incorporated into larger projects later but for now I'm satisfied to let them stand alone.

#### blackwellsbet.dart

**Blackwell's Bet**

Showing off a strange, unintuitive mathematical principle. Say you have two integers, *x* and *y*. You know the value of x, but not the value of y, and are asked to guess whether y is larger or smaller than x. This seems like a situation where the best you can do is 50/50, but it turns out that there's a way to improve your odds: create a random number *d*. If d is greater than x, guess that y is greater; if d is less than x, guess that y is less. This significantly improves your odds of guessing correctly - in fact, if the ranges from which x, y, and d are picked are all the same (this code defaults to 0-9999), your odds improve to 66% if you use d as a pseudo-predictive tool.

[Here's more information about it.](https://www.futilitycloset.com/2016/06/28/blackwells-bet/)

Written in Dart 1.22.1.

#### kellyanne.py

**Kellyanne Warns!**

Written in the aftermath of the tragic Bowling Green massacre, this bot continues to keep America on its toes by reminding us of the danger shown by other fictional tragedies.

You can see her in action [here](https://www.twitter.com/kellyanne_warns); the account is powered by a cron job.

Written in Python 3.5. Requires Twython.

#### mccoy_ebooks.py

**McCoy_ebooks**

Damn it, Jim, I'm a doctor, not a <random noun>!

You can see him in action [here](https://www.twitter.com/mccoy_ebooks). (The account is not automated and only updates when I remember to run the script.)

Written in Python 3.5. Requires Twython.

#### newArray.rb

**Array modifications**

Some utility functions for arrays in Ruby, useful for including in larger scripts.

Written in Ruby 2.4.
