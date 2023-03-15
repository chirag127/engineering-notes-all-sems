### Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions in light of new or relevant evidence, also known as posterior probability or inverse probability.
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied using modern Markov Chain Monte Carlo methods.

#### Formula and Derivation

- The formula of Bayes' theorem is:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

where:

- $P(A|B)$ is the conditional probability of event $A$ given that event $B$ has occurred, also known as the posterior probability.
- $P(B|A)$ is the conditional probability of event $B$ given that event $A$ has occurred, also known as the likelihood.
- $P(A)$ is the prior probability of event $A$ occurring, based on existing knowledge or belief.
- $P(B)$ is the prior probability of event $B$ occurring, or the marginal probability of event $B$.

- The derivation of Bayes' theorem is based on the following two rules of probability:

  - The product rule: $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$
  - The sum rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

- Using the product rule, we can write:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

- Similarly, we can write:

$$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

- Solving for $P(A \cap B)$ in both equations, we get:

$$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$

- Dividing both sides by $P(B)$, we get:

$$\frac{P(A \cap B)}{P(B)} = \frac{P(B|A)P(A)}{P(B)}$$

- Simplifying, we get:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- This is the formula of Bayes' theorem.

#### Example

- Suppose we want to find the probability of a person having a disease, given that they have a positive test result, using Bayes' theorem. We have the following information:

  - The prior probability of having the disease is 0.01, or 1%.
  - The probability of a positive test result given that the person has the disease is 0.99, or 99%.
  - The probability of a positive test result given that the person does not have the disease is 0.05, or 5%.

- Using Bayes' theorem, we can write:

$$P(Disease|Positive) = \frac{P(Positive|Disease)P(Disease)}{P(Positive)}$$

- To find $P(Positive)$, we can use the sum rule and the product rule:

$$P(Positive) = P(Positive|Disease)P(Disease) + P(Positive|No Disease)P(No Disease)$$

- Substituting the given values, we get:

$$P(Positive) = 0.99 \times 0.01 + 0.05 \times 0.99 = 0.0594$$

- Therefore, the posterior probability of having the disease given a positive test result is:

$$P(Disease|Positive) = \frac{0.99 \times 0.01}{0.0594} = 0.1664$$

- This means that there is a 16.64% chance of having the disease given a positive test result.