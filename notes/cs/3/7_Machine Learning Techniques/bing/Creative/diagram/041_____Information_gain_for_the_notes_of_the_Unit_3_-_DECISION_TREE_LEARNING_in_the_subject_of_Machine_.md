### Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a dataset  .
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a dataset  .
- Entropy can be calculated as:

![Entropy formula](https://latex.codecogs.com/png.latex?H%28S%29%20%3D%20-%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dp_i%5Clog_2p_i)

where S is the dataset, n is the number of possible class labels, and p_i is the proportion of instances that belong to the i-th class label  .

- Information gain can be calculated as:

![Information gain formula](https://latex.codecogs.com/png.latex?IG%28S%2CA%29%20%3D%20H%28S%29%20-%20%5Csum_%7Bv%20%5Cin%20Values%28A%29%7D%5Cfrac%7B%7CS_v%7C%7D%7B%7CS%7C%7DH%28S_v%29)

where S is the dataset, A is the feature to split on, Values(A) is the set of possible values for the feature A, S_v is the subset of S where A has the value v, and H(S_v) is the entropy of S_v  .

- Information gain measures the reduction in entropy after splitting the dataset on a feature  .
- Information gain helps to determine the order of attributes in the nodes of a decision tree  .
- The main node is referred to as the parent node, whereas sub-nodes are known as child nodes  .
- We can use information gain to determine how good the splitting of nodes in a decision tree is  .
- The feature with the highest information gain is chosen as the splitting attribute for the parent node  .
- This process is repeated recursively for each child node until all the instances in a node belong to the same class or there are no more features to split on  .
- Information gain can work with both continuous and discrete variables.
- Information gain can handle missing values by assigning them to the most common value of the feature.
- Information gain can be biased towards features with more values, as they tend to have higher entropy and thus higher information gain.
- Information gain can be normalized by dividing it by the intrinsic information of a feature, which is the entropy of the feature values.
- This normalized information gain is also known as the gain ratio.

: https://www.section.io/engineering-education/entropy-information-gain-machine-learning/
: https://analyticsindiamag.com/a-complete-guide-to-decision-tree-split-using-information-gain/
: https://en.wikipedia.org/wiki/Information_gain_(decision_tree)
: https://en.wikipedia.org/wiki/Information_gain_(decision_tree)#Advantages_and_disadvantages