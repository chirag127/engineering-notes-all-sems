Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on conditional probability for the Unit 1 - Descriptive Statistics in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE.

# Conditional Probability

- Conditional probability is the probability of an event occurring given that another event has already occurred.
- Conditional probability is denoted by P(A|B), which means the probability of event A happening given that event B has already happened.
- Conditional probability can be calculated using the formula:

P(A|B) = P(A and B) / P(B)

- where P(A and B) is the joint probability of both events happening, and P(B) is the marginal probability of event B happening.
- Conditional probability can also be expressed using a contingency table, which shows the frequencies of different outcomes for two events.

|       | B    | not B | Total |
| ----- | ---- | ----- | ----- |
| A     | a    | b     | a + b |
| not A | c    | d     | c + d |
| Total | a + c| b + d | n     |

- In this table, P(A|B) = a / (a + c), P(B|A) = a / (a + b), P(A and B) = a / n, and P(B) = (a + c) / n.
- Conditional probability can be used to find the probability of dependent events, which are events that are influenced by each other.
- For example, if we want to find the probability of drawing two red cards from a deck of cards without replacement, we can use conditional probability:

P(red and red) = P(red) * P(red|red) = (26/52) * (25/51) = 0.245

- Conditional probability can also be used to find the probability of independent events, which are events that are not influenced by each other.
- For example, if we want to find the probability of flipping a coin and rolling a six on a die, we can use conditional probability:

P(heads and six) = P(heads) * P(six|heads) = (1/2) * (1/6) = 1/12

- Conditional probability can also be used to update our beliefs about an event based on new information, using Bayes' theorem.
- Bayes' theorem states that:

P(A|B) = P(B|A) * P(A) / P(B)

- where P(A) and P(B) are the prior probabilities of events A and B, and P(A|B) and P(B|A) are the posterior probabilities of events A and B after observing each other.
- For example, if we want to find the probability of having a disease given a positive test result, we can use Bayes' theorem:

P(disease|positive) = P(positive|disease) * P(disease) / P(positive)

- where P(positive|disease) is the sensitivity of the test, P(disease) is the prevalence of the disease, and P(positive) is the probability of a positive test result.