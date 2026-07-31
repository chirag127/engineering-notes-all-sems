# Binary Search Tree

A binary search tree (BST) is a special type of binary tree that satisfies the following properties:

- The value of the key of the left sub-tree is less than the value of its parent (root) node's key.
- The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.
- The left and right sub-trees are also binary search trees.

A binary search tree can perform three basic operations: searching, insertion, and deletion.

- Searching in a BST: The search operation finds whether or not a particular value exists in a tree. Since the BST is ordered, the search can be easily made by comparing the value with the root node and then recursively searching in the left or right sub-tree depending on the comparison result. The search operation takes O(h) time, where h is the height of the tree.
- Insertion in a BST: The insertion operation adds a new node with a given value to the tree. To insert a new node, we start from the root and compare the value with the root node. If the value is less than the root node, we go to the left sub-tree. If the value is greater than or equal to the root node, we go to the right sub-tree. We repeat this process until we find an empty spot where we can insert the new node. The insertion operation takes O(h) time, where h is the height of the tree.
- Deletion in a BST: The deletion operation removes a node with a given value from the tree. To delete a node, we first search for the node in the tree. If the node is not found, we do nothing. If the node is found, we have three cases to consider:

  - Case 1: The node has no children. In this case, we simply delete the node and free the memory.
  - Case 2: The node has one child. In this case, we copy the child to the node and delete the child.
  - Case 3: The node has two children. In this case, we find the minimum value in the right sub-tree of the node (or the maximum value in the left sub-tree) and copy it to the node. Then we delete the minimum value node from the right sub-tree (or the maximum value node from the left sub-tree).

The deletion operation takes O(h) time, where h is the height of the tree.

The following is an example of a binary search tree:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

The following is a pseudocode for the search, insertion, and deletion operations in a BST:

```
// Search for a value in a BST
function search(root, value)
  if root is null
    return false
  else if root.key == value
    return true
  else if value < root.key
    return search(root.left, value)
  else
    return search(root.right, value)

// Insert a value in a BST
function insert(root, value)
  if root is null
    create a new node with value as key and assign it to root
  else if value < root.key
    insert(root.left, value)
  else
    insert(root.right, value)

// Delete a value in a BST
function delete(root, value)
  if root is null
    return null
  else if value < root.key
    root.left = delete(root.left, value)
  else if value > root.key
    root.right = delete(root.right, value)
  else // root.key == value
    if root has no children
      free root and return null
    else if root has one child
      copy root's child to root and free root's child
      return root
    else // root has two children
      find the minimum value node in root's right sub-tree and assign it to minNode
      copy minNode.key to root.key
      root.right = delete(root.right, minNode.key)
      return root
```