# Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Tree Structures
- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has a root node, which is the topmost node in the hierarchy.
- A node can have zero or more child nodes, which are nodes that are directly connected to it by an edge.
- A node that has no child nodes is called a leaf node.
- A node that has at least one child node is called an internal node.
- A path is a sequence of nodes and edges from one node to another node in the tree.
- The length of a path is the number of edges in the path.
- The depth of a node is the length of the path from the root node to that node.
- The height of a node is the length of the longest path from that node to a leaf node.
- The height of a tree is the height of the root node.

## Binary Tree
- A binary tree is a special kind of tree in which each node can have at most two child nodes, called the left child and the right child.
- A binary tree can be empty, which means it has no nodes.
- A binary tree can be represented using an array or a linked list.
- In an array representation, the root node is stored at index 0, and the left child and the right child of a node at index i are stored at index 2i+1 and 2i+2, respectively.
- In a linked list representation, each node has a data field and two pointer fields, one for the left child and one for the right child.
- A binary tree can be implemented in C using a struct data type, as shown below:

```c
// Define a node structure
struct node {
  int data; // Data field
  struct node *left; // Pointer to left child
  struct node *right; // Pointer to right child
};

// Create a new node with given data and NULL children
struct node* createNode(int data) {
  struct node* newNode = (struct node*)malloc(sizeof(struct node)); // Allocate memory
  newNode->data = data; // Assign data
  newNode->left = NULL; // Initialize left child as NULL
  newNode->right = NULL; // Initialize right child as NULL
  return newNode; // Return the new node
}
```

## Tree Traversal
- Tree traversal is the process of visiting each node in a tree in a specific order.
- There are three common ways of traversing a binary tree: inorder, preorder, and postorder.
- Inorder traversal: visit the left subtree, then the root, then the right subtree.
- Preorder traversal: visit the root, then the left subtree, then the right subtree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root.
- Tree traversal can be implemented using recursion or iteration.
- A recursive implementation of inorder traversal in C is shown below:

```c
// Recursive function to perform inorder traversal of a binary tree
void inorder(struct node* root) {
  if (root == NULL) return; // Base case: empty tree
  inorder(root->left); // Recursively traverse the left subtree
  printf("%d ", root->data); // Print the root data
  inorder(root->right); // Recursively traverse the right subtree
}
```

## Binary Search Tree
- A binary search tree (BST) is a special kind of binary tree that satisfies the following property: for any node in the tree, the values of all the nodes in its left subtree are smaller than its value, and the values of all the nodes in its right subtree are greater than its value.
- A BST can be used to store and search data efficiently, as the average time complexity of searching, inserting, and deleting a node in a BST is O(log n), where n is the number of nodes in the tree.
- A BST can be implemented using the same node structure and createNode function as a binary tree, as shown above.
- To search for a node with a given value in a BST, we can use the following algorithm:
  - Start from the root node.
  - If the root node is NULL, or its value is equal to the given value, return the root node.
  - If the given value is smaller than the root node's value, recursively search in the left subtree.
  -