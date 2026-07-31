# Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a dataset.
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a dataset.
- Information gain helps to determine the order of attributes in the nodes of a decision tree. The main node is referred to as the parent node, whereas sub-nodes are known as child nodes.
- Information gain is calculated by subtracting the entropy of the child nodes from the entropy of the parent node.
- Information gain can be expressed as:

    IG(S, A) = H(S) - H(S|A)

    where S is the dataset, A is the attribute, H(S) is the entropy of S, and H(S|A) is the conditional entropy of S given A.

- Information gain can be used to select the best attribute for splitting a node in a decision tree. The attribute with the highest information gain is chosen as the splitting criterion.
- Information gain can work with both continuous and discrete variables.
- Information gain can handle missing values by assigning them to a separate branch or by using a probabilistic approach.
- Information gain can be biased towards attributes with more values or levels, as they tend to have higher entropy and thus higher information gain.
- Information gain can be normalized by dividing it by the intrinsic information of the attribute, which is the entropy of the attribute values. This is called the gain ratio.