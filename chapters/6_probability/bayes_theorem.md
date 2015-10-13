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

 * P(A|B) = Chance of `A`, given a positive test result `B`.
 * P(B|A) = Chance of a positive test result `B` given `A`.
 * P(A) = Chance of `A`
 * P(not A) = Chance of not `A`.
 * P(B|not A) = Chance of a positive test result `B` given not `A`.

#### The Classic Example - Mamograms

The classic Bayes' Theorem example is the mamogram.

Let's say we know some things about the mamogram test:

 * 1% of women have breast cancer
 * a mamogram will catch breast cancer 80% of the time
 * 10% of women without breast cancer will test positive during a mamogram

To put this in the terminology of Bayes' Theorem:

 * P(A) = 0.01
 * P(B|A) = 0.8
 * P(B|not A) = 0.1

Of course, since we know those things, we also know the converse of each:

 * P(not A) = 0.99
 * P(not B|A) = 0.2
 * P(not B|not A) = 0.9

So we might draw a True/False, Positive/Negative probability table like this:

| Has Cancer    | True | False |
| ------------- | ---- | ----- |
| Test Positive | 0.8  | 0.1   |
| Test Negative | 0.2  | 0.9   |

But that table isn't the whole story, it's just the raw data. What if you want to know:

> You just got your mamogram result, now what is the chance you really have cancer?

We can now calculate the chance of getting *any* positive result:

    P(B) = P(B|A) * P(A) + P(B|not A) * P(not A)
    P(B) = 0.8 * 0.01 + 0.1 * 0.99 = 0.107

The chance that you have cancer, given a positive test result:

    P(A|B) = P(B|A) * P(A) / P(B)
    P(A|B) = 0.8 * 0.01 / 0.107 = 0.075

And the chance that you have cancer, given a negative test result:

    P(A|not B) = P(not B|A) * P(A) / P(not B)
    P(A|not B) = P(not B|A) * P(A) / [P(not B|A) * P(A) + P(not B|not A) * P(not A)]
    P(A|not B) = 0.2 * 0.01 / [0.2 * 0.01 + 0.9 * 0.99] = 0.022

This is a key difference in interpretting your test result: `P(A|B)` vs `P(B|A)`. Before you even got your test done, you knew that the test would only identify breast cancer 80% of the time (`P(B|A)`). But now that you have a positive result, you know you still only have a 7.5% chance of having cancer. This is because it is *far* more likely that your test is a False Positive.

Now we can re-draw the table above and list what people really want to know:

> What is the chance that you have breast cancer, given your test result:

|                      | Real Chance of Cancer |
| -------------------- | :-------------------: |
| Positive Test Result |        0.075          |
| Negative Test Result |        0.022          |

#### Interpretting Bayes' Theorem

 * coming soon

#### More Examples - Practice, Practice, Practice

 * coming soon

#### References

Seemingly every pocket protector on the intertubes has their own explanation for Bayes' Theorem. Caveat emptor.

Here are some of the more helpful links:

 * [Wikipedia - Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
 * [BetterExplained - Bayes' Theorem](http://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/)
 * [Oscar Bonilla - Bayes' Theorem](https://oscarbonilla.com/2009/05/visualizing-bayes-theorem/)
 * [New Yorker- What Nate Silver Gets Wrong](http://www.newyorker.com/books/page-turner/what-nate-silver-gets-wrong)
