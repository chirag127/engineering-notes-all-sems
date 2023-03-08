 Here is the content in markdown format for the topic ## Unit 3 - DECISION TREE LEARNING:

## Unit 3 - DECISION TREE LEARNING

Decision Tree Learning is a supervised learning algorithm which is used for both classification and regression problems. However, it is mainly used for solving classification problems. It uses a tree-like model of decisions and their possible consequences. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data.

Some key points about Decision Tree Learning:

- It is a white-box model, i.e. the learned tree can be easily interpreted by humans. The learned tree shows the hierarchical relationship between features and the target variable.
- It is non-parametric and does not make any assumptions about the underlying data distribution.
- The entire learning process can be represented graphically as a tree which makes it easy to understand.
- It performs well even if the input features are unscaled.
- It tends to overfit the training data easily due to which it can result in poor performance on unseen data. Hence, pruning techniques like cost-complexity pruning are commonly used to reduce overfitting.
- Some algorithms used to generate decision trees are ID3, C4.5, CART, CHAID, etc.

Steps involved in Decision Tree Learning:

1. Select the best attribute to split the data: Choose the attribute which results in the most homogenous partitions (subgroups). The measure of homogeneity is calculated based on the target variable and is known as impurity. Gini index and Information gain are commonly used impurity measures.
2. Split the data: Split the data into subsets based on the values of the chosen attribute.
3. Repeat 1 and 2 on each partition recursively until stopping criteria is met. The stopping criteria can be max depth of the tree, minimum number of instances in a leaf node, etc.
4. Label the leaf nodes: Assign a classification label to each leaf node based on the target values of the training instances it contains.

[Include diagrams, formulas, codes, applications, advantages, disadvantages, etc. if required]