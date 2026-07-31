# Binary Search Tree

A binary search tree (BST) is a data structure that stores values in a hierarchical order. It has the following properties  :

- A BST is a rooted binary tree, which means it has a single node called the root at the top, and each node has at most two children, called the left child and the right child.
- Each node in a BST has a key (and an optional value) that can be compared with other keys using a total order relation, such as less than, equal to, or greater than.
- The key of any node is greater than all the keys in its left subtree, and less than all the keys in its right subtree. This is called the binary search property, and it allows for efficient search, insertion, and deletion operations.
- A BST can be empty, which means it has no nodes.

Here is an example of a BST with seven nodes:

```
    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13
```

The root node has the key 8, and it has two children: the left child has the key 3, and the right child has the key 10. The node with the key 3 has two children: the left child has the key 1, and the right child has the key 6. The node with the key 10 has one child: the right child has the key 14. The node with the key 6 has two children: the left child has the key 4, and the right child has the key 7. The node with the key 14 has one child: the left child has the key 13. The nodes with the keys 1, 4, 7, and 13 have no children, and they are called the leaf nodes.

The binary search property is satisfied for every node in this BST. For example, the key of the node with the key 6 is greater than the key of its left child (4), and less than the key of its right child (7). The key of the node with the key 10 is greater than all the keys in its left subtree (8, 3, 1, 6, 4, 7), and less than all the keys in its right subtree (14, 13).

A BST can have different shapes depending on the order of insertion and deletion of the nodes. For example, if we insert the nodes with the keys 1, 2, 3, 4, 5, 6, 7 in that order, we get a BST that looks like a linked list:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
```

This BST is called a skewed BST, and it has the worst performance for search, insertion, and deletion operations, because they take linear time in the number of nodes. On the other hand, if we insert the nodes with the keys 4, 2, 6, 1, 3, 5, 7 in that order, we get a BST that looks like a balanced tree:

```
    4
   / \
  2   6
 / \ / \
1  3 5  7
```

This BST is called a balanced BST, and it has the best performance for search, insertion, and deletion operations, because they take logarithmic time in the number of nodes. A balanced BST is also called a height-balanced BST, because the difference between the heights of the left and right subtrees of any node is at most one. The height of a BST is the length of the longest path from the root to a leaf node.

There are different ways to implement a BST, such as using arrays, linked lists, or pointers. The most common way is to use a node class that has three attributes: a key, a value, and two pointers to the left and right children. Here is an example of a node class in Python:

```python
class Node:
  def __init__(self, key, value=None):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
```

To create a BST, we can use a tree class that has a root attribute, and methods for search, insertion, and