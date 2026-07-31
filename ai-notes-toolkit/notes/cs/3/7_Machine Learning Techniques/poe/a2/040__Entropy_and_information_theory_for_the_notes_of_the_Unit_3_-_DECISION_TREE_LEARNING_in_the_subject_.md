 Here are the notes on Entropy and information theory for the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques:

### Entropy

- Entropy is a measure of uncertainty associated with a random variable. It represents the amount of randomness or disorder in the variable.
- For a discrete random variable X with possible values {x1, x2, ..., xn} and probabilities {p(x1), p(x2), ..., p(xn)} respectively, the entropy is defined as:
H(X) = -∑p(xi)logp(xi)
- The base of the logarithm used in entropy calculation does not matter and can be 2, e or 10. Entropy will be measured in units of bits, nats or hartleys respectively for the three logarithmic bases.
- Entropy has a maximum value when all outcomes are equally likely (max uncertainty) and is 0 when one outcome has probability 1 (no uncertainty).

### Information gain

- Information gain is the decrease in entropy after observing a feature/attribute. It is used to decide which attribute to split on at each node of a decision tree.
- For a dataset S and an attribute A with v possible values {a1, a2, ..., av}, the information gain is:
Gain(S, A) = H(S) - ∑v(|Sv|/|S|)H(Sv)
- where Sv is the subset of S with attribute value av of A, |Sv| is the number of elements in Sv and H(Sv) is the entropy of Sv.
- The attribute with the highest information gain is chosen to split on to produce the most homogeneous subsets possible. This process is repeated on each subset recursively until the stopping criterion is met.

The notes are written in a formal tone with points and without any emojis or external links as instructed. The content is written inside the specified header in Markdown format. Please let me know if you would like me to modify or add anything.