### Information gain for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques

- Information gain is a measure of how much information a feature provides about the class label of a data set  .
- Information gain is based on the concept of entropy, which is the degree of uncertainty or randomness in a data set  .
- The higher the entropy, the more difficult it is to predict the class label of a data point  .
- The lower the entropy, the more homogeneous or pure the data set is  .
- Information gain is calculated as the difference between the entropy of the parent node and the weighted average entropy of the child nodes after splitting by a feature  .
- Information gain helps to determine the order of attributes in the nodes of a decision tree  .
- The feature that has the highest information gain is chosen as the splitting criterion at each node of the decision tree  .
- The goal of information gain is to reduce the entropy or increase the purity of the data set at each node of the decision tree  .
- Information gain can work with both continuous and discrete variables.
- Information gain can be expressed mathematically as:

![Information gain formula](https://latex.codecogs.com/png.latex?IG%28S%2CA%29%20%3D%20H%28S%29%20-%20%5Csum_%7Bv%20%5Cin%20Values%28A%29%7D%20%5Cfrac%7B%7CS_v%7C%7D%7B%7CS%7C%7D%20H%28S_v%29)

where:

  - IG(S,A) is the information gain of splitting a data set S by a feature A
  - H(S) is the entropy of the data set S
  - Values(A) is the set of possible values of the feature A
  - S_v is the subset of S where the feature A has the value v
  - |S| is the number of data points in S
  - |S_v| is the number of data points in S_v
  - H(S_v) is the entropy of the subset S_v