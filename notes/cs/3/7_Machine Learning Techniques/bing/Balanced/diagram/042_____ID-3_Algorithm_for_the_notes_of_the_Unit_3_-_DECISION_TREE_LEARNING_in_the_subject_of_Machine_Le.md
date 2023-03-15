### ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3, which is a learning algorithm for decision tree introduced by Ross Quinlan in 1986 .
- ID-3 is an iterative algorithm where a subset (window) of the training set is chosen at random to build a decision tree. This tree will classify every object within this window correctly.
- ID-3 uses the concept of information gain to select the best attribute for splitting the data at each node of the tree. Information gain is the difference between the entropy of the parent node and the weighted average entropy of the child nodes .
- ID-3 follows these steps to construct a decision tree  :
  - Start with the root node that contains all the data.
  - If all the data belong to the same class, then the node is a leaf node and the class label is assigned to it.
  - If the data are not homogeneous, then select the attribute that has the highest information gain among the remaining attributes.
  - Split the data based on the values of the selected attribute and create a child node for each value.
  - Repeat the process for each child node until all the data are classified or no more attributes are left.
- ID-3 has some limitations, such as  :
  - It can only handle categorical attributes and binary classes.
  - It does not handle missing values or noisy data.
  - It can overfit the data and create complex trees that do not generalize well.
  - It uses a greedy approach that does not guarantee an optimal solution.