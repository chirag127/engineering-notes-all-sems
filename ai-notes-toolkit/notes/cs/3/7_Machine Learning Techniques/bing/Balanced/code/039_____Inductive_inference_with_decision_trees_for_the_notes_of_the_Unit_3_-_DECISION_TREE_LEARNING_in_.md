# Inductive inference with decision trees

- Decision tree learning is a method that uses inductive inference to approximate a target function, which will produce discrete values    .
- Inductive inference is the process of generalizing from a set of observed examples to a hypothesis that can make predictions for unseen examples.
- Decision trees are graphical representations of the learned function, where each node corresponds to a test on an attribute, and each branch corresponds to a possible outcome of the test    .
- The leaf nodes of the decision tree represent the class labels or values of the target function    .
- Decision trees can be converted to equivalent sets of if-then-else rules, where each rule corresponds to a path from the root to a leaf    .
- Decision tree learning is widely used, robust to noisy data, and capable of learning disjunctive expressions    .
- Disjunctive expressions are logical formulas that consist of one or more disjunctions (or clauses), where each disjunction is a conjunction of one or more literals.
- A literal is an atomic proposition or its negation.
- For example, the expression (A and B) or (C and not D) is a disjunctive expression with two disjunctions, each containing two literals.
- Decision tree learning algorithms typically use a top-down, greedy, divide-and-conquer approach to construct the tree from a given set of training examples    .
- The algorithm starts with an empty tree and recursively splits the examples based on the attribute that best separates the classes or minimizes the error    .
- The algorithm stops when all the examples belong to the same class, or when there are no more attributes to split on, or when a predefined limit is reached    .
- The algorithm may also prune the tree after construction to remove or simplify nodes that do not contribute to the accuracy or generalization of the learned function    .
- There are different criteria for choosing the best attribute to split on, such as information gain, gain ratio, gini index, or chi-square test    .
- These criteria measure the degree of impurity or uncertainty in the examples before and after the split, and aim to maximize the information gain or minimize the impurity    .
- Information gain is based on the concept of entropy, which quantifies the amount of disorder or randomness in a set of examples    .
- Entropy is defined as:

![Entropy formula](https://latex.codecogs.com/png.latex?Entropy(S)&space;=&space;-\sum_{i=1}^{c}&space;P_i&space;\log_2&space;P_i)

where S is the set of examples, c is the number of classes, and P_i is the proportion of examples that belong to class i    .

- Information gain is defined as:

![Information gain formula](https://latex.codecogs.com/png.latex?Gain(S,A)&space;=&space;Entropy(S)&space;-&space;\sum_{v&space;\in&space;Values(A)}&space;\frac{|S_v|}{|S|}&space;Entropy(S_v))

where A is the attribute to split on, Values(A) is the set of possible values of A,