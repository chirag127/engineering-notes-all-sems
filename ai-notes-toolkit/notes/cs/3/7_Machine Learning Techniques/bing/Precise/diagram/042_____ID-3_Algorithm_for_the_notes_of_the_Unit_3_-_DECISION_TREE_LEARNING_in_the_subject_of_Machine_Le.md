### ID-3 Algorithm

ID3 algorithm, which stands for Iterative Dichotomiser 3, is a classification algorithm that follows a greedy approach to building a decision tree by selecting the best attribute that yields maximum Information Gain (IG) or minimum Entropy (H).

#### Characteristics of ID3 Algorithm:
- ID3 uses a greedy approach, which is why it does not guarantee an optimal solution; it can get stuck in local optimums.
- ID3 can overfit the training data. To avoid overfitting, smaller decision trees should be preferred over larger ones.

#### How ID3 Algorithm Works:
- The ID3 algorithm begins with the original set as the root node.
- On each iteration of the algorithm, it iterates through every unused attribute of the set and calculates the entropy or the information gain of that attribute.
- It then selects the attribute which has the smallest entropy (or largest information gain) value.

#### Usage of ID3 Algorithm:
- The ID3 algorithm is used by training on a dataset to produce a decision tree, which is stored in memory.
- At runtime, this decision tree is used to classify new test cases (feature vectors) by traversing the decision tree using the features of the datum to arrive at a leaf node.

ID3 is the precursor to the C4.5 algorithm and is typically used in the machine learning and natural language processing domains.