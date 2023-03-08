 Here is the content in markdown format for the topic ### Entropy and information theory for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques:

### Entropy and information theory

- Entropy is a measure of uncertainty associated with a random variable. It specifies the minimum number of bits needed to encode the variable's possible outcomes.
- For a discrete random variable X that can take on possible values {x1, x2, ..., xn} with probabilities {p1, p2, ..., pn}, the entropy H(X) is defined as:
H(X) = -Σpi log pi
- The entropy is maximum when all probabilities are equal, i.e. no outcome is certain. The entropy is minimum (zero) when one of the outcomes has probability 1.
- Information gain is used to select attributes (features) for splitting the data. It is based on the concept of entropy.
- Information gain of an attribute A is the expected reduction in entropy caused by partitioning the samples according to A.
- Information gain (IG) of an attribute A = Entropy (S) - [Weighted Average Entropy of subsets of S based on A]
- where S is the set of samples, and the weighted average entropy is calculated using the probability of subsets as weights.
- The attribute with the highest information gain is chosen as the splitting attribute at each node in decision tree learning. This is because it results in the purest subsets (least entropy) and hence the most homogeneous partitions.

[Include diagrams/codes/examples/applications if needed]