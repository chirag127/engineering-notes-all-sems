 Here is the content in markdown format for the topic ### Red-Black Trees for the notes of the Unit 2 - Advanced Data Structures:

### Red-Black Trees

Red-Black Trees are self-balancing Binary Search Trees (BSTs) with following properties:

1. Every node is either red or black.
2. The root is always black.
3. Every red node must have two black child nodes.
4. Every path from a node (including root) to any of its descendant NIL nodes contains the same number of black nodes.

Advantages:

- Guaranteed O(log n) time for insertion, deletion and search operations as Red-Black trees are height balanced BSTs.
- Keep tree balance while inserting and deleting nodes, thus avoiding degeneration into linear list which can happen with basic BST implementation.

### Properties and rotations:

To ensure properties 3 and 4, Red-Black trees use color flipping and rotations. There are two types of rotations:

1. Left rotation: Right child of the root is moved up and the root is made the right child of its right child.
2. Right rotation: Left child of the root is moved up and the root is made the left child of its left child.

Rotations occur on the insertion of a new red node that violates properties. After rotations, the properties are ensured and the tree remains height balanced.

### Insertion:

1. Insert the new node as in BST and color it red.
2. If the parent is red, perform rotations and recolor nodes to resolve violations.
3. If the new node is the root, color it black.

### Deletion:

1. Delete the node as in BST.
2. Perform rotations and recolor nodes to resolve any violations due to deletion and maintain properties.

Applications: Red-Black trees are typically used to implement associative arrays (maps) as they support fast search, insert and delete operations with guaranteed logarithmic time complexity. They are thus commonly used in database systems and programming language implementations.