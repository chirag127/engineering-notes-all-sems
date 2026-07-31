 Here is the formal markdown content on the topic Decision tree learning algorithm for the notes of the Unit 3 - DECISION TREE LEARNING in the subject of Machine Learning Techniques:

### Decision Tree Learning Algorithm

1. Decision tree is a supervised learning algorithm which is used for both classification and regression problems.
2. In decision tree learning, a tree-like model of decisions and their possible consequences is created. The root node contains the first decision to be made, and subsequent child nodes contain subsequent decisions or possible outcomes.
3. Some key aspects of decision tree learning algorithm are:
- It is a white-box model, i.e. the reasoning behind the classification or prediction is explicit and interpretable. The learned tree can be intuitively understood and interpreted by humans.
- It performs multi-class classification naturally.
- It can handle both numerical and categorical data.
- It is robust to outliers and does not require data normalization.
- It can suffer from high variance and can overfit the training data easily.
- The final tree size depends heavily on the training data.

4. The basic steps involved in creating a decision tree are:

- Choose an attribute to split the data on. This is done using various measures such as Information gain, Gini index, etc.
- Split the data into subsets based on the chosen attribute.
- Repeat step#1 and 2 on each subset until the subset is pure or contains instances of only one class.
- The recursion is stopped, and the subtree is used to predict the class of unknown instances.

5. Some pros and cons of decision tree algorithm are:

Pros:
- Easy to understand and interpret.
- Requires little data preprocessing.
- Can handle both numerical and categorical data.
- Useful for exploratory data analysis.

Cons:
- Can suffer from high variance and overfitting.
- Does not perform well with large and complex datasets.
- The resulting tree can be quite complex and include many conditions/rules.
- Can be unstable, i.e. small changes in the data can result in a different tree being generated.