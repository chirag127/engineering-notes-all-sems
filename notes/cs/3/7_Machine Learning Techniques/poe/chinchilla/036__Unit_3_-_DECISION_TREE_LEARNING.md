## Unit 3 - DECISION TREE LEARNING

Decision tree learning is a popular and widely used machine learning technique that is used for both classification and regression tasks. It involves building a tree-like structure in which each internal node represents a test on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label or a numerical value.

### What are decision trees?

Decision trees are a type of supervised learning algorithm that is used for both classification and regression tasks. A decision tree is a hierarchical structure that is built by recursively partitioning the data into subsets based on the values of the input features. Each internal node of the tree represents a test on one of the input features, and the branches represent the possible outcomes of the test. The leaf nodes represent the output values, which can be either class labels or numerical values.

### How do decision trees work?

Decision trees work by recursively partitioning the data into subsets based on the values of the input features. The decision tree is built by selecting the input feature that provides the most information about the target variable. This is done by calculating the information gain or the Gini index.

Once the feature with the highest information gain or the lowest Gini index is selected, the data is split into subsets based on the values of the selected feature. This process is repeated for each subset until the data is completely partitioned into pure subsets, i.e., all the examples in a subset belong to the same class label or have the same numerical value.

### Advantages of decision trees

- Decision trees are easy to understand and interpret.
- Decision trees can handle both categorical and numerical input features.
- Decision trees can handle missing values and outliers.
- Decision trees can be used for both classification and regression tasks.
- Decision trees can be used for feature selection.

### Disadvantages of decision trees

- Decision trees can easily overfit the data.
- Decision trees can be unstable, i.e., small changes in the data can result in large changes in the tree structure.
- Decision trees can be biased towards features with many values or high cardinality.
- Decision trees can be sensitive to the order of the input features.

### Conclusion

Decision tree learning is a powerful and widely used machine learning technique that is used for both classification and regression tasks. Decision trees are easy to understand and interpret, and they can handle both categorical and numerical input features. However, decision trees can easily overfit the data and can be unstable. Therefore, it is important to carefully tune the hyperparameters of the decision tree algorithm and to use techniques such as pruning and ensembling to improve the performance of the model.