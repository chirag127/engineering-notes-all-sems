# Addition and multiplication law of probability

- Probability is a measure of how likely an event is to occur in a random experiment.
- An event is a subset of the sample space, which is the set of all possible outcomes of the experiment.
- The probability of an event A is denoted by P(A) and satisfies 0 ≤ P(A) ≤ 1.
- The probability of the sample space is 1, and the probability of the empty set is 0.
- The addition and multiplication rules of probability are two ways of finding the probability of compound events, which are events that involve two or more simple events.

## The addition rule of probability

- The addition rule of probability is used to find the probability of the union of two events, which is the event that either one or both of them occur.
- The addition rule states that P(A ∪ B) = P(A) + P(B) - P(A ∩ B), where A ∩ B is the intersection of the two events, which is the event that both of them occur.
- The subtraction term P(A ∩ B) is needed to avoid double-counting the outcomes that belong to both events.
- If the two events are mutually exclusive, meaning that they cannot occur at the same time, then P(A ∩ B) = 0, and the addition rule simplifies to P(A ∪ B) = P(A) + P(B).
- For example, if A is the event of rolling an even number on a fair die, and B is the event of rolling a multiple of 3, then P(A) = 3/6, P(B) = 2/6, and P(A ∩ B) = 1/6. Therefore, P(A ∪ B) = 3/6 + 2/6 - 1/6 = 4/6.

## The multiplication rule of probability

- The multiplication rule of probability is used to find the probability of the intersection of two events, which is the event that both of them occur.
- The multiplication rule states that P(A ∩ B) = P(A)P(B | A), where P(B | A) is the conditional probability of B given A, which is the probability of B occurring after A has occurred.
- The multiplication factor P(B | A) is needed to account for the dependence of B on A, meaning that the occurrence of A may affect the likelihood of B.
- If the two events are independent, meaning that the occurrence of A does not affect the likelihood of B, then P(B | A) = P(B), and the multiplication rule simplifies to P(A ∩ B) = P(A)P(B).
- For example, if A is the event of getting heads on the first toss of a fair coin, and B is the event of getting heads on the second toss, then P(A) = 1/2, P(B) = 1/2, and P(B | A) = 1/2. Therefore, P(A ∩ B) = 1/2 × 1/2 = 1/4.