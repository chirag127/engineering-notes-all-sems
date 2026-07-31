# Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions in light of new or relevant evidence, also known as posterior probability or inverse probability.
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied using modern Markov Chain Monte Carlo methods.

## Formula

- The formula for Bayes' theorem is:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Where:

  - $P(A|B)$ is the conditional probability of event A given event B, also known as the posterior probability.
  - $P(B|A)$ is the conditional probability of event B given event A, also known as the likelihood.
  - $P(A)$ is the prior probability of event A, also known as the marginal probability.
  - $P(B)$ is the prior probability of event B, also known as the evidence or normalizing constant.

## Derivation

- Bayes' theorem can be derived from the definition of conditional probability and the law of total probability.
- The definition of conditional probability is:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

- The law of total probability states that for any partition of the sample space $\{B_1, B_2, ..., B_n\}$, such that $P(B_i) > 0$ for all $i$, and $\bigcup_{i=1}^n B_i = S$, where $S$ is the sample space, the following holds:

$$P(A) = \sum_{i=1}^n P(A|B_i)P(B_i)$$

- Applying the law of total probability to the denominator of the conditional probability definition, we get:

$$P(A|B) = \frac{P(A \cap B)}{\sum_{i=1}^n P(A \cap B_i)}$$

- If we assume that event B is one of the partition elements, say $B_k$, then we can simplify the denominator as:

$$P(A|B) = \frac{P(A \cap B)}{P(A \cap B_k)}$$

- Applying the definition of conditional probability to the numerator and the denominator, we get:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B|A)P(A)}$$

- Cancelling out the common factor, we get:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Which is the formula for Bayes' theorem.

## Examples

- Example 1: Suppose there is a test for a rare disease, which has a 99% accuracy rate, meaning that 99% of the time it gives a correct result, either positive or negative. The disease affects 1 in 10,000 people in the population. What is the probability that a person who tests positive actually has the disease?

  - Solution: Let $D$ be the event that a person has the disease, and $T$ be the event that a person tests positive. We want to find $P(D|T)$, the posterior probability. We are given the following information:

    - $P(T|D) = 0.99$, the likelihood, which is the probability of testing positive given that the person has the disease.
    - $P(D) = 0.0001$, the prior probability, which is the probability of having the disease in the population.
    - $P(T) = P(T|D)P(D) + P(T|\neg D)P(\neg D)$, the evidence, which is the probability of testing positive in the population, calculated using the law of total probability. Here, $\neg D$ is the complement of $D$, meaning that the person does not have the disease. We can assume that $P(T|\neg D) = 0.01$, which is the probability of testing positive given that the person does not have