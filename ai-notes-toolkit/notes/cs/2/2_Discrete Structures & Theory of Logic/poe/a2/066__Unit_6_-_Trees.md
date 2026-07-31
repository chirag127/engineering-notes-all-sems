 Here is the formal content written in Markdown format without any emojis or external links inside the header ## Unit 6 - Trees:

## Unit 6 - Trees

1. Tree: A tree is a data structure that emulates a hierarchical tree structure, with a root value and subtrees of children with a parent node, represented as a set of linked nodes.

2. Parts of a Tree:
    - Root: The top node in a tree.
    - Child: A node directly connected to another node when moving away from the root.
    - Parent: The converse notion of a child.
    - Sibling: Nodes with the same parent.
    - Leaf: A node with no children.
    - Edge: The connection between one node and another.

3. Types of Trees:
    - Binary Tree: Each node has at most two children.
    - Binary Search Tree: Nodes are ordered such that left children are less than parent nodes, which are less than right children. This allows for efficient searching.
    - Balanced Binary Search Tree: A binary search tree that is height-balanced, meaning the heights of the two subtrees of any node never differ by more than one. This enables more efficient inserts, deletes, and searches. Examples include red-black trees and AVL trees.

4. Tree Traversals: There are three common ways to traverse a tree:
    - Pre-order: Visit the root, then the left subtree, then the right subtree.
    - In-order: Visit the left subtree, then the root, then the right subtree. Used to visit nodes in sorted order for binary search trees.
    - Post-order: Visit the left subtree, then the right subtree, then the root.

5. Tree Applications: Trees are commonly used to represent hierarchical data and for efficient data storage and retrieval. Example applications include:
    - The DOM in web browsers.
    - File systems.
    - Family trees.
    - Decision trees in machine learning.