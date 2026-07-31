Hello, I am Sydney, your AI assistant. I can help you with your study material on conditional probability for the Unit 1 - Descriptive Statistics in the subject of Mathematical Foundation AI, ML and Data Science. Here are some points to note:

- Conditional probability is the probability of one event occurring with some relationship to one or more other events. For example, the probability of a boy playing tennis in the evening is 95% (0.95) whereas the probability that he plays given that it is a rainy day is less which is 10% (0.1). 
- The conditional probability of an event A given that another event B has occurred is denoted by P(A|B) and is calculated by the formula: P(A|B) = P(A and B) / P(B), where P(A and B) is the joint probability of both events happening and P(B) is the marginal probability of event B happening. 
- The conditional probability formula can be derived from the definition of the joint probability: P(A and B) = P(A) * P(B|A) = P(B) * P(A|B), where P(B|A) is the conditional probability of B given A and P(A|B) is the conditional probability of A given B. Dividing both sides by P(B) gives the formula for P(A|B). 
- Conditional probability can be used to find the probability of an event based on some prior information or condition. For example, if a card is drawn from a standard deck of 52 cards, the probability that it is a king is 4/52 or 1/13. However, if it is known that the card is a face card, then the conditional probability that it is a king is 4/12 or 1/3, since there are only 12 face cards in the deck. 
- Conditional probability can also be used to test the independence of two events. Two events are independent if the occurrence of one event does not affect the probability of the other event. This means that P(A|B) = P(A) and P(B|A) = P(B) for independent events A and B. If these equalities do not hold, then the events are dependent. 
- Conditional probability can be represented by a Venn diagram or a two-way table. A Venn diagram shows the overlapping regions of two or more sets, where each set represents an event. The conditional probability of one event given another can be found by comparing the area of the intersection of the sets to the area of the set representing the given event. A two-way table shows the frequency or probability of different combinations of two events in a tabular form. The conditional probability of one event given another can be found by dividing the corresponding cell value by the row or column total. 

Here is an example of a Venn diagram and a two-way table for the events A and B:

![Venn diagram](https://www.cuemath.com/data/conditional-probability/venn-diagram.png)

|       | A    | not A | Total |
| ----- | ---- | ----- | ----- |
| B     | 0.2  | 0.1   | 0.3   |
| not B | 0.4  | 0.3   | 0.7   |
| Total | 0.6  | 0.4   | 1     |

Using the Venn diagram or the two-way table, we can find the following conditional probabilities:

- P(A|B) = 0.2 / 0.3 = 2/3
- P(B|A) = 0.2 / 0.6 = 1/3
- P(A|not B) = 0.4 / 0.7 = 4/7
- P(not B|A) = 0.4 / 0.6 = 2/3
- P(not A|B) = 0.1 / 0.3 = 1/3
- P(B|not A) = 0.1 / 0.4 = 1/4
- P(not A|not B) = 0.3 / 0.7 = 3/7
- P(not B|not A) = 0.3