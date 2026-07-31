# Binary tree traversal

- A binary tree is a non-linear data structure that stores data in the form of nodes, and nodes are connected to each other with the help of edges.
- A node has at most two children, called the left child and the right child.
- The root node is the main node of the binary tree, and all other nodes are the descendants of the root node.
- Binary tree traversal is the process of visiting each node in the binary tree exactly once in a specific order.
- There are three common types of binary tree traversal: inorder, preorder, and postorder.

## Inorder traversal

- Inorder traversal is a type of binary tree traversal that visits the left subtree, the root, and the right subtree in that order.
- Inorder traversal gives the nodes in non-decreasing order if the binary tree is a binary search tree.
- Inorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for inorder traversal is:

```
inorder(root)
  if root is not null
    inorder(root.left) // visit left subtree
    print(root.data) // visit root
    inorder(root.right) // visit right subtree
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

- Preorder traversal is a type of binary tree traversal that visits the root, the left subtree, and the right subtree in that order.
- Preorder traversal can be used to create a copy of the binary tree or to print the prefix expression of an expression tree.
- Preorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for preorder traversal is:

```
preorder(root)
  if root is not null
    print(root.data) // visit root
    preorder(root.left) // visit left subtree
    preorder(root.right) // visit right subtree
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

- Postorder traversal is a type of binary tree traversal that visits the left subtree, the right subtree, and the root in that order.
- Postorder traversal can be used to delete the binary tree or to print the postfix expression of an expression tree.
- Postorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for postorder traversal is:

```
postorder(root)
  if root is not null
    postorder(root.left) // visit left subtree
    postorder(root.right) // visit right subtree
    print(root.data) // visit root
```

- The postorder traversal of the following binary tree is: 4 5 2 3 1

```
    1
   / \
  2   3
 / \
4   5
```

## References

: Binary Tree Traversal in Data Structure - javatpoint
: Vertical Order Traversal of a Binary Tree in Java
: Binary Tree | Traversal - GeeksforGeeks
: Tree Traversals (Inorder, Preorder and Postorder) - GeeksforGeeks
: Binary Search Tree (BST) Traversals – Inorder, Preorder, Post Order