# Multivariate Probability Calculations

- Multivariate probability is the study of random variables that are jointly distributed over a sample space. 
- A multivariate probability distribution is a function that assigns probabilities to each possible outcome of a multivariate experiment. 
- A multivariate experiment is one that has more than one random variable of interest, such as the number of heads and tails in a coin toss, or the height and weight of a person. 
- There are different types of multivariate probability distributions, depending on the nature and relationship of the random variables involved. Some common examples are:
  - Multinomial distribution: a generalization of the binomial distribution, where there are more than two possible outcomes for each trial, such as rolling a dice. 
  - Multivariate normal distribution: a generalization of the normal distribution, where each random variable follows a normal distribution and has a linear correlation with the others, such as the scores of students on different tests. 
  - Wishart distribution: a distribution of positive definite matrices, such as the sample covariance matrix of a multivariate normal distribution. 
- To calculate the probability of a multivariate event, we need to use the joint probability mass function (PMF) or the joint probability density function (PDF), depending on whether the random variables are discrete or continuous. 
- The joint PMF or PDF gives the probability of a specific combination of values for the random variables, such as P(X = 2, Y = 3), where X and Y are discrete random variables. 
- The joint PMF or PDF can be obtained from the marginal PMF or PDF and the conditional PMF or PDF, using the product rule or the chain rule of probability. 
- The marginal PMF or PDF gives the probability of a single random variable, ignoring the others, such as P(X = 2), where X is a discrete random variable. 
- The conditional PMF or PDF gives the probability of a random variable, given the values of the others, such as P(X = 2 | Y = 3), where X and Y are discrete random variables. 
- The product rule states that the joint PMF or PDF is equal to the product of the marginal PMF or PDF and the conditional PMF or PDF, such as P(X = 2, Y = 3) = P(X = 2) P(Y = 3 | X = 2). 
- The chain rule states that the joint PMF or PDF is equal to the product of the conditional PMF or PDF for each random variable, such as P(X = 2, Y = 3) = P(X = 2) P(Y = 3 | X = 2) = P(Y = 3) P(X = 2 | Y = 3). 
- To calculate the probability of a multivariate event, we need to sum or integrate over the joint PMF or PDF, depending on whether the random variables are discrete or continuous. 
- For example, to calculate the probability of X + Y = 5, where X and Y are discrete random variables, we need to sum over all possible values of X and Y that satisfy the equation, such as P(X + Y = 5) = P(X = 0, Y = 5) + P(X = 1, Y = 4) + P(X = 2, Y = 3) + P(X = 3, Y = 2) + P(X = 4, Y = 1) + P(X = 5, Y = 0). 
- For example, to calculate the probability of X + Y < 5, where X and Y are continuous random variables, we need to integrate over the region of the joint PDF that satisfies the inequality, such as P(X + Y < 5) = ∫∫(X + Y < 5) f(X, Y) dX dY, where f(X, Y) is the joint PDF.