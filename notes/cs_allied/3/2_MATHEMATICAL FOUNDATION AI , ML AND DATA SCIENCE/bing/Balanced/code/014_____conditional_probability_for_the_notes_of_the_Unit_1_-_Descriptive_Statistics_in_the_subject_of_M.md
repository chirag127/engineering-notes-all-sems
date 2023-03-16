Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on conditional probability for the Unit 1 - Descriptive Statistics in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE.

### Conditional Probability

- Conditional probability is the probability of an event occurring given that another event has already occurred.
- The notation for conditional probability is P(A|B), which means the probability of event A happening given that event B has already happened.
- The formula for conditional probability is P(A|B) = P(A and B) / P(B), where P(A and B) is the joint probability of both events occurring, and P(B) is the marginal probability of event B occurring.
- Conditional probability can be used to update our beliefs about an event based on new information or evidence.
- Conditional probability can also be used to find the probability of an event using a contingency table, a tree diagram, or Bayes' theorem.

#### Contingency Table

- A contingency table is a table that shows the frequencies or probabilities of different outcomes of two or more categorical variables.
- A contingency table can be used to find the conditional probability of an event by dividing the frequency or probability of the event and its condition by the frequency or probability of the condition.
- For example, suppose we have a contingency table that shows the gender and eye color of 100 students:

|       | Blue | Brown | Green | Total |
|-------|------|-------|-------|-------|
| Male  | 10   | 30    | 5     | 45    |
| Female| 15   | 25    | 15    | 55    |
| Total | 25   | 55    | 20    | 100   |

- To find the conditional probability of a student having blue eyes given that they are male, we can use the formula P(Blue|Male) = P(Blue and Male) / P(Male) = 10 / 45 = 0.222
- To find the conditional probability of a student being female given that they have green eyes, we can use the formula P(Female|Green) = P(Female and Green) / P(Green) = 15 / 20 = 0.75

#### Tree Diagram

- A tree diagram is a graphical representation of the possible outcomes of a sequence of events or experiments.
- A tree diagram can be used to find the conditional probability of an event by multiplying the probabilities along the branches that lead to the event.
- For example, suppose we have a tree diagram that shows the outcomes of flipping a fair coin twice:

![tree diagram](https://www.mathsisfun.com/data/images/probability-tree-coin2.svg)

- To find the conditional probability of getting two heads given that the first flip is a head, we can use the formula P(HH|H) = P(HH and H) / P(H) = P(HH) / P(H) = 0.25 / 0.5 = 0.5
- To find the conditional probability of getting a tail on the second flip given that the first flip is a head, we can use the formula P(T|H) = P(T and H) / P(H) = P(HT) / P(H) = 0.25 / 0.5 = 0.5

#### Bayes' Theorem

- Bayes' theorem is a formula that relates the conditional probability of an event to the prior probability of the event and the likelihood of the evidence.
- Bayes' theorem can be used to find the conditional probability of an event using the formula P(A|B) = P(B|A) * P(A) / P(B), where P(B|A) is the likelihood of the evidence given the event, P(A) is the prior probability of the event, and P(B) is the marginal probability of the evidence.
- Bayes' theorem can also be used to find the posterior probability of an event, which is the updated probability of the event after observing the evidence, using the formula P(A|B) = P(B|A) * P(A) / [P(B|A) * P(A) + P(B|not A) * P(not A)], where P(B|not A) is the likelihood of the evidence given the complement of the event, and P(not A) is the prior probability of the complement of the event.
- For example, suppose we have a test for a rare disease that has a 99% accuracy rate, meaning that it correctly identifies 99% of the people who have the disease and 99% of the people who do not have the disease.