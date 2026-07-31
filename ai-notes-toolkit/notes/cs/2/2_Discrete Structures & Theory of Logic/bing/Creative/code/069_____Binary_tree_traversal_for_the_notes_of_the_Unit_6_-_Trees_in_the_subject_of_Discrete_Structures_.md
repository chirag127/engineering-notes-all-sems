### Binary tree traversal

Binary tree traversal is the process of visiting each node in a binary tree in a systematic way. A binary tree is a data structure that consists of nodes that have at most two children: a left child and a right child. The topmost node is called the root, and the nodes with no children are called leaves.

There are three common types of binary tree traversal: inorder, preorder, and postorder. Each type of traversal defines a different order of visiting the nodes, based on the relative positions of the root, the left child, and the right child.

- Inorder traversal: visit the left subtree, then the root, then the right subtree. This traversal gives the nodes in sorted order if the binary tree is a binary search tree (BST).
- Preorder traversal: visit the root, then the left subtree, then the right subtree. This traversal is useful for copying or cloning a binary tree, or for creating a prefix expression of an arithmetic expression tree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root. This traversal is useful for deleting a binary tree, or for evaluating a postfix expression of an arithmetic expression tree.

The following diagram shows an example of a binary tree and its inorder, preorder, and postorder traversals.

![Binary tree and its traversals](https://www.geeksforgeeks.org/wp-content/uploads/2009/06/tree12.gif)

Inorder traversal: 4, 2, 5, 1, 3
Preorder traversal: 1, 2, 4, 5, 3
Postorder traversal: 4, 5, 2, 3, 1

To implement binary tree traversal, we can use either recursion or iteration. Recursion is a natural way to express the traversal, as each subtree is a smaller binary tree that can be traversed in the same way. Iteration is more efficient in terms of space and time, as it avoids the overhead of function calls and stack frames. Iteration requires the use of a stack or a queue to store the nodes that need to be visited.

The following pseudocode shows the recursive and iterative implementations of inorder traversal.

```python
# Recursive inorder traversal
def inorder(root):
  if root is not None:
    inorder(root.left) # visit left subtree
    print(root.data) # visit root
    inorder(root.right) # visit right subtree

# Iterative inorder traversal
def inorder(root):
  stack = [] # create an empty stack
  current = root # start from the root
  while True:
    if current is not None:
      stack.push(current) # push the current node to the stack
      current = current.left # move to the left child
    elif stack is not empty:
      current = stack.pop() # pop the top node from the stack
      print(current.data) # visit the node
      current = current.right # move to the right child
    else:
      break # the stack is empty and the current node is None, traversal is done
```

The recursive and iterative implementations of preorder and postorder traversal are similar, with slight modifications in the order of visiting the nodes and pushing or popping them to the stack.