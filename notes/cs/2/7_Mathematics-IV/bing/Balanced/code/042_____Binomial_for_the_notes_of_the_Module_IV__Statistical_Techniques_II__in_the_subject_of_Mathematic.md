### Binomial Distribution

- Binomial distribution is a type of probability distribution that describes the possible outcomes of a series of independent trials, where each trial has only two possible outcomes, such as success or failure, yes or no, or on or off.
- Binomial distribution is defined by two parameters: the number of trials (n) and the probability of success (p) in each trial. The probability of getting exactly x successes in n trials is given by the formula:

![binomial formula](https://www.investopedia.com/thmb/9x1xQ0nZ0f0y0w7wQ1Z1a0Zf0sE=/1279x853/smart/filters:no_upscale()/binomialdistribution-5c3e0f0ec9e77c0001a9a9f0.png)

- Binomial distribution has some important properties, such as:

  - The mean of the binomial distribution is np.
  - The variance of the binomial distribution is np(1-p).
  - The standard deviation of the binomial distribution is sqrt(np(1-p)).
  - The binomial distribution is symmetric when p = 0.5, skewed to the right when p < 0.5, and skewed to the left when p > 0.5.
  - The binomial distribution approaches the normal distribution when n is large and p is not too close to 0 or 1.

- Binomial distribution is used to model various real-life situations, such as:

  - The number of heads in a series of coin flips.
  - The number of yes votes in a survey.
  - The number of defective items in a batch of products.
  - The number of free throws made by a basketball player.

- Binomial distribution can be calculated using the binomial probability formula, or using the binompdf and binomcdf functions in a calculator or software. The binompdf function gives the probability of getting a specific number of successes, while the binomcdf function gives the cumulative probability of getting up to a certain number of successes. For example:

  - The probability of getting exactly 3 heads in 5 coin flips is binompdf(5, 0.5, 3) = 0.3125.
  - The probability of getting at most 2 heads in 5 coin flips is binomcdf(5, 0.5, 2) = 0.5.