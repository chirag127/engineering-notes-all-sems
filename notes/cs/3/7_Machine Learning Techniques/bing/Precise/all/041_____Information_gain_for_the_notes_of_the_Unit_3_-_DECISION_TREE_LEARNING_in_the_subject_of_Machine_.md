### Information Gain

Information gain is a measure used in decision tree learning to determine the best attribute to split the data on at each level of the tree. It is calculated by comparing the entropy of the dataset before and after the split.

- **Entropy** is a measure of the impurity or disorder of a dataset. It is calculated as the negative sum of the probabilities of each class in the dataset multiplied by the logarithm of the probabilities.

- The **information gain** for an attribute is calculated as the difference between the entropy of the dataset before the split and the weighted average of the entropies of the datasets after the split.

- The attribute with the highest information gain is chosen as the splitting attribute at each level of the decision tree.

- Information gain is used to build a decision tree that can accurately classify new instances by recursively splitting the data on the attribute with the highest information gain until all instances in a subset belong to the same class or the tree reaches a predefined maximum depth.

- Information gain is an effective measure for decision tree learning, but it can be biased towards attributes with many values. To overcome this bias, other measures such as gain ratio or gini index can be used.

- Information gain is also known as mutual information or Kullback-Leibler divergence.