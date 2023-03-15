# ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3  .
- It is a classification algorithm that follows a greedy approach of building a decision tree by selecting the best attribute that yields maximum information gain or minimum entropy .
- It is a precursor to the C4.5 algorithm, and is typically used in machine learning and natural language processing domains.
- The algorithm begins with the original set as the root node. On each iteration, it iterates through every unused attribute of the set and calculates the entropy or the information gain of that attribute. It then selects the attribute which has the smallest entropy or the largest information gain value.
- The algorithm then splits the set into subsets based on the values of the selected attribute, and repeats the process recursively for each subset until one of the following conditions is met:
  - The subset is pure, meaning all the instances belong to the same class.
  - There are no more unused attributes.
  - There are no more instances.
- The algorithm then returns a decision tree that can be used to classify new test cases by traversing the tree using the features of the datum to arrive at a leaf node.
- The algorithm has some limitations, such as :
  - It does not guarantee an optimal solution, as it can get stuck in local optima.
  - It can overfit to the training data, meaning it may not generalize well to unseen data. To avoid overfitting, smaller decision trees should be preferred over larger ones, and techniques such as pruning, regularization, or cross-validation can be applied.
  - It can only handle nominal attributes, meaning it cannot deal with continuous or ordinal attributes. To handle such attributes, they need to be discretized or converted into nominal values.