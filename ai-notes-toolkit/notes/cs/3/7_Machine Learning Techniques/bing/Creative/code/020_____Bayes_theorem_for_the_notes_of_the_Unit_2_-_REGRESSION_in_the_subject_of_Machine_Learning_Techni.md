# Bayes Theorem

Bayes theorem is a mathematical formula that allows us to calculate the conditional probability of an event, given some prior knowledge or evidence. It is named after Thomas Bayes, an 18th-century British mathematician and philosopher.

## Formula

The formula for Bayes theorem is:

P(A|B) = P(A) P(B|A) / P(B)

where:

- P(A|B) is the posterior probability of A given B, or the probability of A after observing B
- P(A) is the prior probability of A, or the probability of A before observing B
- P(B|A) is the likelihood of B given A, or the probability of observing B if A is true
- P(B) is the marginal probability of B, or the probability of observing B regardless of A

## Derivation

Bayes theorem can be derived from the definition of conditional probability and the law of total probability. The definition of conditional probability is:

P(A|B) = P(A and B) / P(B)

The law of total probability states that the probability of an event is the sum of the probabilities of the event occurring under each mutually exclusive condition. For example, if A and A' are complementary events (meaning that one of them must occur), then:

P(B) = P(B|A) P(A) + P(B|A') P(A')

Using these two rules, we can derive Bayes theorem as follows:

P(A|B) = P(A and B) / P(B)

P(A|B) = P(B|A) P(A) / P(B)

P(A|B) = P(B|A) P(A) / [P(B|A) P(A) + P(B|A') P(A')]

## Example

Suppose we have a test for a disease that has a 99% accuracy rate, meaning that it correctly identifies 99% of the people who have the disease and 99% of the people who do not have the disease. Suppose also that the disease affects 1% of the population. What is the probability that a person who tests positive for the disease actually has the disease?

Using Bayes theorem, we can calculate the posterior probability of having the disease given a positive test result as follows:

P(D|+) = P(D) P(+|D) / P(+)

where:

- P(D|+) is the probability of having the disease given a positive test result
- P(D) is the prior probability of having the disease, which is 0.01
- P(+|D) is the likelihood of a positive test result given the disease, which is 0.99
- P(+) is the marginal probability of a positive test result, which we can calculate using the law of total probability:

P(+) = P(+|D) P(D) + P(+|D') P(D')

where:

- P(+|D') is the likelihood of a positive test result given no disease, which is 0.01
- P(D') is the prior probability of not having the disease, which is 0.99

Plugging in the values, we get:

P(+) = 0.99 x 0.01 + 0.01 x 0.99

P(+) = 0.0198

P(D|+) = 0.01 x 0.99 / 0.0198

P(D|+) = 0.5

Therefore, the probability that a person who tests positive for the disease actually has the disease is 50%. This may seem surprising, given the high accuracy rate of the test, but it is due to the low prevalence of the disease in the population. If the disease were more common, the posterior probability would be higher. For example, if the disease affected 10% of the population, the posterior probability would be:

P(D|+) = 0.1 x 0.99 / [0.1 x 0.99 + 0.9 x 0.01]

P(D|+) = 0.916

Therefore, the probability that a person who tests positive for the disease actually has the disease would be 91.6%.