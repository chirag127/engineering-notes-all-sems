# Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a given dataset .
- Information gain is based on the concept of entropy, which is a measure of the uncertainty or randomness of a set of data .
- Entropy can be calculated as:

$$
Entropy(S) = -\sum_{i=1}^{c} p_i \log_2 p_i
$$

where $S$ is the set of data, $c$ is the number of classes, and $p_i$ is the proportion of data belonging to class $i$ .

- Information gain can be calculated as:

$$
InformationGain(S, A) = Entropy(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} Entropy(S_v)
$$

where $S$ is the set of data, $A$ is a feature, $Values(A)$ is the set of possible values of $A$, $S_v$ is the subset of data where $A$ has value $v$, and $|S|$ and $|S_v|$ are the cardinalities of $S$ and $S_v$ respectively  .

- Information gain helps to determine the order of attributes in the nodes of a decision tree. The main node is referred to as the parent node, whereas sub-nodes are known as child nodes .
- The attribute with the highest information gain is chosen as the splitting criterion for the parent node. The data is then partitioned according to the values of that attribute, and the process is repeated for each child node until a leaf node is reached  .
- The goal of information gain is to reduce the entropy of the data as much as possible, which means to increase the purity or homogeneity of the data in each node  .
- Information gain can work with both continuous and discrete variables. For continuous variables, a threshold value can be chosen to split the data into two subsets.
- Information gain is also known as Kullback-Leibler divergence or relative entropy. It can be interpreted as the difference between the prior and posterior distributions of the class label given a feature.
- Information gain is one of the metrics used to train decision trees. Other metrics include Gini index, Chi-square, and Gain ratio . Each metric has its own advantages and disadvantages, and the choice of metric depends on the data and the problem .