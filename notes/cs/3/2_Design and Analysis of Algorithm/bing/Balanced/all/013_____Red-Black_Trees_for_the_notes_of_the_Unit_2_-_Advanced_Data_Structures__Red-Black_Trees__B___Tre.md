# Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and have a **guaranteed time complexity of O(log n)** for basic operations like insertion, deletion, and search .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**. This can be stored as a single bit in memory (e.g. 'red' = 1, 'black' = 0).
  - The **root** of the tree is always **black**.
  - Every **leaf** (null pointer) is considered **black**.
  - If a node is **red**, then both its **children** are **black**.
  - Every **simple path** from a node to a descendant leaf contains the **same number** of **black nodes**. This number is called the **black height** of the node.
- Red-black trees maintain these properties by performing **rotations** and **recoloring** operations after insertion or deletion of nodes. These operations ensure that the tree remains **approximately balanced** and that the **height** of the tree is **logarithmic** in the number of nodes .
- Red-black trees are used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - **C++ STL** (Standard Template Library) uses red-black trees to implement **map**, **multimap**, **set**, and **multiset** containers.
  - **Java Collections Framework** uses red-black trees to implement **TreeMap**, **TreeSet**, and **ConcurrentSkipListMap** classes.
  - **Linux kernel** uses red-black trees to manage **virtual memory areas**, **epoll** (event polling) system call, and **timer** data structures.
  - **Git** (version control system) uses red-black trees to store **directory contents** and **file names**.
  - **MongoDB** (database system) uses red-black trees to implement **indexes** on collections and documents.