### Inductive bias for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Inductive bias is the set of assumptions that a learning algorithm uses to predict outputs for inputs that it has not encountered before .
- Inductive bias is necessary for generalization, which is the ability of a learning algorithm to perform well on unseen data, not just on the training data.
- Different learning algorithms have different inductive biases, which affect their performance and suitability for different problems.
- Decision tree learning is a learning algorithm that constructs a tree-like structure of nodes and branches, where each node represents a test on an attribute, and each branch represents an outcome of the test.
- The leaf nodes of the tree represent the class labels or the target values of the instances.
- Decision tree learning can be used for both classification and regression problems.
- Decision tree learning uses a top-down, greedy, recursive partitioning approach to construct the tree, starting from the root node and splitting the data based on some criterion.
- The criterion for splitting the data can be based on different measures of impurity or information gain, such as entropy, gini index, or chi-square test .
- The splitting process stops when a node becomes pure (contains only one class) or when a predefined stopping condition is met, such as the maximum depth of the tree or the minimum number of instances in a node.
- The inductive bias of decision tree learning is the assumption that the target function can be approximated by a tree-like structure of simple tests on the attributes.
- Another inductive bias of decision tree learning is the preference for shorter and simpler trees over longer and more complex ones, which follows the principle of Occam's razor .
- The inductive bias of decision tree learning can be influenced by the choice of the splitting criterion, the pruning method, and the ordering of the attributes .
- The inductive bias of decision tree learning can be beneficial for problems that have a hierarchical or compositional structure, where the target function can be decomposed into simpler sub-functions based on the attributes.
- The inductive bias of decision tree learning can be detrimental for problems that have a linear or smooth structure, where the target function cannot be easily represented by a series of binary tests.
- The inductive bias of decision tree learning can be evaluated by comparing the performance of the algorithm on different datasets, using cross-validation, or using theoretical bounds on the generalization error .