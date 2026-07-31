 Here is the content in Markdown format without any emotions or external links:

### Binary Search Tree

- Binary Search Tree is a node-based binary tree data structure which has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- The left and right subtree each must also be a binary search tree.
- There must be no duplicate nodes.

To insert a new key:

- Compare the new key with the root key. If the new key is lesser, insert it in the left subtree. If the new key is greater, insert it in the right subtree.
- If the subtree is empty, insert the new node there.
- If the subtree is not empty, recur down the appropriate subtree and insert the node in the correct position.

To search a key:

- Compare the search key with the root key. If it matches, return the root node.
- If the search key is lesser, recur down the left subtree. If it is greater, recur down the right subtree.
- If the node is found, return it. If the search terminates without a match, return null.

To delete a key:

- Search for the key to be deleted.
- If the node to be deleted has no children, simply remove it.
- If the node has only one child, replace it with its child.
- If the node has two children, find the minimum element in its right subtree. Replace the data in the node to be deleted with that element. Recursively delete the duplicate node in the right subtree.

This is the study material notes in the requested formal tone without any emotions or external links for the topic Binary Search Tree from Unit 6 - Trees in Discrete Structures & Theory of Logic.