### Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and have a **guaranteed time complexity of O(log n)** for basic operations like insertion, deletion, and search .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf (NIL) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf contains the **same number of black nodes**. This number is called the **black-height** of the node.
- Red-black trees maintain these properties by **rotating** and **recoloring** the nodes after insertion or deletion .
- Red-black trees are used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - **Java Collections Framework**: The TreeMap and TreeSet classes are implemented using red-black trees.
  - **Linux kernel**: The Completely Fair Scheduler and the Ext4 file system use red-black trees.
  - **C++ STL**: The map, multimap, set, and multiset containers are typically implemented using red-black trees.
- Red-black trees are a special case of **B-trees** with order 4 and minimum degree 2. B-trees are another type of self-balancing search tree that can have more than two children per node and store multiple keys per node. B-trees are useful for storing large amounts of data on disk.