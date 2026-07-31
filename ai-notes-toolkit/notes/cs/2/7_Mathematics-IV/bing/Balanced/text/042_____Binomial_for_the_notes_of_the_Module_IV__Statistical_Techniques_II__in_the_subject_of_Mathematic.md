### Binomial Distribution

- A binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials, each with the same probability of success .
- A binomial distribution has the following properties :
  - The number of trials, n, is fixed and known in advance.
  - Each trial has only two possible outcomes: success or failure.
  - The probability of success, p, is constant for each trial.
  - The trials are independent, meaning the outcome of one trial does not affect the outcome of another trial.
- The probability mass function (PMF) of a binomial distribution is given by the formula :
  - P(X = k) = nCk * p^k * (1-p)^(n-k)
  - where X is the random variable that counts the number of successes, k is the number of successes, n is the number of trials, p is the probability of success, and nCk is the binomial coefficient that represents the number of ways to choose k successes out of n trials.
- The mean, variance, and standard deviation of a binomial distribution are given by the formulas :
  - E(X) = np
  - Var(X) = np(1-p)
  - SD(X) = sqrt(np(1-p))
- A binomial distribution can be used to model various real-world scenarios, such as the number of heads in a coin toss, the number of correct answers in a multiple-choice test, the number of defective items in a batch, etc.