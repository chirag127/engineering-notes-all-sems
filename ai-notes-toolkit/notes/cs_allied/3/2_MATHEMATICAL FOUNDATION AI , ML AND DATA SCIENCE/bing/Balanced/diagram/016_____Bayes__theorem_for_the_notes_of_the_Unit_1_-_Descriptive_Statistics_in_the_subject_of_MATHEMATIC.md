### Bayes' Theorem

- Bayes' theorem is a mathematical formula for determining conditional probability, which is the likelihood of an event occurring, based on a previous outcome having occurred in similar circumstances.
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who used conditional probability to provide an algorithm for calculating limits on an unknown parameter.
- Bayes' theorem can be used to update or revise predictions or beliefs in light of new or relevant evidence, also known as posterior probability or inverse probability .
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line, and can be applied to various fields, such as statistics, machine learning, artificial intelligence, data science, etc .
- Bayes' theorem can be stated as follows:

  - Let A and B be two events. The conditional probability of A given B is denoted by P(A|B), and the conditional probability of B given A is denoted by P(B|A).
  - The prior probability of A is denoted by P(A), and the prior probability of B is denoted by P(B).
  - The marginal probability of B is denoted by P(B), and is the probability of B occurring regardless of A.
  - The posterior probability of A given B is denoted by P(A|B), and is the probability of A occurring after observing B.
  - Bayes' theorem states that:

    - P(A|B) = P(B|A) * P(A) / P(B)

  - Alternatively, Bayes' theorem can be written as:

    - P(A|B) = P(B|A) * P(A) / (P(B|A) * P(A) + P(B|A<sup>c</sup>) * P(A<sup>c</sup>))

  - Where A<sup>c</sup> and B<sup>c</sup> are the complements of A and B, respectively.

- Bayes' theorem can be derived from the definition of conditional probability and the law of total probability, as follows:

  - By definition, P(A|B) = P(A and B) / P(B), and P(B|A) = P(A and B) / P(A).
  - By rearranging, P(A and B) = P(A|B) * P(B) = P(B|A) * P(A).
  - By dividing both sides by P(B), P(A|B) = P(B|A) * P(A) / P(B).
  - By the law of total probability, P(B) = P(B|A) * P(A) + P(B|A<sup>c</sup>) * P(A<sup>c</sup>).
  - By substituting, P(A|B) = P(B|A) * P(A) / (P(B|A) * P(A) + P(B|A<sup>c</sup>) * P(A<sup>c</sup>)).

- Bayes' theorem can be illustrated by an example:

  - Suppose there is a test for a rare disease, which has a 99% accuracy rate, meaning that it correctly identifies 99% of the people who have the disease and 99% of the people who do not have the disease. The disease affects 1% of the population. What is the probability that a person who tests positive for the disease actually has the disease?
  - Let D be the event that a person has the disease, and T be the event that a person tests positive for the disease. We want to find P(D|T), the posterior probability of having the disease given a positive test result.
  - By Bayes' theorem, P(D|T) = P(T|D) * P(D) / P(T).
  - P(T|D) is the probability of testing positive given that the person has the disease, which is 0.99, the accuracy rate of the test.
  - P(D) is the prior probability of having the disease, which is 0.01, the prevalence rate of the disease in the population.
  - P(T) is the marginal probability of testing positive, which can be calculated by the law of total probability as P(T) = P(T|D) * P(D) + P(T|D<sup>c</sup>) * P(D<sup>c</sup>