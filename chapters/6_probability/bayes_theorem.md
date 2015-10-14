# Bayes' Theorem

In the trenches of science, no battle has lasted longer or become more fierce than the one between Frequentists and Bayesians. If you think no one is going to war over probability theory, you're wrong. And don't let anyone tell you that one side has claimed victory. Thomas Bayes died in 1761 and at this point it is a holy war; no one will win. The best you can do is understand the two approaches and give them both a healthy dose of skepticism. 

To that end, let's take a look at Bayes' Theorem.

#### The Equation

Like a lot of great ideas, Bayes' Theorem can be written down in a single equation, but understanding all the implications takes time.

    P(A|B) = P(A) * P(B|A) / P(B)

or, expanding `P(B)`:

    P(A|B) = P(A) * P(B|A) / [P(B|A) * P(A) + P(B|not A) * P(not A)]

where this notation means:

 * `P(X)` means "probability of X"
 * `X|Y` means "X given Y"
 * `A` is what we are interested in measuring the probability of
 * `B` is the test result we measured

Or, defining each term conceptually:

 * P(A) = Chance of `A` actually being true.
 * P(B) = Chance of any positive test result (false positive OR true positive).
 * P(A|B) = Chance of `A`, given a positive test result `B`.
 * P(B|A) = Chance of a positive test result `B` given `A`.
 * P(not A) = Chance of not `A`.
 * P(B|not A) = Chance of a positive test result `B` given not `A`.

#### The Classic Example - Mamograms

A classic Bayes' Theorem example is the mamogram.

Because such a large number of women have had mamograms and/or breast cancer, there is a lot of data avaailble for scientists to analyze the effectiveness of the mamogram. Here are the results of those analysis:

 * 1% of women have breast cancer
 * a mamogram will catch breast cancer 80% of the time
 * 10% of women without breast cancer will test positive during a mamogram

To put this in the terminology of Bayes' Theorem:

 * P(A) = 0.01
 * P(B|A) = 0.8
 * P(B|not A) = 0.1

And we can easily calculate the converse of each:

 * P(not A) = 0.99
 * P(not B|A) = 0.2
 * P(not B|not A) = 0.9

So we might draw a True/False, Positive/Negative probability table like this:

| Has Cancer    | True | False |
| ------------- | ---- | ----- |
| Test Positive | 0.8  | 0.1   |
| Test Negative | 0.2  | 0.9   |

But that isn't the whole story, it's just data. What a patient will want to know is:

> I just got my mamogram result, now what is the chance I have cancer?

First, we can calculate the chance of getting *any* positive result:

    P(B) = P(B|A) * P(A) + P(B|not A) * P(not A)
    P(B) = 0.8 * 0.01 + 0.1 * 0.99 = 0.107

The chance that you have cancer, given a positive test result:

    P(A|B) = P(B|A) * P(A) / P(B)
    P(A|B) = 0.8 * 0.01 / 0.107 = 0.075

And the chance that you have cancer, given a negative test result:

    P(A|not B) = P(not B|A) * P(A) / P(not B)
    P(A|not B) = P(not B|A) * P(A) / [P(not B|A) * P(A) + P(not B|not A) * P(not A)]
    P(A|not B) = 0.2 * 0.01 / [0.2 * 0.01 + 0.9 * 0.99] = 0.002

This is a key difference in interpretting your test result: `P(A|B)` vs `P(B|A)`. You know the mamogram will only identify breast cancer 80% of the time (`P(B|A)`). But now that you have a positive result, you know you still only have a 7.5% chance of having cancer. This is because it is *far* more likely that your test is a False Positive.

Now we can re-draw the table above and list what people really want to know:

> What is the chance that you have breast cancer, given your test result?

|                      | Real Chance of Cancer |
| :------------------- | :-------------------: |
| Positive Test Result |        0.075          |
| Negative Test Result |        0.002          |

So, what have we learned? Getting a positive result on a mamogram is reason enough to do more testing, but you still only have a 7.5% chance of having breast cancer; stay calm. And if you get a negative result, you only have a 0.2% chance of cancer; rest easy (but get tested again next year).

