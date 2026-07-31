# Binary tree traversal

- A binary tree is a non-linear data structure that stores data in the form of nodes, and nodes are connected to each other with the help of edges.
- A node has at most two children, called the left child and the right child.
- The root node is the main node of the binary tree, and all other nodes are the descendants of the root node.
- Traversal is the process of visiting each node in the binary tree exactly once in a specific order.
- There are three common types of traversal: inorder, preorder, and postorder.

## Inorder traversal

- Inorder traversal is a recursive algorithm that follows the left-root-right order.
- That is, it first visits the left subtree, then the root node, and then the right subtree.
- Inorder traversal is useful for binary search trees, as it gives the nodes in sorted order.
- The pseudocode for inorder traversal is:

```
inorder(node)
  if node is not null
    inorder(node.left) // visit left subtree
    print node.data // visit root node
    inorder(node.right) // visit right subtree
```

- The inorder traversal of the following binary tree is: 4 2 5 1 3

```
    1
   / \
  2   3
 / \
4   5
```

## Preorder traversal

- Preorder traversal is a recursive algorithm that follows the root-left-right order.
- That is, it first visits the root node, then the left subtree, and then the right subtree.
- Preorder traversal is useful for creating a copy of the binary tree, as it preserves the structure of the tree.
- The pseudocode for preorder traversal is:

```
preorder(node)
  if node is not null
    print node.data // visit root node
    preorder(node.left) // visit left subtree
    preorder(node.right) // visit right subtree
```

- The preorder traversal of the following binary tree is: 1 2 4 5 3

```
    1
   / \
  2   3
 / \
4   5
```

## Postorder traversal

- Postorder traversal is a recursive algorithm that follows the left-right-root order.
- That is, it first visits the left subtree, then the right subtree, and then the root node.
- Postorder traversal is useful for deleting the binary tree, as it deletes the nodes from the bottom up.
- The pseudocode for postorder traversal is:

```
postorder(node)
  if node is not null
    postorder(node.left) // visit left subtree
    postorder(node.right) // visit right subtree
    print node.data // visit root node
```

- The postorder traversal of the following binary tree is: 4 5 2 3 1

```
    1
   / \
  2   3
 / \
4   5
```

: https://www.javatpoint.com/binary-tree-traversal-in-data-structure
: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/