### Bayes' Theorem

- Bayes' theorem is a mathematical formula that calculates the conditional probability of an event, based on prior knowledge of related conditions .
- Conditional probability is the likelihood of an event occurring, given that another event has occurred .
- Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician, statistician and philosopher, who published his work posthumously in 1763 .
- Bayes' theorem can be used to revise predictions or beliefs in light of new evidence or data.
- Bayes' theorem can be generalized to include improper prior distributions, such as the uniform distribution on the real line.
- Bayes' theorem can be applied to various fields, such as machine learning, artificial intelligence, data science, statistics, medicine, etc.

#### Formula and Derivation

- The formula of Bayes' theorem is:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Where:

  - $P(A|B)$ is the conditional probability of event A occurring, given that event B has occurred.
  - $P(B|A)$ is the conditional probability of event B occurring, given that event A has occurred.
  - $P(A)$ is the prior probability of event A occurring, without any knowledge of event B.
  - $P(B)$ is the prior probability of event B occurring, without any knowledge of event A.

- The derivation of Bayes' theorem is based on the product rule of probability, which states that:

$$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$$

- Where:

  - $P(A \cap B)$ is the joint probability of event A and event B occurring together.
  - $P(A|B)P(B)$ is the product of the conditional probability of event A occurring, given that event B has occurred, and the prior probability of event B occurring.
  - $P(B|A)P(A)$ is the product of the conditional probability of event B occurring, given that event A has occurred, and the prior probability of event A occurring.

- By dividing both sides of the equation by $P(B)$, we get:

$$\frac{P(A \cap B)}{P(B)} = \frac{P(A|B)P(B)}{P(B)} = \frac{P(B|A)P(A)}{P(B)}$$

- Simplifying, we get:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Which is the formula of Bayes' theorem.

#### Example

- Suppose we have a test for a disease that has a 99% accuracy rate, meaning that it correctly identifies 99% of the people who have the disease and 99% of the people who do not have the disease. Suppose also that the disease has a prevalence rate of 0.1%, meaning that 0.1% of the population has the disease. What is the probability that a person who tests positive for the disease actually has the disease?

- Using Bayes' theorem, we can calculate the conditional probability of having the disease, given that the test is positive, as follows:

  - Let A be the event of having the disease, and B be the event of testing positive for the disease.
  - We are given that:

    - $P(B|A) = 0.99$, which is the probability of testing positive, given that the person has the disease (true positive rate).
    - $P(A) = 0.001$, which is the prior probability of having the disease (prevalence rate).
    - $P(B|\neg A) = 0.01$, which is the probability of testing positive, given that the person does not have the disease (false positive rate).
    - $P(\neg A) = 0.999$, which is the prior probability of not having the disease (1 - prevalence rate).

  - We can use the law of total probability to calculate $P(B)$, which is the prior probability of testing positive, as follows:

    - $P(B) = P(B|A)P(A) + P(B|\neg A)P(\neg A)$
    - $P(B) = 0.99 \times 0.001