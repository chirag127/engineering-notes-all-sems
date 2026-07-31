# Inductive inference with decision trees

- Decision tree learning is a method that uses **inductive inference** to approximate a **target function**, which will produce **discrete values**    .
- Inductive inference is the process of **generalizing** from a set of **training examples** to a **hypothesis** that can make **predictions** for unseen **test examples**.
- A target function is the **true** function that maps the **input** to the **output**.
- A decision tree is a **graphical** representation of a **hypothesis** that consists of **nodes**, **branches**, and **leaves**    .
- A node is a point in the tree where a **test** is performed on an **attribute** of the input    .
- A branch is a connection between two nodes that represents the **outcome** of a test    .
- A leaf is a node that has no children and specifies the **value** of the target function for the input that reaches that node    .
- An example of a decision tree is shown below:

![Decision tree example](https://upload.wikimedia.org/wikipedia/commons/f/f3/CART_tree_titanic_survivors.png)

- The decision tree learning algorithm is a **greedy**, **top-down**, **recursive** procedure that **splits** the training examples into **subsets** based on the **best** attribute at each node    .
- The best attribute is the one that **maximizes** the **information gain** or **minimizes** the **entropy** of the subsets    .
- Information gain is the **reduction** in entropy caused by partitioning the examples according to an attribute    .
- Entropy is a measure of the **uncertainty** or **impurity** of a set of examples    .
- The algorithm stops when all the examples in a subset have the **same** value for the target function or when there are **no** more attributes to test    .
- The advantages of decision tree learning are that it is **widely used**, **robust** to noisy data, and **practical** for learning **disjunctive** expressions   .
- The disadvantages of decision tree learning are that it can **overfit** the data, **ignore** some attributes, and **suffer** from the **NP-hard** problem of finding the optimal tree    .