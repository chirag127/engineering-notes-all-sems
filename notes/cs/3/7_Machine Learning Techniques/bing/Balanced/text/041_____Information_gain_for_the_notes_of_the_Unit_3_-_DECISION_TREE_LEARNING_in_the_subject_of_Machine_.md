### Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a dataset .
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a dataset .
- Information gain is calculated by comparing the entropy of the dataset before and after splitting it based on a feature .
- Information gain can be used as a criterion to select the best feature to split a node in a decision tree .
- Information gain can be expressed as:

  IG(S, A) = H(S) - H(S|A)

  where S is the dataset, A is the feature, H(S) is the entropy of S, and H(S|A) is the conditional entropy of S given A .

- Information gain can be interpreted as the reduction in entropy or surprise by splitting the dataset based on a feature .
- Information gain can help to build more compact and accurate decision trees by choosing the features that provide the most information about the class label .