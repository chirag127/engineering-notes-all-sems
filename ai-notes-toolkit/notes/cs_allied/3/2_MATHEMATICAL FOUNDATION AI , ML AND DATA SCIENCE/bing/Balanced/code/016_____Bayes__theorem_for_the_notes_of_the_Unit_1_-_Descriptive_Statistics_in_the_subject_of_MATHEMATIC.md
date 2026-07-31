### Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions in light of new or relevant evidence, also known as posterior probability or inverse probability.
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied using modern Markov Chain Monte Carlo methods.

#### Formula

- The formula for Bayes' theorem is:

    `P(A|B) = (P(B|A) * P(A)) / P(B)`

- Where:

    - `P(A|B)` is the conditional probability of event A given event B, also known as the posterior probability.
    - `P(B|A)` is the conditional probability of event B given event A, also known as the likelihood.
    - `P(A)` is the prior probability of event A, also known as the marginal probability.
    - `P(B)` is the prior probability of event B, also known as the evidence or normalizing constant.

#### Example

- Suppose we want to find the probability of a person having a disease, given that they have a positive test result. We can use Bayes' theorem to calculate this probability, using the following information:

    - The prior probability of having the disease is 0.01, or 1%.
    - The likelihood of testing positive given that the person has the disease is 0.9, or 90%.
    - The prior probability of testing positive is 0.05, or 5%.

- Using the formula, we get:

    `P(Disease|Positive) = (P(Positive|Disease) * P(Disease)) / P(Positive)`

    `P(Disease|Positive) = (0.9 * 0.01) / 0.05`

    `P(Disease|Positive) = 0.18`

- Therefore, the probability of having the disease given a positive test result is 0.18, or 18%.