# Decision tree learning algorithm

- A decision tree is a **supervised learning algorithm** that is used for both **classification and regression** tasks .
- It has a **hierarchical, tree structure**, which consists of a **root node**, **branches**, **internal nodes** and **leaf nodes** .
- The root node is the **topmost node** that represents the **entire dataset**.
- The branches are the **edges** that connect the nodes and represent the **conditions** or **tests** on the features of the dataset .
- The internal nodes are the **non-terminal nodes** that perform the **decisions** or **splits** based on the feature values .
- The leaf nodes are the **terminal nodes** that represent the **final outcomes** or **class labels** .
- The goal of a decision tree is to **partition** the dataset into **homogeneous** or **pure** subsets based on the target variable .
- The purity or homogeneity of a subset is measured by **impurity** or **entropy** metrics, such as **information gain**, **gain ratio**, **gini index** or **variance reduction**  .
- The decision tree learning algorithm is a **recursive**, **greedy** and **top-down** approach that starts from the root node and **repeatedly** selects the **best attribute** to split the data using an **attribute selection measure** (ASM) until a **stopping criterion** is met  .
- The stopping criterion can be based on the **maximum depth** of the tree, the **minimum number** of samples in a node, the **minimum improvement** in impurity or entropy, or the **pruning** of the tree to avoid **overfitting**  .
- The basic algorithm used in decision trees is known as the **ID3** (by Quinlan) algorithm, which uses **information gain** as the ASM and **categorical** features.
- Other variants of decision tree algorithms are **C4.5** (an extension of ID3 that can handle **numerical** features and **missing values**), **CART** (Classification and Regression Trees that can perform both **classification** and **regression** using **gini index** or **variance reduction** as the ASM), and **CHAID** (Chi-squared Automatic Interaction Detection that uses **chi-squared test** to find the best split) .