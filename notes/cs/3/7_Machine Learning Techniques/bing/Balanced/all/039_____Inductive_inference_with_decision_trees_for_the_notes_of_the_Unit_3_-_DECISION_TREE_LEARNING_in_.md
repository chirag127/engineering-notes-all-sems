# Inductive inference with decision trees

- Decision tree learning is a method that uses **inductive inference** to approximate a **target function**, which will produce **discrete values**    .
- Inductive inference is the process of **generalizing** from a set of **training examples** to a **hypothesis** that can make **predictions** for unseen **test examples**.
- A target function is the **true** function that maps the **input** to the **output** .
- A decision tree is a **graphical** representation of a **hypothesis** that consists of **nodes**, **branches**, and **leaves**    .
- A node is a point in the tree where a **test** is performed on an **attribute** of the input    .
- A branch is a link between two nodes that represents the **outcome** of a test    .
- A leaf is a node that has no children and specifies the **value** of the target function    .
- An example of a decision tree is shown below:

![Decision tree example](https://upload.wikimedia.org/wikipedia/commons/f/f3/CART_tree_titanic_survivors.png)

- The decision tree learning algorithm is a **greedy** and **top-down** method that **recursively** partitions the **training data** into **subsets** based on the **best** attribute at each level    .
- The best attribute is the one that **maximizes** the **information gain** or **minimizes** the **entropy** of the data    .
- Information gain is the **reduction** in entropy caused by partitioning the data on an attribute    .
- Entropy is a measure of the **uncertainty** or **impurity** of a data set    .
- The decision tree learning algorithm stops when all the data in a subset belong to the **same** class, or when there are no more attributes to test, or when a **predefined** limit is reached    .
- The decision tree learning algorithm can handle **categorical** and **numerical** attributes, **missing** values, and **noisy** data    .
- The advantages of decision tree learning are that it is **simple**, **interpretable**, **robust**, and **fast**    .
- The disadvantages of decision tree learning are that it can be **overfitting**, **unstable**, and **biased**    .
- Overfitting is when the decision tree is too **complex** and **specific** to the training data, and fails to **generalize** well to the test data    .
- Unstable is when the decision tree is sensitive to **small** changes in the training data, and produces **different** trees    .
- Biased is when the decision tree favors some attributes over others, and ignores some **relevant** features    [^6^