### Binary tree traversal

Binary tree traversal is a process of visiting each node in a binary tree exactly once in a predefined order. A binary tree is a non-linear data structure that consists of nodes connected by edges. Each node has at most two children, called the left child and the right child. The node without any child is called a leaf node. The node at the top of the tree is called the root node.

There are three common types of binary tree traversal: inorder, preorder and postorder. Each type of traversal defines a different order of visiting the nodes. The order of traversal can be represented by a recursive algorithm or an iterative algorithm using a stack.

#### Inorder traversal

Inorder traversal visits the nodes in the following order:

- Traverse the left subtree in inorder
- Visit the root node
- Traverse the right subtree in inorder

Inorder traversal is useful for binary search trees, as it gives the nodes in sorted order. For example, the inorder traversal of the following binary tree is 4, 2, 5, 1, 3.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for inorder traversal is:

```
void inorder(node *root) {
  if (root == NULL) return; // base case
  inorder(root->left); // traverse left subtree
  print(root->data); // visit root node
  inorder(root->right); // traverse right subtree
}
```

The iterative algorithm for inorder traversal using a stack is:

```
void inorder(node *root) {
  stack<node*> s; // create an empty stack
  node *current = root; // start from the root node
  while (current != NULL || !s.empty()) { // while there are nodes to visit
    while (current != NULL) { // while the current node is not null
      s.push(current); // push the current node to the stack
      current = current->left; // move to the left child
    }
    current = s.top(); // pop the top node from the stack
    s.pop();
    print(current->data); // visit the node
    current = current->right; // move to the right child
  }
}
```

#### Preorder traversal

Preorder traversal visits the nodes in the following order:

- Visit the root node
- Traverse the left subtree in preorder
- Traverse the right subtree in preorder

Preorder traversal is useful for creating a copy of the tree or printing the tree structure. For example, the preorder traversal of the following binary tree is 1, 2, 4, 5, 3.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for preorder traversal is:

```
void preorder(node *root) {
  if (root == NULL) return; // base case
  print(root->data); // visit root node
  preorder(root->left); // traverse left subtree
  preorder(root->right); // traverse right subtree
}
```

The iterative algorithm for preorder traversal using a stack is:

```
void preorder(node *root) {
  stack<node*> s; // create an empty stack
  s.push(root); // push the root node to the stack
  while (!s.empty()) { // while the stack is not empty
    node *current = s.top(); // pop the top node from the stack
    s.pop();
    print(current->data); // visit the node
    if (current->right != NULL) s.push(current->right); // push the right child to the stack if not null
    if (current->left != NULL) s.push(current->left); // push the left child to the stack if not null
  }
}
```

#### Postorder traversal

Postorder traversal visits the nodes in the following order:

- Traverse the left subtree in postorder
- Traverse the right subtree in postorder
- Visit the root node

Postorder traversal is useful for deleting the tree or evaluating an expression tree. For example, the postorder traversal of the following binary tree is 4, 5, 2, 3, 1.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for postorder traversal is:

```
void postorder(node *root) {
  if (root == NULL) return; // base case
  postorder(root->left); //

```
