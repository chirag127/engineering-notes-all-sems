## Unit 3 - DECISION TREE LEARNING

- Decision tree learning is a method of supervised learning that uses a tree-like structure to represent a set of rules for classifying or predicting an outcome based on a set of input features.
- A decision tree consists of nodes, branches, and leaves. A node represents a test or a question on a feature, a branch represents an outcome or an answer to the test, and a leaf represents a class label or a prediction.
- The root node is the first node in the tree, and it has no incoming branches. The internal nodes are the nodes that have both incoming and outgoing branches. The leaf nodes are the nodes that have only incoming branches and no outgoing branches.
- The goal of decision tree learning is to find the best split at each node, such that the tree can accurately classify or predict the outcome for new instances.
- There are different algorithms for decision tree learning, such as ID3, C4.5, CART, etc. They differ in the way they measure the quality of a split, handle missing values, prune the tree, etc.
- Some common measures of the quality of a split are entropy, information gain, gini index, gain ratio, etc. They quantify the amount of uncertainty, information, or impurity in a node or a set of nodes.
- Entropy is a measure of the randomness or disorder in a node. It is calculated as:

  `Entropy(S) = - sum(p_i * log2(p_i))` for i = 1 to n

  where S is a set of instances, p_i is the proportion of instances in S that belong to class i, and n is the number of classes.
- Information gain is a measure of the reduction in entropy after a split. It is calculated as:

  `InformationGain(S, A) = Entropy(S) - sum((|S_v| / |S|) * Entropy(S_v))` for v in Values(A)

  where S is a set of instances, A is an attribute, Values(A) is the set of possible values of A, S_v is the subset of S where A has value v, and |S| is the cardinality of S.
- Gini index is a measure of the impurity or the probability of misclassification in a node. It is calculated as:

  `Gini(S) = 1 - sum(p_i^2)` for i = 1 to n

  where S is a set of instances, p_i is the proportion of instances in S that belong to class i, and n is the number of classes.
- Gain ratio is a measure of the information gain normalized by the intrinsic information of a split. It is calculated as:

  `GainRatio(S, A) = InformationGain(S, A) / SplitInformation(S, A)`

  where S is a set of instances, A is an attribute, and SplitInformation(S, A) is the entropy of the distribution of values of A in S.
- Pruning is a technique of reducing the size and complexity of a decision tree by removing nodes that do not contribute much to the accuracy or generalization of the tree. Pruning can be done either during the tree construction (pre-pruning) or after the tree is fully grown (post-pruning).
- Some common methods of pruning are reduced error pruning, minimum error pruning, cost complexity pruning, etc. They use different criteria to decide which nodes to prune, such as validation error, minimum error threshold, cost complexity measure, etc.