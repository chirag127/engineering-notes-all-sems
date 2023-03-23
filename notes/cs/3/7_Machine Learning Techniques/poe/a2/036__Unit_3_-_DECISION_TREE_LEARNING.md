 Here is the formal content in Markdown format without any emojis or external links:

## Unit 3 - DECISION TREE LEARNING

1. Decision Tree Learning is a type of supervised learning algorithm (i.e. it requires labeled data for training) that uses a tree-like model of decisions and their possible consequences.

2. It works for both classification and regression problems. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features.

3. The key steps involved in Decision Tree Learning are:

- Gathering the data
- Selecting the attribute/feature that best splits the data (requires a metric to calculate the "goodness" of a split)
- Creating subsets/branches for each attribute value
- Repeating step#2 and #3 on each sub-tree/subset until the subset is pure or contains a small number of instances

4. Some pros and cons of Decision Tree Learning are:

Pros:
- Easy to interpret
- Requires little data preprocessing
- Can handle both numerical and categorical data

Cons:
- Can overfit the training data
- Can be unstable and vary based on minor changes in the data
- Performance can degrade rapidly with increase in dimensionality of the data

5. The key hyperparameters to tune in Decision Tree Learning are:

- Max depth of the tree (controls overfitting vs underfitting)
- Minimum number of samples required to split an internal node
- Minimum number of samples required in a leaf node
- Criterion to measure the goodness of a split (Gini index or Information gain are commonly used)