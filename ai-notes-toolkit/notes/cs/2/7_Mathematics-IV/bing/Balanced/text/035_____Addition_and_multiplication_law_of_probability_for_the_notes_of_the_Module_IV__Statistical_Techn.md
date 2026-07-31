### Addition and multiplication law of probability

- The addition law of probability is used to find the probability of the union of two events, denoted by P(A OR B).
- The multiplication law of probability is used to find the probability of the intersection of two events, denoted by P(A AND B).
- The addition and multiplication laws of probability depend on whether the events are mutually exclusive or independent.

#### Mutually exclusive events
- Two events are mutually exclusive if they cannot occur at the same time, i.e., P(A AND B) = 0.
- For mutually exclusive events, the addition law of probability is given by:

P(A OR B) = P(A) + P(B)

- For mutually exclusive events, the multiplication law of probability is not applicable, since P(A AND B) = 0.

#### Independent events
- Two events are independent if the occurrence of one event does not affect the probability of the other event, i.e., P(A | B) = P(A) and P(B | A) = P(B).
- For independent events, the addition law of probability is given by:

P(A OR B) = P(A) + P(B) - P(A AND B)

- For independent events, the multiplication law of probability is given by:

P(A AND B) = P(A) * P(B)

#### Dependent events
- Two events are dependent if the occurrence of one event affects the probability of the other event, i.e., P(A | B) ≠ P(A) or P(B | A) ≠ P(B).
- For dependent events, the addition law of probability is given by:

P(A OR B) = P(A) + P(B) - P(A AND B)

- For dependent events, the multiplication law of probability is given by:

P(A AND B) = P(A) * P(B | A) = P(B) * P(A | B)

#### Examples
- Example 1: A coin is tossed twice. What is the probability of getting at least one head?
  - Solution: Let A be the event of getting a head on the first toss, and B be the event of getting a head on the second toss. Then A and B are independent events, since the outcome of one toss does not affect the other. We can use the addition law of probability to find the probability of getting at least one head, which is the same as the probability of A OR B. We have:

  P(A) = P(B) = 1/2, since the coin is fair.

  P(A AND B) = P(A) * P(B) = 1/2 * 1/2 = 1/4, by the multiplication law of probability for independent events.

  P(A OR B) = P(A) + P(B) - P(A AND B) = 1/2 + 1/2 - 1/4 = 3/4, by the addition law of probability for independent events.

  Therefore, the probability of getting at least one head is 3/4.

- Example 2: A card is drawn from a standard deck of 52 cards. What is the probability of getting a king or a spade?
  - Solution: Let A be the event of getting a king, and B be the event of getting a spade. Then A and B are not mutually exclusive, since there is one card that is both a king and a spade (the king of spades). We can use the addition law of probability to find the probability of getting a king or a spade, which is the same as the probability of A OR B. We have:

  P(A) = 4/52, since there are four kings in the deck.

  P(B) = 13/52, since there are 13 spades in the deck.

  P(A AND B) = 1/52, since there is only one card that is both a king and a spade.

  P(A OR B) = P(A) + P(B) - P(A AND B) = 4/52 + 13/52 - 1/52 = 16/52, by the addition law of probability for dependent events.

  Therefore, the probability of getting a king or a spade is 16/52.