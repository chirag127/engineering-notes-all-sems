### Inductive bias for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Inductive bias is the set of assumptions that a learning algorithm uses to predict outputs of given inputs that it has not encountered.
- Inductive bias is necessary for generalization, which is the ability of a learning algorithm to perform well on unseen data.
- Different learning algorithms have different inductive biases, which affect their performance and suitability for different problems.
- Decision tree learning is a learning algorithm that constructs a tree-like structure of rules to classify or predict data.
- Decision tree learning has the following inductive biases :
  - Shorter trees are preferred over longer trees. This is based on the principle of Occam's razor, which states that the simplest hypothesis that fits the data is the best.
  - Trees that place high information gain attributes close to the root are preferred over those that do not. This is based on the heuristic that attributes that are more informative or discriminative should be tested earlier.
  - The depth of the tree is the inductive bias. This is based on the assumption that the complexity of the tree is related to its depth, and that simpler trees are more likely to generalize better.