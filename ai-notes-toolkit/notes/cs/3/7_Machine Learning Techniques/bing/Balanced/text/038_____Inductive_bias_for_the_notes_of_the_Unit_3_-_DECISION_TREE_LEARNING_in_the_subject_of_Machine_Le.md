### Inductive bias for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Inductive bias is the set of assumptions that a learning algorithm uses to predict outputs of given inputs that it has not encountered .
- Inductive bias is necessary for generalization, which is the ability of a learning algorithm to perform well on unseen data.
- Different learning algorithms have different inductive biases, which affect their performance and suitability for different problems.
- Decision tree learning is a learning algorithm that constructs a tree-like structure of rules to classify or predict data.
- Decision tree learning has two main components: the tree induction algorithm and the tree pruning algorithm.
- The tree induction algorithm recursively splits the data into subsets based on the values of the attributes, until the subsets are pure or small enough.
- The tree pruning algorithm removes or simplifies some of the branches of the tree to reduce overfitting and improve generalization.
- The inductive bias of decision tree learning is the preference for shorter and simpler trees over longer and more complex ones .
- The inductive bias of decision tree learning is also influenced by the choice of the splitting criterion, which determines how to select the best attribute to split the data at each node.
- Some common splitting criteria are information gain, gain ratio, and gini index.
- Information gain measures the reduction in entropy (or uncertainty) after splitting the data by an attribute.
- Gain ratio adjusts the information gain by the intrinsic information of the attribute, which is the entropy of the attribute values.
- Gini index measures the impurity of the data, which is the probability of misclassification after splitting the data by an attribute.
- The inductive bias of decision tree learning can be summarized as: trees that place high information gain (or gain ratio or low gini index) attributes close to the root are preferred over those that do not .