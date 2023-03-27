### Discrete and Continuous Probability Distributions

Probability distribution is a fundamental concept in statistics and probability theory. In this section, we will explore two types of probability distributions: discrete and continuous probability distributions.

#### Discrete Probability Distributions

A discrete probability distribution is a probability distribution that assigns probabilities to a finite or countable set of outcomes. In other words, the distribution only takes on a finite or countably infinite number of values. 

Some common examples of discrete probability distributions include the binomial distribution, the Poisson distribution, and the geometric distribution.

##### Binomial Distribution

The binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent trials. It is characterized by two parameters: n, the number of trials, and p, the probability of success in each trial. The probability mass function (PMF) of the binomial distribution is given by:

P(X=k) = (n choose k) * p^k * (1-p)^(n-k)

where X is the number of successes, k is the number of successes, n is the number of trials, p is the probability of success in each trial, and (n choose k) is the binomial coefficient.

##### Poisson Distribution

The Poisson distribution is a discrete probability distribution that describes the number of events in a fixed interval of time or space. It is characterized by one parameter, lambda, which is the expected number of events in the interval. The probability mass function (PMF) of the Poisson distribution is given by:

P(X=k) = (e^(-lambda) * lambda^k) / k!

where X is the number of events, k is the number of events, lambda is the expected number of events, e is the mathematical constant e, and k! is the factorial of k.

##### Geometric Distribution

The geometric distribution is a discrete probability distribution that describes the number of trials needed to achieve the first success in a sequence of independent trials. It is characterized by one parameter, p, which is the probability of success in each trial. The probability mass function (PMF) of the geometric distribution is given by:

P(X=k) = (1-p)^(k-1) * p

where X is the number of trials needed to achieve the first success, k is the number of trials needed to achieve the first success, p is the probability of success in each trial.

#### Continuous Probability Distributions

A continuous probability distribution is a probability distribution that assigns probabilities to an uncountably infinite set of outcomes. In other words, the distribution takes on an infinite number of values. 

Some common examples of continuous probability distributions include the normal distribution, the uniform distribution, and the exponential distribution.

##### Normal Distribution

The normal distribution is a continuous probability distribution that describes a continuous random variable that is symmetric and bell-shaped. It is characterized by two parameters: mu, the mean of the distribution, and sigma, the standard deviation of the distribution. The probability density function (PDF) of the normal distribution is given by:

f(x) = (1 / (sigma * sqrt(2*pi))) * e^(-((x-mu)^2 / (2*sigma^2)))

where x is a value of the random variable, mu is the mean of the distribution, sigma is the standard deviation of the distribution, e is the mathematical constant e, pi is the mathematical constant pi.

##### Uniform Distribution

The uniform distribution is a continuous probability distribution that describes a continuous random variable that is equally likely to take on any value within a specified range. It is characterized by two parameters: a, the minimum value of the distribution, and b, the maximum value of the distribution. The probability density function (PDF) of the uniform distribution is given by:

f(x) = 1 / (b-a)

where x is a value of the random variable, a is the minimum value of the distribution, and b is the maximum value of the distribution.

##### Exponential Distribution

The exponential distribution is a continuous probability distribution that describes the time between events in a Poisson process. It is characterized by one parameter, lambda, which is the rate of the Poisson process. The probability density function (PDF) of the exponential distribution is given by:

f(x) = lambda * e^(-lambda*x)

where x is a value of the random variable, lambda is the rate of the Poisson process, e is the mathematical constant e.