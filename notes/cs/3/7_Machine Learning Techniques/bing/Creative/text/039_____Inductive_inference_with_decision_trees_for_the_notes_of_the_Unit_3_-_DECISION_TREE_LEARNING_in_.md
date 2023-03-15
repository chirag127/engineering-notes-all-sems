### Inductive inference with decision trees

- Decision tree learning is a method that uses **inductive inference** to approximate a **target function**, which will produce **discrete values**    .
- Inductive inference is the process of **generalizing** from a **finite set of examples** (training data) to a **hypothesis** that can make **predictions** for **unseen instances** (test data).
- A decision tree is a **graphical representation** of a **hypothesis** that can be easily **interpreted** and **converted** to **rules**    .
- A decision tree consists of **nodes** and **branches**. The nodes are either **internal** or **leaf**. The internal nodes represent **tests** on **attributes**. The branches represent the **outcomes** of the tests. The leaf nodes represent the **class labels** or **values** of the target function    .
- A decision tree can be used to **classify** an instance by **traversing** the tree from the **root** to a **leaf**, following the **branch** that corresponds to the **value** of the **attribute** tested at each **node**    .
- A decision tree can be **learned** from a set of **training examples** by using a **top-down**, **greedy**, **divide-and-conquer** algorithm that **recursively** **partitions** the data into **subsets** based on the **best** **splitting** **criterion**    .
- The best splitting criterion is usually based on some **measure** of **information gain** or **impurity reduction** that evaluates how well an attribute **separates** the examples into **homogeneous** classes    .
- The recursion stops when all the examples in a subset belong to the **same** class, or when there are **no** more attributes to test, or when some **threshold** or **pruning** condition is met    .
- Decision tree learning is **widely used**, **robust** to **noisy data**, and considered a **practical** method for learning **disjunctive expressions**  .
- Decision tree learning can also handle **missing values**, **continuous attributes**, and **multivalued attributes** with some **extensions** or **modifications**    .