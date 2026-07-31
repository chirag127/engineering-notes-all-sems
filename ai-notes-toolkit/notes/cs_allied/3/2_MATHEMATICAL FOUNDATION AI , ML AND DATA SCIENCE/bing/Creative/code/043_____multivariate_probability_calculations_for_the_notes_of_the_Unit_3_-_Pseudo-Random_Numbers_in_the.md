### Multivariate Probability Calculations

- Multivariate probability is the study of random variables that are jointly distributed, meaning that their outcomes are interdependent or correlated in some way.
- Multivariate probability calculations involve finding the probabilities of events that involve more than one random variable, such as the joint probability, the marginal probability, and the conditional probability.
- Joint probability is the probability of two or more random variables occurring together, denoted by P(X, Y) or P(X and Y). It can be calculated using the multiplication rule, the chain rule, or the table method, depending on the type and number of random variables involved.
- Marginal probability is the probability of one random variable occurring regardless of the other random variables, denoted by P(X) or P(Y). It can be calculated by summing up the joint probabilities over all possible values of the other random variables, or by using the law of total probability.
- Conditional probability is the probability of one random variable occurring given that another random variable has occurred, denoted by P(X|Y) or P(Y|X). It can be calculated using the definition of conditional probability, P(X|Y) = P(X, Y) / P(Y), or by using Bayes' theorem, P(X|Y) = P(Y|X)P(X) / P(Y).
- Multivariate probability distributions are mathematical models that describe the joint behavior of multiple random variables. There are different types of multivariate distributions, such as the multinomial distribution, the multivariate normal distribution, and the Wishart distribution, each with its own assumptions, parameters, and properties.
- Multinomial distribution is a multivariate version of the binomial distribution. It is the probability distribution of the outcomes from a multinomial experiment, which is an experiment that has a fixed number of trials, each with a finite number of possible outcomes, and each trial is independent of the others. The probability of each outcome is constant across the trials. The multinomial distribution can be used to model situations such as dice rolling, voting, or classification problems. The formula for the probability of a particular outcome in a multinomial experiment is:

P(X1 = x1, X2 = x2, ..., Xk = xk) = n! / (x1! x2! ... xk!) * p1^x1 * p2^x2 * ... * pk^xk

where n is the number of trials, k is the number of possible outcomes, xi is the number of times outcome i occurs, and pi is the probability of outcome i.

- Multivariate normal distribution is a generalization of the normal distribution to multiple dimensions. It is the probability distribution of a vector of random variables that are jointly normally distributed, meaning that any linear combination of them is normally distributed. The multivariate normal distribution can be used to model situations such as height and weight, test scores, or stock returns. The formula for the probability density function of a multivariate normal distribution is:

f(x) = (2π)^(-k/2) * |Σ| ^ (-1/2) * exp(-1/2 * (x - μ)' * Σ^(-1) * (x - μ))

where k is the number of random variables, x is the vector of random variables, μ is the vector of means, Σ is the covariance matrix, |Σ| is the determinant of Σ, and Σ^(-1) is the inverse of Σ.

- Wishart distribution is a multivariate version of the chi-square distribution. It is the probability distribution of the sample covariance matrix of a set of random variables that are multivariate normally distributed. The Wishart distribution can be used to model situations such as the variability of stock returns, the precision of measurements, or the uncertainty of estimates. The formula for the probability density function of a Wishart distribution is:

f(X) = |X|^(v - k - 1) / 2 * exp(-1/2 * tr(Σ^(-1) * X)) / (2^(vk/2) * |Σ|^(v/2) * Γk(v/2))

where k is the number of random variables, X is the sample covariance matrix, v is the degrees of freedom, Σ is the population covariance matrix, tr is the trace operator, and Γk is the multivariate gamma function.