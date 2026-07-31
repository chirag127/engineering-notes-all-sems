### Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a given dataset .
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a dataset .
- Entropy can be calculated as:

$$
Entropy(S) = -\sum_{i=1}^{c} p_i \log_2 p_i
$$

where $S$ is the dataset, $c$ is the number of classes, and $p_i$ is the proportion of instances that belong to class $i$ .

- Information gain can be calculated as:

$$
InformationGain(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Entropy(S_v)
$$

where $S$ is the dataset, $A$ is a feature, $Values(A)$ is the set of possible values of $A$, and $S_v$ is the subset of $S$ where $A$ has value $v$ .

- Information gain measures the reduction in entropy or the increase in purity of a dataset after splitting it based on a feature .
- Information gain helps to determine the order of attributes in the nodes of a decision tree. The main node is referred to as the parent node, whereas sub-nodes are known as child nodes.
- We can use information gain to determine how good the splitting of nodes in a decision tree is. The higher the information gain, the better the split .
- Information gain can work with both continuous and discrete variables.
- Information gain is also known as Kullback-Leibler divergence or relative entropy.
- Information gain is one of the metrics used to train decision trees. Other metrics include Gini index, Chi-square, and Gain ratio .