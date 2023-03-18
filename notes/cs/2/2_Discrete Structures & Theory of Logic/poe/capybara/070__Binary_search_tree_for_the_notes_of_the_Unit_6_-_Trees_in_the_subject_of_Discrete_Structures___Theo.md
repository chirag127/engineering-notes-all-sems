### Binary Search Tree

A binary search tree (BST) is a type of tree data structure. It is a binary tree where the left subtree contains only nodes with keys less than the root node and the right subtree contains only nodes with keys greater than the root node. 

#### Properties of a Binary Search Tree

- Each node in a BST has at most two children.
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- The left and right subtree each must also be a binary search tree.
- There are no duplicate nodes.

#### Searching in a Binary Search Tree

To search for a value in a binary search tree, we start at the root node and compare the value we are searching for with the value of the current node. If the value is less than the current node's value, we move to the left subtree. If the value is greater than the current node's value, we move to the right subtree. We continue this process until we find the node with the desired value, or we reach a null node indicating that the value is not in the tree.

#### Insertion in a Binary Search Tree

To insert a value in a binary search tree, we start at the root node and compare the value we want to insert with the value of the current node. If the value is less than the current node's value, we move to the left subtree. If the value is greater than the current node's value, we move to the right subtree. We continue this process until we reach a null node, indicating that we have found the correct place to insert the new node.

#### Deletion in a Binary Search Tree

To delete a node from a binary search tree, there are three cases to consider:

- The node has no children: We simply remove the node from the tree.
- The node has one child: We replace the node with its child.
- The node has two children: We find the node's successor (i.e., the smallest node in the right subtree) and replace the node with its successor. We then delete the successor from the tree.

#### Time Complexity of Binary Search Tree Operations

- Searching: O(log n) in the average case, O(n) in the worst case (when the tree is skewed).
- Insertion: O(log n) in the average case, O(n) in the worst case (when the tree is skewed).
- Deletion: O(log n) in the average case, O(n) in the worst case (when the tree is skewed).

#### Applications of Binary Search Trees

- Binary search trees are used in many search algorithms and data structures, such as binary heaps and AVL trees.
- They are also used in many computer science applications, such as compilers, databases, and file systems.
- Binary search trees can be used to implement various operations, such as searching, inserting, and deleting data, in an efficient manner.