#### Interpretting Bayes' Theorem

Obviously, in order to use Bayes' Theorem you need a lot of information. If you get the information from hard data, as is the case for mamograms above, we call those [posterior probabilities](https://en.wikipedia.org/wiki/Posterior_probability). If, on the other hand, no data is available and you have to make assumptions, we all these [prior probabilities](https://en.wikipedia.org/wiki/Prior_probability).

In the real world, we often find ourselves in the situation of having to create some "uninformed prior assumptions". For instance, let us place ourselves in the mind a 50-year-old woman living in the year 2041 in Nihonmatsu, Japan. At the age of 20, the Fukushima nuclear power plant disaster occured, and we spent our whole life in Nihonmatsu, the city closest to the Fukushima Exclusion Zone.

If we are a positive person, we might say that nothing has changed from the mamogram scenario above. But perhaps we are a very negative person and think that 3% of women in Nihonmatsu will have breast cancer (a dramatic increase from the world average of 1%). This would change significantly change how we interpret our mamogram results:

    P(A|B) = P(B|A) * P(A) / P(B)
    P(A|B) = 0.8 * 0.03 / (0.8 * 0.03 + 0.1 * 0.97) = 0.198

    P(A|not B) = P(not B|A) * P(A) / P(not B)
    P(A|not B) = P(not B|A) * P(A) / [P(not B|A) * P(A) + P(not B|not A) * P(not A)]
    P(A|not B) = 0.2 * 0.03 / (0.2 * 0.03 + 0.9 * 0.97) = 0.007

Our expectation of the effectiveness of the mamogram test itself hasn't changed, but `P(A)` and `P(B)` have. This gives us the far more pessimistic table of results:

|                      | Real Chance of Cancer |
| :------------------- | :-------------------: |
| Positive Test Result |        0.198          |
| Negative Test Result |        0.007          |

Let us imagine another scenario. Perhaps it in the year 2041 the mamogram test will be more effective. So instead of only an 80% chance of identifying cancer, it has a 95% of chance (`P(B|A) = 0.95`). Assuming the worldwide rate of breast cancer remains at 1%, we would find:

    P(A|B) = P(B|A) * P(A) / P(B)
    P(A|B) = 0.95 * 0.01 / (0.95 * 0.01 + 0.1 * 0.99) = 0.087

    P(A|not B) = P(not B|A) * P(A) / P(not B)
    P(A|not B) = P(not B|A) * P(A) / [P(not B|A) * P(A) + P(not B|not A) * P(not A)]
    P(A|not B) = 0.05 * 0.01 / [0.05 * 0.01 + 0.95 * 0.99] = 0.0005

In this situation we could interpret our results to mean:

|                      | Real Chance of Cancer |
| :------------------- | :-------------------: |
| Positive Test Result |        0.087          |
| Negative Test Result |        0.0005         |

One can imagine this kind of analysis is also useful to the designers of mamogram equipment. They currently only identify 80% of breast cancer (`P(B|A)`) and 10% of women without breast cancer get positive results (`P(B|not A)`). In an ideal world they would improve both of these numbers. But no one has infinite money, so they must decide *where* they want to spend their R&D money first. If the goal is to improve the confidence of patients who take the test, the tables above could be recreated with various values of `P(B|A)` and `P(B|not A)` to see which will be the most effective for the least amount of money.

#### The Monty Hall Problem

> A classic example of how just a little math can change the way you see the world.

Once upon a time there was a TV game show called "Let's Make a Deal". A contestant was brought on stage and shown three doors, behind one was a new car. First, the contestant would select a door. Then the host (Monty Hall) would open a different door that contained nothing. The contestant then had the chance to either stick with their door or switch to the remaining unopened door.

The surprising result is that it is *always* a better idea to switch to the new door than to stay with your original choice.

