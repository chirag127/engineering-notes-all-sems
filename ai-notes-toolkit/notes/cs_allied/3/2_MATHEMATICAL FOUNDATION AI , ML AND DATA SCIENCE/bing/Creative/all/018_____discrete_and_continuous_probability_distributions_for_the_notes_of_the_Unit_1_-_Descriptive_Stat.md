# Discrete and Continuous Probability Distributions

## Introduction

A probability distribution is a function that describes the possible values and probabilities of a random variable. A random variable is a variable whose value is determined by the outcome of a random experiment. For example, the number of heads in 10 coin tosses is a random variable.

There are two types of probability distributions: discrete and continuous. A discrete probability distribution is one that applies to a discrete random variable, which can only take a finite or countable number of values. A continuous probability distribution is one that applies to a continuous random variable, which can take any value in a continuous range.

## Discrete Probability Distribution

A discrete probability distribution assigns a probability to each possible value of a discrete random variable. The sum of all the probabilities must be equal to 1. The probability of any value is equal to the number of times it occurs divided by the total number of outcomes.

For example, the probability distribution of the number of heads in 10 coin tosses is a discrete probability distribution. The possible values are 0, 1, 2, ..., 10, and the probabilities are calculated using the binomial formula:

P(X = x) = (10 choose x) * (0.5)^x * (0.5)^(10-x)

The following table shows the probability distribution of the number of heads in 10 coin tosses:

| x | P(X = x) |
|---|----------|
| 0 | 0.00098  |
| 1 | 0.00977  |
| 2 | 0.04395  |
| 3 | 0.11719  |
| 4 | 0.20508  |
| 5 | 0.24609  |
| 6 | 0.20508  |
| 7 | 0.11719  |
| 8 | 0.04395  |
| 9 | 0.00977  |
| 10| 0.00098  |

The sum of all the probabilities is 1, as expected.

Some common examples of discrete probability distributions are the binomial distribution, the Poisson distribution, and the Bernoulli distribution.

## Continuous Probability Distribution

A continuous probability distribution assigns a probability to each possible value of a continuous random variable. However, unlike a discrete probability distribution, the probability of any single value is zero, because there are infinitely many values in a continuous range. Therefore, continuous probability distributions are defined by a probability density function (PDF), which gives the probability of a value in a small interval around that value. The area under the curve of the PDF between two values gives the probability of the random variable being in that range.

For example, the probability distribution of the height of a randomly selected person is a continuous probability distribution. The possible values are any real number between 0 and some maximum height, and the probabilities are given by a PDF that looks like a bell-shaped curve. The probability of a person being exactly 170 cm tall is zero, but the probability of a person being between 169.5 and 170.5 cm tall is the area under the curve between those two values.

The following graph shows the PDF of the height of a randomly selected person, assuming a normal distribution with a mean of 170 cm and a standard deviation of 10 cm:

![PDF of height](https://www.mathsisfun.com/data/images/normal-distrubution-large.svg)

The area under the curve between 169.5 and 170.5 cm is approximately 0.0398, which means the probability of a person being in that range is 0.0398.

Some common examples of continuous probability distributions are the normal distribution, the exponential distribution, and the uniform distribution.