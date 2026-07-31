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

$$P(A) = \sum_{i=1}^n P(A \cap B_i) = \sum_{i=1}^n P(A|B_i)P(B_i)$$

- Applying the definition of conditional probability to the term $P(A \cap B)$, we get:

$$P(A \cap B) = P(B|A)P(A)$$

- Substituting this into the formula for $P(A|B)$, we get:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Which is Bayes' theorem.

## Example

- Suppose we want to find the probability that a person has a certain disease, given that they have tested positive for it. We know that the disease affects 1% of the population, and that the test has a 95% accuracy rate, meaning that it correctly identifies 95% of the people who have the disease, and 95% of the people who do not have the disease.
- Let $D$ be the event that the person has the disease, and $T$ be the event that the person tests positive. We want to find $P(D|T)$, the posterior probability.
- Using Bayes' theorem, we have:

$$P(D|T) = \frac{P(T|D)P(D)}{P(T)}$$

- We know that $P(T|D) = 0.95$, the accuracy rate of the test for people who have the disease, and $P(D) = 0.01$, the prevalence rate of the disease in the population.
- To find $P(T)$, the evidence, we can use the law of total probability, and partition the sample space into two mutually exclusive events: $D$ and $D^c$, the complement of $D$, meaning that the person does not have the disease. We have:

$$P(T) = P(T \cap D) + P(T \cap D^c) = P(T|D)P(D) + P(T|D^c)P(D^c)$$

- We know that $P(T|D^c) = 0.05$, the false positive rate of the test for people who do not have the disease, and $P(D^c) = 0.99$, the complement of the prevalence rate of the disease in the population.
- Substituting these values into the formula for $P