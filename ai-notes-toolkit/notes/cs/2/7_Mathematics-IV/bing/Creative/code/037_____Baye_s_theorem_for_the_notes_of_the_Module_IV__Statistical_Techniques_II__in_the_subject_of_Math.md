### Bayes' Theorem

Bayes' theorem is a mathematical formula that allows us to calculate the conditional probability of an event, based on prior knowledge of related conditions. Conditional probability is the likelihood of an event occurring, given that another event has occurred. Bayes' theorem is named after Thomas Bayes, an 18th-century British mathematician and philosopher, who published his work posthumously in 1763.

#### Formula

The formula for Bayes' theorem is:

P(A|B) = (P(B|A) * P(A)) / P(B)

where:

- P(A|B) is the conditional probability of event A occurring, given that event B has occurred.
- P(B|A) is the conditional probability of event B occurring, given that event A has occurred.
- P(A) is the prior probability of event A occurring, without any knowledge of event B.
- P(B) is the prior probability of event B occurring, without any knowledge of event A.

#### Derivation

Bayes' theorem can be derived from the definition of conditional probability, which states that:

P(A|B) = P(A and B) / P(B)

and

P(B|A) = P(A and B) / P(A)

Multiplying both sides of the second equation by P(A), we get:

P(A and B) = P(B|A) * P(A)

Substituting this into the first equation, we get:

P(A|B) = (P(B|A) * P(A)) / P(B)

which is the formula for Bayes' theorem.

#### Examples

- Suppose we have a test for a disease that has a 99% accuracy rate, meaning that it correctly identifies 99% of the people who have the disease and 99% of the people who do not have the disease. If the prevalence of the disease in the population is 1%, what is the probability that a person who tests positive actually has the disease?

Using Bayes' theorem, we can assign the following probabilities:

- P(A) = 0.01, the prior probability of having the disease.
- P(B) = 0.01 * 0.99 + 0.99 * 0.01, the prior probability of testing positive, which is the sum of the probabilities of having the disease and testing positive, and not having the disease and testing positive.
- P(B|A) = 0.99, the conditional probability of testing positive, given that the person has the disease.
- P(A|B) = ?, the conditional probability of having the disease, given that the person tests positive.

Plugging these values into the formula, we get:

P(A|B) = (0.99 * 0.01) / (0.01 * 0.99 + 0.99 * 0.01)
P(A|B) = 0.5

Therefore, the probability that a person who tests positive actually has the disease is 50%.

- Suppose we have a bag of 10 marbles, 3 of which are red and 7 of which are blue. We draw one marble at random and observe its color, then put it back in the bag and draw another marble at random. What is the probability that the second marble is red, given that the first marble was red?

Using Bayes' theorem, we can assign the following probabilities:

- P(A) = 0.3, the prior probability of drawing a red marble.
- P(B) = 0.3, the prior probability of drawing a red marble again, since we are replacing the marble after each draw.
- P(B|A) = 0.3, the conditional probability of drawing a red marble again, given that the first marble was red.
- P(A|B) = ?, the conditional probability of drawing a red marble, given that the second marble was red.

Plugging these values into the formula, we get:

P(A|B) = (0.3 * 0.3) / 0.3
P(A|B) = 0.3

Therefore, the probability that the second marble is red, given that the first marble was red, is 30%.