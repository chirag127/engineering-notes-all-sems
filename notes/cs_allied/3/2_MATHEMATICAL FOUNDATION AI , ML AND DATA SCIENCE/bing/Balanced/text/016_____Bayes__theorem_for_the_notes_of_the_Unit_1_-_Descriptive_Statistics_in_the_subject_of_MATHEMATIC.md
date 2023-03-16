### Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions or beliefs in light of new or relevant evidence, also known as posterior probability or inverse probability .
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied to various fields, such as science, engineering, medicine, economics, etc.
- Bayes' theorem can be expressed in various forms, but the most common one is:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

where:

- $P(A|B)$ is the conditional probability of event A given that event B has occurred, also known as the posterior probability.
- $P(B|A)$ is the conditional probability of event B given that event A has occurred, also known as the likelihood.
- $P(A)$ is the prior probability of event A, which is the probability of event A before observing event B.
- $P(B)$ is the marginal probability of event B, which is the probability of event B regardless of event A.

- Bayes' theorem can be derived from the definition of conditional probability and the law of total probability, as follows:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

$$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

$$P(A \cap B) = P(B|A)P(A) = P(A|B)P(B)$$

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Bayes' theorem can be extended to more than two events, such as:

$$P(A|B,C) = \frac{P(B,C|A)P(A)}{P(B,C)}$$

- Bayes' theorem can also be applied to continuous random variables, such as:

$$f(x|y) = \frac{f(y|x)f(x)}{f(y)}$$

where:

- $f(x|y)$ is the conditional probability density function of random variable X given that random variable Y has a value of y, also known as the posterior density.
- $f(y|x)$ is the conditional probability density function of random variable Y given that random variable X has a value of x, also known as the likelihood function.
- $f(x)$ is the prior probability density function of random variable X, which is the probability density of X before observing Y.
- $f(y)$ is the marginal probability density function of random variable Y, which is the probability density of Y regardless of X.

- Bayes' theorem can be illustrated by various examples, such as:

  - Example 1: Suppose there is a test for a disease that has a 99% accuracy rate, meaning that 99% of the time it gives a correct result (positive or negative) for a person who has or does not have the disease. Suppose also that 1% of the population has the disease. What is the probability that a person who tests positive actually has the disease?

    - Solution: Let A be the event that a person has the disease, and B be the event that a person tests positive. We want to find $P(A|B)$, the probability that a person has the disease given that they test positive. Using Bayes' theorem, we have:

    $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

    - We know that $P(B|A) = 0.99$, the accuracy rate of the test for a person who has the disease. We also know that $P(A) = 0.01$, the prevalence rate of the disease in the population. To find $P(B)$, the probability that a person tests positive, we can use the law of total probability, which states that:

    $$P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$$