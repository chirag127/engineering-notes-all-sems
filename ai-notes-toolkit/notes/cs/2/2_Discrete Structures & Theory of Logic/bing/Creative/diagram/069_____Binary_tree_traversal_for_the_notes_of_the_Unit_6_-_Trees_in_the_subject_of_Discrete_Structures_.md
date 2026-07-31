### Binary tree traversal

Binary tree traversal is the process of visiting each node in a binary tree in a systematic way. There are three common types of binary tree traversal: inorder, preorder and postorder. Each type of traversal defines a different order of visiting the root, left subtree and right subtree of each node.

- Inorder traversal: visit the left subtree, then the root, then the right subtree. This traversal gives the nodes in sorted order for a binary search tree. For example, the inorder traversal of the following binary tree is 4, 2, 5, 1, 3.

```
    1
   / \
  2   3
 / \
4   5
```

- Preorder traversal: visit the root, then the left subtree, then the right subtree. This traversal can be used to create a copy of the binary tree or to print a prefix expression of an arithmetic expression tree. For example, the preorder traversal of the following binary tree is 1, 2, 4, 5, 3.

```
    1
   / \
  2   3
 / \
4   5
```

- Postorder traversal: visit the left subtree, then the right subtree, then the root. This traversal can be used to delete the binary tree or to print a postfix expression of an arithmetic expression tree. For example, the postorder traversal of the following binary tree is 4, 5, 2, 3, 1.

```
    1
   / \
  2   3
 / \
4   5
```

There are two ways to implement binary tree traversal: recursively or iteratively. The recursive approach is simpler and more intuitive, but it may cause stack overflow for large trees. The iterative approach uses a stack or a queue to store the nodes to be visited, and it is more efficient in terms of space and time complexity.

The pseudocode for the recursive approach is:

```
inorder(node):
  if node is not null:
    inorder(node.left)
    print node.data
    inorder(node.right)

preorder(node):
  if node is not null:
    print node.data
    preorder(node.left)
    preorder(node.right)

postorder(node):
  if node is not null:
    postorder(node.left)
    postorder(node.right)
    print node.data
```

The pseudocode for the iterative approach using a stack is:

```
inorder(node):
  create an empty stack S
  while node is not null or S is not empty:
    while node is not null:
      push node to S
      node = node.left
    node = pop from S
    print node.data
    node = node.right

preorder(node):
  create an empty stack S
  push node to S
  while S is not empty:
    node = pop from S
    print node.data
    if node.right is not null:
      push node.right to S
    if node.left is not null:
      push node.left to S

postorder(node):
  create an empty stack S
  create another empty stack O
  push node to S
  while S is not empty:
    node = pop from S
    push node to O
    if node.left is not null:
      push node.left to S
    if node.right is not null:
      push node.right to S
  while O is not empty:
    node = pop from O
    print node.data
```

The pseudocode for the iterative approach using a queue is:

```
levelorder(node):
  create an empty queue Q
  enqueue node to Q
  while Q is not empty:
    node = dequeue from Q
    print node.data
    if node.left is not null:
      enqueue node.left to Q
    if node.right is not null:
      enqueue node.right to Q
```

The levelorder traversal is also known as the breadth-first traversal, as it visits the nodes in each level from left to right. This traversal can be used to find the height of the binary tree or to print the nodes in a zigzag pattern. For example, the levelorder traversal of the following binary tree is 1, 2, 3, 4, 5.

```
    1
   / \
  2   3
 / \
4   5
```