Let us analyze the game using Bayes' Theorem. First, we will make some definitions:

 * The doors in question are labeled: `A`, `B`, and `C`.
 * The door you choose first is `A`.
 * The door the host reveals is `B`.

We already know some of the probabilities involved:

 * The chance of the car is behind door `X` is 1 in 3: `P(X) = 1/3`.
 * The chance that Monty opens door `B` if the car is behind `A` is 1 in 2: `P(Monty opens B|A) = 1/2`.
 * The chance that Monty opens door `B` if the car is behind `B` is zero: `P(Monty opens B|B) = 0`.
 * The chance that Monty opens door `B` if the car is behind `C` is: `P(Monty opens B|C) = 1`.

That is all of our prior knowledge of the situation. Now let's write down Bayes' Theorem for your two choices:

If you stick with door `A`:

    P(A|Monty opens B) = P(A) * P(Monty opens B|A) / P(Monty opens B)

If you switch to door `C`:

    P(C|Monty opens B) = P(C) * P(Monty opens B|C) / P(Monty opens B)

The denominator to both equations are the same. In order to calculate the chance that Monty will open door `B`, we need to consider the possibility that the car is behind each of the three doors:

    P(Monty opens B) = P(A) * P(Monty opens B|A) + P(B) * P(Monty opens B|B) + P(C) * P(Monty opens B|C)
                     = (1/3 * 1/2) + (1/3 * 0) + (1/3 * 1) = 1/6 + 0 + 1/3
                     = 1/2

Now we can solve our two equations.

If you stick with door `A`:

    P(A|Monty opens B) = P(A) * P(Monty opens B|A) / P(Monty opens B)
                       = 1/3 * 1/2 / 1/2
                       = 1/3

If you switch to door `C`:

    P(C|Monty opens B) = P(C) * P(Monty opens B|C) / P(Monty opens B)
                       = 1/3 * 1 / 1/2
                       = 2/3

There you have it. Your chances of winning the car double if you switch to the other door.

For many, this result does not seem intuitively right. *Why* would switching to the other door increase your chances? The usual argument here is that it seems more intuitive that each of the two remaining doors should have a 50% chance of being right. But this is too simple. When the contestant picks the first door they have a 1-in-3 chance: it's totally random. But the door Monty Hall opens isn't random, because he can't select the door with the car behind it. And you have to take into account two scenarios. In scenario (a) you selected the right door and Monty can pick either of the others. In scenario (b) you selected the wrong door and Monty only has one option. But scenario (b) is twice as likely as scenario (a). So it's a good idea to act like you're in scenario (b), which means switching your door choice.

Are you *still* not convinced? It's good to be a skeptic. One thing we can do is use computers to simulate the game many thousands of times and see what happens. If you are familiar with Python, check out [this iPython notebook that simulates the Monty Hall Game](monty_hall_problem.ipynb). See for yourself, switching your door doubles your chances of winning a car.

#### References

Seemingly every pocket protector on the intertubes has their own explanation for Bayes' Theorem. Caveat emptor.

Here are some of the more helpful links:

 * Bayes' Theorem Explained
     * [Wikipedia - Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
     * [BetterExplained - Bayes' Theorem](http://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/)
     * [Oscar Bonilla - Bayes' Theorem](https://oscarbonilla.com/2009/05/visualizing-bayes-theorem/)
     * [New Yorker- What Nate Silver Gets Wrong](http://www.newyorker.com/books/page-turner/what-nate-silver-gets-wrong)
 * Jargon
     * [Wikipedia - Prior Probability](https://en.wikipedia.org/wiki/Prior_probability)
     * [Wikipedia - Posterior Probability](https://en.wikipedia.org/wiki/Posterior_probability)
 * Examples
     *  [Curiouser - The Monty Hall Problem](http://www.curiouser.co.uk/monty/montyhall2.htm)
     *  [Stat Trek - Rain on Your Wedding Day example](http://www.stattrek.com/probability/bayes-theorem.aspx)
     *  [Statlect - 3 examples](http://www.statlect.com/bayes_rule_exercise_set_1.htm)
