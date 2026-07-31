 Here is the formal write-up in Markdown format without any emojis or external links for the given topic:

### Case-based learning for the notes of the Unit 3 - DECISION TREE LEARNING

1. Decision Tree Learning is a supervised learning technique that can be used for both classification and regression problems.

2. In Decision Tree Learning, we split the population or sample into two or more homogeneous sets (or sub-populations) based on most significant splitter or differentiator in input variables.

3. The splitting is done recursively on each subset in a greedy manner until the subset at a node has all the same target values or until it meets defined stopping criteria.

4. The split is done based on an impurity measure like Gini Index or Information Gain (for classification problems) or Mean Squared Error (for regression problems). The split that results in most homogeneous subsets is chosen.

5. The result is a tree-like model of decisions that classify a new data instance starting from the root node and moving through the decision nodes until a leaf node (terminal node) is reached. The prediction is the target value of the training instances in that leaf node.

6. Some advantages of Decision Tree Learning are:

- It is easy to understand and interpret.
- It can handle both numerical and categorical data.
- It is memory efficient as it stores only the learned tree structure.
- It can handle multi-output problems.

7. Some disadvantages of Decision Tree Learning are:

- It can lead to overfitting if the tree is too deep.
- It can be unstable and lead to different trees due to small changes in the data.
- It does not naturally provide probability estimates.
- It works well with relatively small datasets. Larger datasets require preprocessing to reduce dimensionality and training time.