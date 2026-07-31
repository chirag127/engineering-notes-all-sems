### Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and **efficient** for storing and retrieving ordered data .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf (null node) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf contains the same number of **black** nodes. This number is called the **black-height** of the node.
- Red-black trees maintain these properties by performing **rotations** and **recoloring** operations after insertion or deletion of nodes .
- Red-black trees have a **guaranteed time complexity** of O(log n) for basic operations like insertion, deletion, and search .
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing **associative arrays** and **multisets**.
  - Implementing **priority queues** and **scheduling algorithms**.
  - Implementing **interval trees** and **augmented trees**.
  - Implementing **concurrent data structures** and **garbage collection**.