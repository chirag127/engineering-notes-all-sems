# Binary tree traversal

Binary tree traversal is a process of visiting each node in a binary tree exactly once in a defined order. A binary tree is a non-linear data structure that consists of nodes, each having at most two children: left child and right child. The topmost node is called the root node, and the nodes with no children are called leaf nodes.

There are three common types of binary tree traversal: inorder, preorder and postorder. Each type of traversal defines a different order of visiting the nodes, based on the following rules:

- Inorder traversal: visit the left subtree, then the root, then the right subtree.
- Preorder traversal: visit the root, then the left subtree, then the right subtree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root.

The following diagram shows an example of a binary tree and its inorder, preorder and postorder traversal.

![Binary tree traversal](https://www.geeksforgeeks.org/wp-content/uploads/2009/06/tree12.gif)

The inorder traversal of the binary tree is: D B E A F C
The preorder traversal of the binary tree is: A B D E C F
The postorder traversal of the binary tree is: D E B F C A

The binary tree traversal can be implemented using recursion or iteration. The recursive approach is simpler and more intuitive, but it may cause stack overflow if the tree is very deep. The iterative approach uses a stack or a queue to store the nodes that need to be visited, and it is more efficient in terms of space and time complexity.

The following pseudocode shows the recursive and iterative implementations of the inorder traversal of a binary tree.

## Recursive inorder traversal

```
procedure inorder(node)
  if node is not null then
    inorder(node.left) // visit the left subtree
    print node.data // visit the root
    inorder(node.right) // visit the right subtree
  end if
end procedure
```

## Iterative inorder traversal

```
procedure inorder(root)
  create an empty stack S
  initialize current node as root
  while current node is not null or stack is not empty do
    while current node is not null do
      push current node to S // store the node for later visit
      current node = current node.left // move to the left child
    end while
    current node = pop from S // retrieve the node from the stack
    print current node.data // visit the node
    current node = current node.right // move to the right child
  end while
end procedure
```