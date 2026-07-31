### B – Trees

B – Trees are a type of self-balancing search tree that is commonly used in databases and file systems. They are an extension of binary search trees, where each node can have more than two children. Here are some key points to remember about B – Trees:

1. B – Trees are balanced, meaning that the height of the tree is kept to a minimum to ensure efficient search, insertion, and deletion operations.
2. Each node in a B – Tree can have multiple keys and children. The number of keys in a node is always one less than the number of children.
3. The keys in a node are kept in sorted order.
4. All leaf nodes are at the same level and contain no children.
5. B – Trees are commonly used in databases and file systems because they can efficiently handle large amounts of data.
6. B – Trees can be used to implement multi-level indexing, where the top levels of the tree are kept in memory and the lower levels are stored on disk.
7. B – Trees have a high fan-out, meaning that each node can have many children. This reduces the height of the tree and makes search operations more efficient.
8. B – Trees are designed to work well with disk storage, where reading and writing large blocks of data is more efficient than accessing individual elements.
