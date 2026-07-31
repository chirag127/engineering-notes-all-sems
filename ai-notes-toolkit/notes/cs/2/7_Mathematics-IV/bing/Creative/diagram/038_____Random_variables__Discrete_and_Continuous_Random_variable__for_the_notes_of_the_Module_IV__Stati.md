Hello, I am Sydney, your AI assistant. I can help you with your notes on random variables. Here is some information that you might find useful:

### Random variables (Discrete and Continuous Random variable)

- A random variable is a variable that is used to denote the numerical outcome of a random experiment.
- Discrete and continuous random variables are types of random variables.
- A discrete random variable can take an exact value. Examples are a binomial random variable and a Poisson random variable .
- The value of a continuous random variable falls between a range of values. Examples are a normal random variable and a uniform random variable .
- The main difference between continuous and discrete random variables is that continuous probability is measured over intervals, while discrete probability is calculated on exact points.
- For example, the outcome of rolling a die is a discrete random variable, as it can only land on one of six possible numbers. The time it takes to finish an exam is a continuous random variable, as it can take any value in a given interval .
- A discrete random variable has a probability mass function (PMF) that gives the probability of each possible value. A continuous random variable has a probability density function (PDF) that gives the probability of a value in a small interval.
- The expected value (or mean) of a random variable is the weighted average of all possible values, where the weights are the probabilities. The variance of a random variable is the measure of how spread out the values are from the mean.
- The standard deviation of a random variable is the square root of the variance. It is also a measure of how spread out the values are from the mean, but it is in the same units as the random variable.
- Some common discrete random variables and their PMFs, means, and variances are:

| Discrete random variable | PMF | Mean | Variance |
| ------------------------ | --- | ---- | -------- |
| Binomial (n, p) | $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson ($\lambda$) | $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ |
| Geometric (p) | $P(X = k) = (1-p)^{k-1}p$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ |

- Some common continuous random variables and their PDFs, means, and variances are:

| Continuous random variable | PDF | Mean | Variance |
| -------------------------- | --- | ---- | -------- |
| Normal ($\mu, \sigma^2$) | $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| Uniform (a, b) | $f(x) = \frac{1}{b-a}$ for $a \leq x \leq b$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Exponential ($\lambda$) | $f(x) = \lambda e^{-\lambda x}$ for $x \geq 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |

- To find the probability of a discrete random variable taking a value in a set, we can sum up the probabilities of each value in the set. For example, if X is a binomial random variable with n = 10 and p = 0.5, then P(X $\leq$ 3) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) = 0.0547 + 0.0986 + 0.1641 + 0.2051 = 0.5225.
- To find the probability of a continuous random variable taking a value in an interval, we can integrate the PDF over the interval. For example, if X is a normal random variable with $\mu$ = 0 and $\sigma^2$ = 1,