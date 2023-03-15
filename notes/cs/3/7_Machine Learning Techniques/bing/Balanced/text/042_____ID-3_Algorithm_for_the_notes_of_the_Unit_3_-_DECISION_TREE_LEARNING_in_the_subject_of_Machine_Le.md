### ID-3 Algorithm

- ID-3 stands for Iterative Dichotomiser 3, and it is an algorithm used to generate a decision tree from a dataset  .
- ID-3 follows a greedy approach of building a decision tree by selecting the best attribute that yields maximum information gain or minimum entropy at each node .
- ID-3 does not guarantee an optimal solution, as it can get stuck in local optima .
- ID-3 can overfit the training data, so smaller decision trees are preferred over larger ones .
- ID-3 uses the following metrics to measure the quality of a split:

  - Entropy: a measure of the randomness or uncertainty of a set of examples. It is calculated as:

    $$H(S) = -\sum_{i=1}^{n} p_i \log_2 p_i$$

    where $S$ is the set of examples, $n$ is the number of possible classes, and $p_i$ is the proportion of examples in $S$ that belong to class $i$.

  - Information gain: a measure of the reduction in entropy after splitting a set of examples on an attribute. It is calculated as:

    $$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

    where $S$ is the set of examples, $A$ is the attribute to split on, $Values(A)$ is the set of possible values for $A$, $S_v$ is the subset of examples in $S$ where $A$ has value $v$, and $|S|$ is the cardinality of $S$.

- ID-3 algorithm works as follows :

  - Start with the original set of examples as the root node.
  - If all examples in the node belong to the same class, or if there are no more attributes to split on, then stop and label the node with the majority class.
  - Otherwise, for each unused attribute, calculate the information gain or entropy of splitting the node on that attribute.
  - Choose the attribute with the highest information gain or lowest entropy as the best attribute to split on.
  - Create a child node for each possible value of the best attribute, and assign the subset of examples with that value to the corresponding child node.
  - Recursively apply the algorithm to each child node until all nodes are labeled with a class or no more attributes are available.