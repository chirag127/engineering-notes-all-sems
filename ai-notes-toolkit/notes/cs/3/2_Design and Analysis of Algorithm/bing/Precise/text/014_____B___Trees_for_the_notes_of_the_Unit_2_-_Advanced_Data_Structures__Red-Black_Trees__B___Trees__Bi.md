### B – Trees

- B – Trees are a type of self-balancing search tree.
- They are used to store large amounts of data in external storage such as disks.
- B – Trees are multi-way trees, meaning that each node can have more than two children.
- Each node in a B – Tree contains a number of keys and an equal number of pointers to its children.
- The keys in each node are sorted in ascending order.
- The number of keys in each node is limited by a fixed integer t, called the minimum degree of the B – Tree.
- A node can have at most 2t-1 keys and 2t children.
- The root node can have as few as 2 children, but all other nodes must have at least t children.
- B – Trees are height-balanced, meaning that all leaf nodes are at the same level.
- B – Trees are used in databases and file systems to efficiently store and retrieve data.
- Common operations on B – Trees include search, insert, and delete.
- These operations take O(log n) time, where n is the number of keys in the tree.
- B – Trees are able to efficiently handle large amounts of data due to their ability to split and merge nodes as needed during insert and delete operations.
