### ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3, an algorithm invented by Ross Quinlan to generate a decision tree from a dataset .
- ID-3 is a classification algorithm that follows a greedy approach of building a decision tree by selecting the best attribute that yields maximum information gain or minimum entropy.
- ID-3 is typically used in the machine learning and natural language processing domains.
- The main steps of ID-3 algorithm are as follows  :
  - Start with the original set as the root node.
  - For each attribute of the set, calculate the entropy or the information gain of the set by splitting on that attribute.
  - Choose the attribute with the smallest entropy or the largest information gain as the splitting criterion for the node.
  - Create a child node for each possible value of the chosen attribute and assign the subset of the data with that value to the child node.
  - If the subset is pure (all instances have the same class label) or there are no more attributes to split on, then stop and make the node a leaf node with the class label as the output.
  - Otherwise, repeat the process for each child node with the remaining attributes.
- ID-3 algorithm has some limitations, such as :
  - It can overfit the training data, especially if the tree is too large or the attributes are too many or noisy.
  - It can only handle nominal attributes, not numeric or continuous ones.
  - It can only handle binary classification problems, not multi-class ones.
  - It does not handle missing values or unknown attribute values.
  - It does not guarantee an optimal solution, as it can get stuck in local optima.