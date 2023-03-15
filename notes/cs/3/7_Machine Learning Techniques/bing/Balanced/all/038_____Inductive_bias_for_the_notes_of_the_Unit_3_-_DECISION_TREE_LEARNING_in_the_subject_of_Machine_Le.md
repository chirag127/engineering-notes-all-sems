# Inductive bias for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Inductive bias is the set of assumptions that a learning algorithm uses to predict outputs of given inputs that it has not encountered.
- Inductive bias is necessary for generalization, which is the ability of a learning algorithm to perform well on unseen data.
- Different learning algorithms have different inductive biases, which affect their performance and suitability for different problems.
- Decision tree learning is a learning algorithm that constructs a tree-like structure to represent the possible outcomes of a decision based on a set of attributes.
- Decision tree learning uses a greedy top-down approach to split the data into subsets based on the attribute that maximizes the information gain.
- Information gain is a measure of how much the entropy (uncertainty) of the data decreases after splitting on an attribute.
- Entropy is a measure of how much the data is mixed or impure, i.e., how much the data belongs to different classes.
- The inductive bias of decision tree learning is that shorter trees are preferred over longer trees, and trees that place high information gain attributes close to the root are preferred over those that do not.
- This inductive bias is based on the principle of Occam's razor, which states that the simplest hypothesis that fits the data is the best.
- The inductive bias of decision tree learning can be influenced by the choice of the splitting criterion, the pruning strategy, and the ordering of the attributes.