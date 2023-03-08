 Here are the key issues with Decision Tree Learning:

### Overfitting
Decision Trees can easily overfit the training data leading to poor generalisation. This happens when the tree is allowed to grow deep and fit the training data perfectly. Some ways to handle overfitting are:

- Pruning: Cutting off branches of the tree to reduce complexity
- Setting max depth for the tree
- Using Ensemble methods like Random Forest

### Numerical attributes
Decision Trees typically work on categorical attributes. For numerical data, the values have to be discretized which can lead to loss of information. Some solutions for this are:

- Finding optimal bins for discretization
- Using regression trees which can handle numerical values directly

### Handling class imbalance
If the training data is skewed with unequal distribution of classes, the tree can be biased towards the dominant class. Some techniques to handle this are:

- Oversampling the minority class
- Undersampling the majority class
- Using weighted training to increase importance of minority class

### Handling high dimensionality
With a large number of features, decision trees tend to overfit and the performance degrades due to curse of dimensionality. Feature selection and dimensionality reduction techniques can be applied to select relevant features before training a decision tree.

Overall, Decision Trees are simple to understand and interpret but care must be taken to tune the hyperparameters and use appropriate techniques to handle the issues and build an accurate model.

[Include diagrams/images/codes if required to explain the concepts]