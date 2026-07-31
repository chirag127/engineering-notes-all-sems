### ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3, an algorithm invented by Ross Quinlan to generate a decision tree from a dataset .
- ID-3 is a classification algorithm that follows a greedy approach of building a decision tree by selecting the best attribute that yields maximum information gain or minimum entropy.
- ID-3 algorithm has the following characteristics:
  - It does not guarantee an optimal solution; it can get stuck in local optima.
  - It can overfit to the training data (to avoid overfitting, smaller decision trees should be preferred over larger ones).
  - It does not handle continuous or missing attributes, nor does it prune the tree.
  - It uses a top-down, depth-first search strategy.
- ID-3 algorithm has the following steps  :
  - Start with the original set as the root node.
  - For each attribute of the data, calculate the entropy or the information gain of the attribute with respect to the class label.
  - Choose the attribute with the smallest entropy or the largest information gain as the splitting criterion for the node.
  - If the entropy is zero or the information gain is maximum, then the node is a leaf node and is labeled with the majority class.
  - If the entropy is not zero or the information gain is not maximum, then the node is an internal node and is split into sub-nodes according to the values of the attribute.
  - Repeat the process for each sub-node until all the nodes are either leaf nodes or cannot be split further.
- ID-3 algorithm is used by training on a data set to produce a decision tree which is stored in memory. At runtime, this decision tree is used to classify new test cases by traversing the decision tree using the features of the datum to arrive at a leaf node.