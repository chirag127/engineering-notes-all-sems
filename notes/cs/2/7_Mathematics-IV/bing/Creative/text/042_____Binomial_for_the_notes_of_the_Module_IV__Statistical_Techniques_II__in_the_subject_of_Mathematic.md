### Binomial Distribution

- A binomial distribution is a discrete probability distribution that gives only two possible results in an experiment, either Success or Failure .
- For example, if we toss a coin, there could be only two possible outcomes: heads or tails, and if any test is taken, then there could be only two results: pass or fail.
- A binomial distribution is characterized by three parameters: n, p, and q, where n is the number of trials, p is the probability of success in each trial, and q is the probability of failure in each trial (q = 1 - p).
- The probability mass function (PMF) of a binomial distribution is given by:

![PMF of binomial distribution](https://latex.codecogs.com/png.latex?P%28X%3Dk%29%3D%5Cbinom%7Bn%7D%7Bk%7Dp%5Ekq%5E%7Bn-k%7D)

where ![binomial coefficient](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bk%7D) is the binomial coefficient, which is the number of ways to choose k successes out of n trials.

- The mean and variance of a binomial distribution are given by:

![mean and variance of binomial distribution](https://latex.codecogs.com/png.latex?%5Cmu%3DE%28X%29%3Dnp%2C%5Cquad%5Csigma%5E2%3DVar%28X%29%3Dnpq)

- A binomial distribution is a special case of a Bernoulli distribution, where the number of trials is one (n = 1).
- A binomial distribution can be approximated by a normal distribution when n is large and p is not too close to 0 or 1 . The normal approximation is given by:

![normal approximation of binomial distribution](https://latex.codecogs.com/png.latex?X%5Csim%20N%28np%2Cnpq%29)

- A binomial distribution can be used to model various real-world phenomena, such as the number of heads in a series of coin tosses, the number of defective items in a batch of products, the number of voters who prefer a certain candidate in an election, etc.