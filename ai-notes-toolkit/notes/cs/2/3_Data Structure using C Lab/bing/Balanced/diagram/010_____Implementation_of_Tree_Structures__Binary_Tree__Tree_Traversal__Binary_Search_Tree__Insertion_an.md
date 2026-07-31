### Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A **tree structure** is a hierarchical data structure that consists of nodes and edges. A node is a data element that can have zero or more child nodes. An edge is a link that connects a parent node to a child node. The topmost node is called the root node, and the nodes that have no children are called leaf nodes. A tree structure can be used to represent various kinds of data, such as file systems, XML documents, organizational charts, etc.
- A **binary tree** is a special kind of tree structure where each node can have at most two child nodes, called the left child and the right child. A binary tree can be implemented in C using a struct that contains a data field and two pointers to the left and right child nodes. For example:

```c
struct node {
  int data;
  struct node *left;
  struct node *right;
};
```

- A **tree traversal** is a process of visiting each node in a tree structure in a systematic way. There are three common ways of traversing a binary tree: inorder, preorder, and postorder. In inorder traversal, the left subtree of a node is visited first, then the node itself, and then the right subtree. In preorder traversal, the node is visited first, then the left subtree, and then the right subtree. In postorder traversal, the left subtree is visited first, then the right subtree, and then the node itself. A tree traversal can be implemented in C using recursion or iteration. For example, the following function performs an inorder traversal of a binary tree:

```c
void inorder(struct node *root) {
  if (root != NULL) {
    inorder(root->left); // visit left subtree
    printf("%d ", root->data); // visit node
    inorder(root->right); // visit right subtree
  }
}
```

- A **binary search tree (BST)** is a special kind of binary tree that satisfies the following property: the value of a node is greater than or equal to the values of all the nodes in its left subtree, and less than or equal to the values of all the nodes in its right subtree. A BST can be used to store and search data efficiently, as the average time complexity of searching, inserting, and deleting a node in a BST is O(log n), where n is the number of nodes in the tree.
- **Insertion** in a BST is the operation of adding a new node to the tree while maintaining the BST property. The insertion algorithm starts from the root node and compares the value of the new node with the value of the current node. If the value of the new node is less than or equal to the value of the current node, the algorithm moves to the left child of the current node. If the value of the new node is greater than the value of the current node, the algorithm moves to the right child of the current node. This process is repeated until a NULL pointer is reached, which means that the new node can be inserted at that position. The insertion algorithm can be implemented in C using recursion or iteration. For example, the following function inserts a new node to a BST using recursion:

```c
struct node *insert(struct node *root, int data) {
  if (root == NULL) { // base case: create a new node
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
  }
  else { // recursive case: traverse the tree
    if (data <= root->data) { // insert to the left subtree
      root->left = insert(root->left, data);
    }
    else { // insert to the right subtree
      root->right = insert(root->right, data);
    }
    return root;
  }
}
```

- **Deletion** in a BST is the operation of removing a node from the tree while maintaining the BST property. The deletion algorithm has three cases, depending on the number of children of the node to be deleted. If the node has no children, it can be simply deleted and the parent node's pointer can be set to NULL. If the node has one child, it can be replaced by its child and the child node can be deleted. If the node has two children, it