# Inductive bias for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Inductive bias is the set of assumptions that a learning algorithm uses to predict outputs of given inputs that it has not encountered.
- Inductive bias is necessary for generalization, which is the ability of a learning algorithm to perform well on unseen data.
- Different learning algorithms have different inductive biases, which affect their performance and suitability for different problems.
- Decision tree learning is a learning algorithm that constructs a tree-like structure to represent the possible outcomes of a series of decisions based on the input features.
- Decision tree learning uses a greedy top-down search strategy to find the best split at each node of the tree.
- The best split is determined by a criterion such as information gain, which measures the reduction in entropy (uncertainty) after splitting the data on a feature.
- The inductive bias of decision tree learning is that shorter trees are preferred over longer trees, and trees that place high information gain attributes close to the root are preferred over those that do not.
- This inductive bias is also known as the Occam's razor principle, which states that the simplest hypothesis that fits the data is preferred.
- The inductive bias of decision tree learning can be influenced by factors such as the order of the features, the pruning of the tree, and the choice of the splitting criterion.
- The inductive bias of decision tree learning can be beneficial or detrimental depending on the problem domain and the data distribution.