

Hello, I am Sydney, your AI assistant. I can help you with writing C programs to illustrate the concept of the following:

- Variables and data types
- Operators and expressions
- Control structures
- Arrays and strings
- Functions and recursion
- Pointers and dynamic memory allocation
- Structures and unions
- File handling and input/output

Please choose one of the topics to start.



# Sorting Algorithms-Non-Recursive

Sorting algorithms are methods of arranging a collection of items in a certain order, such as ascending or descending. Non-recursive sorting algorithms are those that do not use recursion, which is a technique of calling a function within itself to solve smaller subproblems. Non-recursive sorting algorithms typically use loops, such as for or while, to iterate over the elements and compare and swap them as needed.

Some examples of non-recursive sorting algorithms are:

- **Selection sort**: This algorithm finds the smallest element in the unsorted part of the array and swaps it with the first element of the unsorted part, then repeats the process until the whole array is sorted. It has a time complexity of O(n^2), where n is the number of elements in the array.
- **Bubble sort**: This algorithm compares adjacent elements in the array and swaps them if they are in the wrong order, then repeats the process until no swaps are needed. It has a time complexity of O(n^2) in the worst case, but can be improved by using a flag to indicate if any swaps were made in the current pass, or by skipping the already sorted part of the array.
- **Insertion sort**: This algorithm iterates over the array and inserts each element into its correct position in the sorted part of the array, shifting the larger elements to the right. It has a time complexity of O(n^2) in the worst case, but can perform well on nearly sorted arrays or small arrays.
- **Merge sort**: This algorithm divides the array into two halves, sorts each half recursively, and then merges the two sorted halves into one sorted array. It has a time complexity of O(n log n), where n is the number of elements in the array, and a space complexity of O(n), as it requires an auxiliary array to store the merged result. To make it non-recursive, one can use a bottom-up approach, where the array is divided into subarrays of size 1, then merged into subarrays of size 2, then 4, and so on, until the whole array is sorted.
- **Quick sort**: This algorithm chooses a pivot element from the array, partitions the array into two subarrays such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray, then sorts each subarray recursively. It has a time complexity of O(n log n) on average, but can degrade to O(n^2) in the worst case, depending on the choice of the pivot. To make it non-recursive, one can use a stack to store the subarray boundaries and pop them when needed.



# Sorting Algorithms-Recursive

Sorting algorithms are methods of arranging a set of data elements in a specific order, such as ascending or descending. Recursive sorting algorithms are those that use recursion, a technique of breaking down a problem into smaller subproblems that can be solved by calling the same function repeatedly.

Some examples of recursive sorting algorithms are:

- **Merge sort**: This algorithm divides the array into two halves, sorts each half recursively, and then merges the two sorted halves into one sorted array. The merge operation is done by comparing the first elements of each half and placing the smaller one in the output array, and repeating this until one of the halves is exhausted. The time complexity of merge sort is O(n log n) in the average and worst cases, and the space complexity is O(n) for the auxiliary array used for merging.

- **Quick sort**: This algorithm chooses a pivot element from the array, partitions the array into two subarrays such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray, and then sorts each subarray recursively. The choice of the pivot element can affect the performance of quick sort, as the best case occurs when the pivot is the median of the array, resulting in a balanced partition. The worst case occurs when the pivot is the smallest or the largest element of the array, resulting in an unbalanced partition. The average time complexity of quick sort is O(n log n), and the worst case time complexity is O(n^2). The space complexity is O(log n) for the stack space used for recursion.

- **Heap sort**: This algorithm builds a max-heap (a binary tree where the parent node is always larger than its children) from the array, and then repeatedly swaps the root element (the largest element) with the last element of the heap, reduces the size of the heap by one, and restores the heap property by calling a recursive function called heapify. The heapify function takes an index of a node and compares it with its children, and swaps it with the larger child if the node is smaller than the child, and repeats this process until the node is larger than both of its children or it reaches a leaf node. The time complexity of heap sort is O(n log n) in the average and worst cases, and the space complexity is O(1) as it does not use any extra space.

- **Insertion sort**: This algorithm iterates over the array from the second element, and for each element, it compares it with the previous elements in the sorted part of the array, and shifts them to the right until it finds the correct position for the element, and inserts it there. This can be done recursively by sorting the first n-1 elements of the array, and then inserting the last element in its correct position. The time complexity of insertion sort is O(n^2) in the average and worst cases, and O(n) in the best case when the array is already sorted. The space complexity is O(1) as it does not use any extra space.



# Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding an element or retrieving an element from any data structure where it is stored.
- There are different types of searching algorithms, such as linear search, binary search, interpolation search, etc.
- The choice of the searching algorithm depends on the data structure, the size of the data, the sorting order of the data, and the complexity of the algorithm.
- In this note, we will focus on two basic searching algorithms: linear search and binary search.

## Linear Search
- Linear search is a simple and brute-force method of searching for an element in an array or a list .
- It works by traversing the array or list sequentially and comparing every element with the target value until a match is found or the end of the array or list is reached.
- The algorithm for linear search is as follows:

```
linear_search(array, size, target)
  for i = 0 to size - 1
    if array[i] == target
      return i // element found at index i
  return -1 // element not found
```

- The time complexity of linear search is O(n), where n is the number of elements in the array or list.
- The space complexity of linear search is O(1), as it does not require any extra space.
- Linear search is suitable for small and unsorted data sets, as it does not require any prior sorting or ordering of the data.

## Binary Search
- Binary search is a more efficient and faster method of searching for an element in a sorted array or list .
- It works by repeatedly dividing the array or list into two halves and checking if the target value is in the left half or the right half.
- The algorithm for binary search is as follows:

```
binary_search(array, low, high, target)
  while low <= high
    mid = (low + high) / 2 // find the middle index
    if array[mid] == target
      return mid // element found at index mid
    else if array[mid] < target
      low = mid + 1 // search in the right half
    else
      high = mid - 1 // search in the left half
  return -1 // element not found
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array or list.
- The space complexity of binary search is O(1), as it does not require any extra space.
- Binary search is suitable for large and sorted data sets, as it reduces the search space by half in each iteration.



# Implementation of Stack using Array

- A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
- This means that the element that is inserted last will be removed first.
- A stack can be implemented using an array or a linked list.
- In this topic, we will see how to implement a stack using an array in C language.
- To implement a stack using an array, we need to declare an array of a fixed size, a variable to store the top index of the stack, and some functions to perform the operations on the stack.
- The top index of the stack is initially set to -1, indicating that the stack is empty.
- The functions that we need to implement are:

  - push(): This function takes an element as a parameter and inserts it into the stack. It also increments the top index by one. If the stack is full, it prints an error message and returns.
  - pop(): This function removes and returns the element at the top of the stack. It also decrements the top index by one. If the stack is empty, it prints an error message and returns.
  - peek(): This function returns the element at the top of the stack without removing it. If the stack is empty, it prints an error message and returns.
  - isEmpty(): This function returns true if the stack is empty, and false otherwise.
  - isFull(): This function returns true if the stack is full, and false otherwise.
  - display(): This function prints all the elements of the stack from top to bottom.

- The following is the C code for implementing a stack using an array:

```c
#include <stdio.h>
#define MAX 10 // Define the maximum size of the stack

int stack[MAX]; // Declare an array of size MAX to store the stack elements
int top = -1; // Declare a variable to store the top index of the stack

// Function to insert an element into the stack
void push(int x)
{
  if (isFull()) // Check if the stack is full
  {
    printf("Stack overflow\n"); // Print an error message
    return; // Return from the function
  }
  top++; // Increment the top index by one
  stack[top] = x; // Store the element at the top of the stack
  printf("Pushed %d into the stack\n", x); // Print a success message
}

// Function to remove and return an element from the stack
int pop()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack underflow\n"); // Print an error message
    return -1; // Return an invalid value
  }
  int x = stack[top]; // Store the element at the top of the stack
  top--; // Decrement the top index by one
  printf("Popped %d from the stack\n", x); // Print a success message
  return x; // Return the element
}

// Function to return the element at the top of the stack
int peek()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack is empty\n"); // Print an error message
    return -1; // Return an invalid value
  }
  int x = stack[top]; // Store the element at the top of the stack
  printf("The top element is %d\n", x); // Print the element
  return x; // Return the element
}

// Function to check if the stack is empty
int isEmpty()
{
  if (top == -1) // Check if the top index is -1
  {
    return 1; // Return true
  }
  else
  {
    return 0; // Return false
  }
}

// Function to check if the stack is full
int isFull()
{
  if (top == MAX - 1) // Check if the top index is MAX - 1
  {
    return 1; // Return true
  }
  else
  {
    return 0; // Return false
  }
}

// Function to display the stack elements
void display()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack is empty\n"); // Print an error message
    return; // Return from the function
  }
  printf("The stack elements are:\n"); // Print a message
  for (int i = top; i >= 0; i--) // Loop from the top index to the bottom index
  {
    printf("%d\n", stack[i]); // Print the element at the current index
  }
}

// Main function to test the stack implementation

```




# Implementation of Queue using Array

A queue is a linear data structure that follows the **First In First Out (FIFO)** principle. It means that the element that is inserted first in the queue is the one that is removed first. A queue can be implemented using an array, but it has some limitations and disadvantages. Here are some points to note about queue using array:

- A queue using array has a fixed size that is declared at the compile time. It cannot be changed at the run time. Therefore, the size of the queue must be known beforehand and it cannot grow or shrink dynamically.
- A queue using array has two variables: **front** and **rear**. The front variable points to the index of the first element in the queue, and the rear variable points to the index of the last element in the queue. Initially, both front and rear are set to -1, indicating that the queue is empty.
- To insert an element in the queue, we increment the rear variable by one and store the element at the rear index of the array. This operation is called **enqueue**. To remove an element from the queue, we return the element at the front index of the array and increment the front variable by one. This operation is called **dequeue**.
- A queue using array can become **full** when the rear variable reaches the last index of the array. In that case, no more elements can be inserted in the queue. Similarly, a queue using array can become **empty** when the front variable becomes greater than the rear variable. In that case, no more elements can be removed from the queue.
- A queue using array can suffer from the problem of **wasted space**. When some elements are dequeued from the front of the queue, the space they occupied in the array becomes unused. However, the rear variable cannot move back to fill the space, as it would violate the FIFO order. Therefore, the queue using array cannot utilize the array efficiently and may run out of space even when there are empty slots in the array.
- A possible solution to the problem of wasted space is to use a **circular queue**. A circular queue is a queue using array that treats the array as a circular buffer. It means that when the rear variable reaches the last index of the array, it wraps around to the first index of the array, and vice versa. This way, the queue can use the array space more efficiently and avoid overflow or underflow. However, a circular queue also has a fixed size and requires some extra logic to check if the queue is full or empty.



# Implementation of Circular Queue using Array

A circular queue is a type of queue data structure that uses an array to store the elements. A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the element that is inserted first is removed first. A circular queue overcomes the limitation of a normal queue, which is the wastage of space due to the empty slots that are left behind after some insertions and deletions.

To implement a circular queue using an array, we need to follow these steps:

- Initialize an array of size n, where n is the maximum number of elements that the queue can hold. This array will be used to store the elements of the queue.
- Initialize two variables front and rear to -1. These variables will keep track of the index of the first and the last element of the queue, respectively.
- To enqueue (insert) an element x onto the queue, do the following:
  - Increment rear by 1. If rear is equal to n, set rear to 0. This ensures that the rear index wraps around the array when it reaches the end.
  - If front is -1, set front to 0. This means that the queue was empty before the insertion, and now it has one element.
  - If front is equal to rear, then the queue is full and the insertion cannot be done. Display an overflow message and return.
  - Otherwise, store x at the rear index of the array.
- To dequeue (remove) an element from the queue, do the following:
  - If front is -1, then the queue is empty and the deletion cannot be done. Display an underflow message and return.
  - Otherwise, store the element at the front index of the array in a variable and return it.
  - Increment front by 1. If front is equal to n, set front to 0. This ensures that the front index wraps around the array when it reaches the end.
  - If front is equal to rear + 1, then the queue is empty after the deletion, and set both front and rear to -1. This resets the queue to its initial state.

Here is an example of a circular queue using an array in C:

```c
#include <stdio.h>
#define MAX 5 // maximum size of the queue

int cqueue_arr[MAX]; // array to store the elements of the queue
int front = -1; // index of the first element of the queue
int rear = -1; // index of the last element of the queue

void insert(int item); // function to enqueue an element
int del(); // function to dequeue an element
void display(); // function to display the elements of the queue

int main()
{
    int choice, item; // variables to store the user input
    while (1) // loop until the user exits
    {
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice); // read the user choice
        switch (choice) // perform the corresponding operation
        {
        case 1:
            printf("Enter the element to be inserted: ");
            scanf("%d", &item); // read the element to be inserted
            insert(item); // call the insert function
            break;
        case 2:
            item = del(); // call the delete function and store the returned element
            if (item != -1) // if the element is valid, display it
                printf("The deleted element is: %d\n", item);
            break;
        case 3:
            display(); // call the display function
            break;
        case 4:
            exit(1); // exit the program
        default:
            printf("Invalid choice\n"); // display an error message for invalid choice
        }
    }
    return 0;
}

void insert(int item)
{
    if ((front == 0 && rear == MAX - 1) || (front == rear + 1)) // check if the queue is full
    {
        printf("Queue Overflow\n"); // display an overflow message
        return;
    }
    if (front == -1) // check if the queue is empty
        front = 0; // set front to 0
    if (rear == MAX - 1) // check if rear is at the end of the array
        rear = 0; // wrap around rear to 0

```




# Implementation of Stack using Linked List

- A stack is a linear data structure that follows the **LIFO (Last In First Out)** principle, meaning that the last element inserted into the stack is the first one to be removed.
- A stack supports various operations like **push**, **pop**, **peek**, **empty**, and **size**.
- A stack can be implemented using an array or a linked list. The benefit of implementing a stack using a linked list over arrays is that it allows the stack to grow or shrink as per the requirements, i.e., memory can be allocated or deallocated dynamically .
- A linked list is a collection of nodes, where each node contains some data and a pointer to the next node in the list. The first node is called the **head** and the last node is called the **tail**. The tail node points to **NULL** to indicate the end of the list.
- To implement a stack using a linked list, we need to maintain a pointer to the top of the stack, which is the head of the linked list. The push operation will insert a new node at the beginning of the list, and the pop operation will delete the first node from the list. The peek operation will return the data of the first node without deleting it. The empty operation will check if the list is empty or not, and the size operation will count the number of nodes in the list.

## Pseudocode for stack operations using linked list

- Define a structure for a node, which contains a data field and a next pointer field.
- Define a global variable for the top pointer, which points to the head of the linked list.
- Define a function to create a new node, which takes a data value as a parameter and returns a pointer to the node.
- Define a function to push a data value into the stack, which takes a data value as a parameter and returns nothing.
  - Create a new node using the create node function and assign the data value to it.
  - If the top pointer is NULL, then the stack is empty and the new node is the first node in the list. Set the top pointer to point to the new node and set the next pointer of the new node to NULL.
  - Else, the stack is not empty and the new node is inserted at the beginning of the list. Set the next pointer of the new node to point to the node pointed by the top pointer and set the top pointer to point to the new node.
- Define a function to pop a data value from the stack, which takes no parameters and returns the data value of the popped node.
  - If the top pointer is NULL, then the stack is empty and there is nothing to pop. Print an error message and return -1.
  - Else, the stack is not empty and the first node is popped from the list. Store the data value of the node pointed by the top pointer in a temporary variable. Set the top pointer to point to the next node in the list and free the memory of the popped node. Return the temporary variable.
- Define a function to peek the data value at the top of the stack, which takes no parameters and returns the data value of the top node.
  - If the top pointer is NULL, then the stack is empty and there is nothing to peek. Print an error message and return -1.
  - Else, the stack is not empty and the first node is the top node. Return the data value of the node pointed by the top pointer.
- Define a function to check if the stack is empty, which takes no parameters and returns a boolean value.
  - If the top pointer is NULL, then the stack is empty and return true.
  - Else, the stack is not empty and return false.
- Define a function to get the size of the stack, which takes no parameters and returns an integer value.
  - Initialize a counter variable to zero.
  - Initialize a temporary pointer to point to the node pointed by the top pointer.
  - Loop through the list until the temporary pointer is NULL, incrementing the counter and moving the temporary pointer to the next node in each iteration.
  - Return the counter value.

## C code for stack operations using linked list

```c
// Define a structure for a node
struct node {
  int data; // data field
  struct node *next; // next pointer field
};

// Define a global variable for the top pointer
struct node *top = NULL;

// Define a function to create a new node
struct node *create_node(int data) {

```




# Implementation of Queue using Linked List

- A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the element that is inserted first is removed first.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A queue can be implemented using a linked list by maintaining two pointers, one for the front of the queue and one for the rear of the queue.
- The front pointer points to the node that is at the head of the list, and the rear pointer points to the node that is at the tail of the list.
- To enqueue an element, a new node is created with the given data and the pointer field set to NULL. The new node is then inserted at the end of the list, and the rear pointer is updated to point to the new node.
- To dequeue an element, the node that is pointed by the front pointer is removed from the list, and the front pointer is updated to point to the next node in the list. The data of the removed node is returned as the dequeued element.
- To check if the queue is empty, the front pointer is compared with NULL. If the front pointer is NULL, then the queue is empty, otherwise it is not.
- To check if the queue is full, the memory allocation for the new node is checked. If the memory allocation fails, then the queue is full, otherwise it is not.
- To display the elements of the queue, the list is traversed from the front pointer to the rear pointer, and the data of each node is printed.
- To free the memory allocated for the queue, the list is traversed from the front pointer to the rear pointer, and each node is deleted. The front and rear pointers are then set to NULL.



# Implementation of Circular Queue using Linked List

- A circular queue is a type of queue data structure that stores elements in a circular manner.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers, front and rear, that point to the first and last nodes of the queue respectively.
- A circular queue is empty when front and rear are NULL, and full when rear->next is front.
- The main operations on a circular queue are enqueue (insert an element at the rear), dequeue (remove an element from the front), and display (print all the elements in the queue).

## Enqueue Operation

- To enqueue an element in a circular queue, we need to perform the following steps:
  - Create a new node and store the data element in it.
  - If the queue is empty, set both front and rear to the new node, and make the new node point to itself.
  - If the queue is not empty, set rear->next to the new node, update rear to the new node, and make the new node point to front.
  - Return the queue.

## Dequeue Operation

- To dequeue an element from a circular queue, we need to perform the following steps:
  - If the queue is empty, return NULL or an error message.
  - If the queue has only one element, store the data element in a temporary variable, free the node, and set both front and rear to NULL.
  - If the queue has more than one element, store the data element in a temporary variable, update front to front->next, free the node, and make rear point to the new front.
  - Return the data element or the queue.

## Display Operation

- To display the elements of a circular queue, we need to perform the following steps:
  - If the queue is empty, return NULL or an error message.
  - If the queue is not empty, initialize a pointer to the front node, and print its data element.
  - Traverse the queue by updating the pointer to the next node, until it reaches the rear node, and print its data element.
  - Return the queue.



# Implementation of Tree Structures, Binary Tree, Tree Traversal, Binary Search Tree, Insertion and Deletion in BST for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Tree Structures
- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has a root node, which is the topmost node in the hierarchy.
- A node can have zero or more child nodes, which are nodes that are directly connected to it by an edge.
- A node that has no child nodes is called a leaf node.
- A node that has at least one child node is called an internal node or a non-leaf node.
- The height of a node is the number of edges on the longest path from the node to a leaf node.
- The height of a tree is the height of the root node.
- The depth of a node is the number of edges on the path from the node to the root node.
- The depth of a tree is the depth of the deepest node in the tree.
- A subtree of a node is the tree formed by the node and all its descendants.
- A binary tree is a special kind of tree in which each node can have at most two child nodes, called the left child and the right child.

## Binary Tree
- A binary tree can be implemented using a dynamic data structure, such as a linked list, or a static data structure, such as an array.
- A linked list implementation of a binary tree uses a node structure that contains three fields: data, left pointer, and right pointer.
- The data field stores the value of the node, and the left and right pointers point to the left and right child nodes, respectively.
- The root node is stored in a separate pointer variable, and the left and right pointers of a leaf node are set to NULL.
- An array implementation of a binary tree uses an array of fixed size to store the nodes of the tree.
- The array is indexed from 1 to n, where n is the number of nodes in the tree.
- The root node is stored at index 1, and the left and right child nodes of a node at index i are stored at index 2i and 2i+1, respectively.
- The array elements that do not correspond to any node are left empty or filled with a special value, such as -1.

## Tree Traversal
- Tree traversal is the process of visiting each node of a tree in a systematic order.
- There are three common ways of traversing a binary tree: inorder, preorder, and postorder.
- Inorder traversal visits the left subtree, the root, and the right subtree of each node in that order.
- Preorder traversal visits the root, the left subtree, and the right subtree of each node in that order.
- Postorder traversal visits the left subtree, the right subtree, and the root of each node in that order.
- Tree traversal can be implemented using recursion or iteration.
- A recursive implementation of tree traversal uses a function that calls itself to visit the left and right subtrees of each node.
- An iterative implementation of tree traversal uses a stack or a queue to store the nodes that need to be visited.

## Binary Search Tree
- A binary search tree (BST) is a special kind of binary tree that satisfies the following property: the value of each node is greater than or equal to the values of all the nodes in its left subtree, and less than or equal to the values of all the nodes in its right subtree.
- A BST can be used to implement a sorted data structure that supports efficient search, insertion, and deletion operations.
- To search for a value in a BST, we start from the root node and compare the value with the node's value. If they are equal, we have found the node. If the value is less than the node's value, we search in the left subtree. If the value is greater than the node's value, we search in the right subtree. We repeat this process until we find the node or reach a leaf node.
- To insert a value in a BST, we follow the same procedure as search, but instead of returning the node, we create a new node with the value and attach it as the left or right child of the leaf node where the search ended.
- To delete a value from a BST, we first search for the node that contains the value. If the node is not found, we do nothing. If the node is found, we have three cases to consider:
  - If the node is a leaf node, we simply delete



# Graph Implementation, BFS, DFS, Minimum cost spanning tree, shortest path algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Graph Implementation

- A graph is a collection of vertices and edges, where each edge connects two vertices.
- A graph can be represented in different ways, such as an adjacency matrix, an adjacency list, or an edge list.
- An adjacency matrix is a two-dimensional array of size V x V, where V is the number of vertices in the graph. The element at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency matrix is easy to implement and query, but it takes O(V^2) space and is inefficient for sparse graphs.
- An adjacency list is an array of linked lists, where each element of the array corresponds to a vertex in the graph. The linked list at index i contains the vertices that are adjacent to vertex i. An adjacency list is more space-efficient than an adjacency matrix, especially for sparse graphs, but it takes more time to check if there is an edge between two vertices.
- An edge list is a list of pairs of vertices, where each pair represents an edge in the graph. An edge list is simple to implement and iterate over, but it takes more time to find the neighbors of a vertex or to check if there is an edge between two vertices.

- In C, we can implement a graph using structures and pointers. For example, we can define a structure for an edge as follows:

```c
// A structure to represent an edge
struct Edge {
    int src; // source vertex
    int dest; // destination vertex
    int weight; // weight of the edge (optional)
    struct Edge* next; // pointer to the next edge in the list
};
```

- Similarly, we can define a structure for a vertex as follows:

```c
// A structure to represent a vertex
struct Vertex {
    int data; // data stored in the vertex (optional)
    struct Edge* head; // pointer to the head of the edge list
};
```

- To represent a graph using an adjacency list, we can use an array of vertices, where each element of the array is a pointer to a vertex structure. For example, we can declare a graph with V vertices as follows:

```c
// A structure to represent a graph
struct Graph {
    int V; // number of vertices
    struct Vertex* array; // array of vertices
};

// A function to create a new graph with V vertices
struct Graph* createGraph(int V) {
    // allocate memory for the graph structure
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    // assign the number of vertices
    graph->V = V;
    // allocate memory for the array of vertices
    graph->array = (struct Vertex*)malloc(V * sizeof(struct Vertex));
    // initialize each vertex and its edge list
    for (int i = 0; i < V; i++) {
        graph->array[i].data = i; // assign some data to the vertex (optional)
        graph->array[i].head = NULL; // initialize the edge list as empty
    }
    // return the graph
    return graph;
}
```

- To add an edge from vertex u to vertex v in the graph, we can create a new edge structure and insert it at the beginning of the edge list of vertex u. For example, we can define a function to add an edge as follows:

```c
// A function to add an edge from u to v in the graph
void addEdge(struct Graph* graph, int u, int v, int weight) {
    // allocate memory for the new edge
    struct Edge* edge = (struct Edge*)malloc(sizeof(struct Edge));
    // assign the source, destination, and weight
    edge->src = u;
    edge->dest = v;
    edge->weight = weight;
    // insert the edge at the beginning of the edge list of u
    edge->next = graph->array[u].head;
    graph->array[u].head = edge;
}
```

- To print the graph, we can iterate over the array of vertices and print the edge list of each vertex. For example, we can define a function to print the graph as follows:

```c
// A function to print the graph
void printGraph(struct Graph* graph) {
    // iterate over the array of vertices
    for (int i = 0;

```




# Computer Organization Lab

- Computer organization lab is a course that teaches the students the basic concepts and principles of computer hardware and architecture.
- The main objectives of this course are:
  - To understand the structure and function of various components of a computer system, such as CPU, memory, I/O devices, buses, etc.
  - To learn how to design and implement simple digital circuits using logic gates, flip-flops, multiplexers, decoders, etc.
  - To learn how to use assembly language and machine code to program a microprocessor or a microcontroller.
  - To learn how to use simulation tools and hardware kits to test and debug the digital circuits and programs.
- The main topics covered in this course are:
  - Number systems and data representation
  - Boolean algebra and logic gates
  - Combinational and sequential circuits
  - Registers, counters, and memory units
  - Instruction set architecture and assembly language
  - Arithmetic and logic unit (ALU) and control unit (CU)
  - Input/output and interrupts
  - Microprocessor and microcontroller
- The main outcomes of this course are:
  - The students will be able to analyze and design simple digital circuits using logic gates and flip-flops.
  - The students will be able to write and execute assembly language and machine code programs for a microprocessor or a microcontroller.
  - The students will be able to use simulation tools and hardware kits to verify and demonstrate the functionality of the digital circuits and programs.
  - The students will be able to apply the knowledge of computer organization and architecture to solve real-world problems.



# Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a combinational logic circuit that performs the addition of two bits and produces a sum and a carry output.
- A full adder is a combinational logic circuit that performs the addition of three bits and produces a sum and a carry output. The third bit is the carry input from the previous stage of addition.
- A half adder can be implemented using an XOR gate and an AND gate. The XOR gate produces the sum output and the AND gate produces the carry output.
- A full adder can be implemented using two half adders and an OR gate. The first half adder takes the two input bits and produces a partial sum and a carry. The second half adder takes the partial sum and the carry input and produces the final sum and a carry. The OR gate combines the two carry outputs and produces the final carry output.
- The following diagram shows the logic circuit of a half adder:

half adder

- The following diagram shows the logic circuit of a full adder:

full adder

- The following table shows the truth table of a half adder:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

- The following table shows the truth table of a full adder:

| A | B | Carry in | Sum | Carry out |
|---|---|----------|-----|-----------|
| 0 | 0 |    0     |  0  |     0     |
| 0 | 0 |    1     |  1  |     0     |
| 0 | 1 |    0     |  1  |     0     |
| 0 | 1 |    1     |  0  |     1     |
| 1 | 0 |    0     |  1  |     0     |
| 1 | 0 |    1     |  0  |     1     |
| 1 | 1 |    0     |  0  |     1     |
| 1 | 1 |    1     |  1  |     1     |

- Half adders and full adders are the basic building blocks of arithmetic logic units that perform arithmetic operations on binary numbers.
- Half adders and full adders can be combined to form n-bit adders that can add two n-bit binary numbers. For example, a 2-bit full adder can be constructed by connecting two full adders in series as shown below:

2-bit full adder

- The applications of half adders and full adders include digital calculators, digital signal processors, microprocessors, data encryption and decryption, error detection and correction, etc.



# Implementing Binary-to-Gray, Gray-to-Binary code conversions

## Binary-to-Gray code conversion

- Binary code is a system of representing numbers, letters, commands, images and sounds using only two symbols: 0 and 1.
- Gray code is a binary numeral system where two successive values differ in only one bit. It is also known as the reflected binary code.
- The conversion from binary code to gray code can be done by using the following steps :
  - Record the most significant bit (MSB) or the leftmost bit of the given binary data as it is, to have MSB of gray equivalent.
  - Proceed towards adding the adjacent bits of the binary data starting from MSB with its adjacent bit to LSB using the XOR (^) operation. The result of each XOR operation is a bit of the gray code.
  - The LSB of the gray code is the same as the LSB of the binary code.
- The logical circuit that performs the binary-to-gray code conversion is known as a binary-to-gray code converter. It consists of XOR gates that take the binary bits as inputs and produce the gray bits as outputs.
- The following is an example of a 4-bit binary-to-gray code converter:

Binary-to-Gray code converter

- The following is the truth table for the 4-bit binary-to-gray code converter:

| Binary | Gray |
|--------|------|
| 0000   | 0000 |
| 0001   | 0001 |
| 0010   | 0011 |
| 0011   | 0010 |
| 0100   | 0110 |
| 0101   | 0111 |
| 0110   | 0101 |
| 0111   | 0100 |
| 1000   | 1100 |
| 1001   | 1101 |
| 1010   | 1111 |
| 1011   | 1110 |
| 1100   | 1010 |
| 1101   | 1011 |
| 1110   | 1001 |
| 1111   | 1000 |

## Gray-to-Binary code conversion

- The conversion from gray code to binary code can be done by using the following steps :
  - Record the MSB or the leftmost bit of the given gray code as it is, to have MSB of binary equivalent.
  - Proceed towards adding the MSB of the binary code with the next bit of the given gray code using the XOR (^) operation. The result of the XOR operation is the next bit of the binary code.
  - Repeat the previous step until all the bits of the gray code are processed.
  - The LSB of the binary code is the same as the LSB of the gray code.
- The logical circuit that performs the gray-to-binary code conversion is known as a gray-to-binary code converter. It consists of XOR gates that take the gray bits as inputs and produce the binary bits as outputs.
- The following is an example of a 4-bit gray-to-binary code converter:

Gray-to-Binary code converter

- The following is the truth table for the 4-bit gray-to-binary code converter:

| Gray  | Binary |
|-------|--------|
| 0000  | 0000   |
| 0001  | 0001   |
| 0011  | 0010   |
| 0010  | 0011   |
| 0110  | 0100   |
| 0111  | 0101   |
| 0101  | 0110   |
| 0100  | 0111   |
| 1100  | 1000   |
| 1101  | 1001   |
| 1111  | 1010   |
| 1110  | 1011   |
| 1010  | 1100   |
| 1011  | 1101   |
| 1001  | 1110   |
| 1000  | 1111   |

## References

: https://www.electrical4u.com/binary-to-gray-code-converter



## Implementing 3-8 line DECODER for the notes of the Computer Organization Lab in the subject of Computer Organization

- A 3-8 line decoder is a digital circuit that converts a 3-bit binary input into an 8-bit output, where only one of the output lines is high (logic 1) and the rest are low (logic 0).
- The 3-bit input represents a decimal number from 0 to 7, and the output line that is high corresponds to that number.
- For example, if the input is 010, the output is 00000100, where the fourth line from the right is high and the rest are low.
- A 3-8 line decoder can be implemented using logic gates, such as AND, OR, and NOT gates.
- The logic expression for each output line can be derived from the truth table of the decoder, where A, B, and C are the input bits and Y0 to Y7 are the output bits.

| A | B | C | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 | Y7 |
|---|---|---|----|----|----|----|----|----|----|----|
| 0 | 0 | 0 | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 0 | 1 | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 0 | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 1 | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1 | 0 | 0 | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1 | 0 | 1 | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1 | 1 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 1 | 1 | 1 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |

- The logic expressions are:

  - Y0 = A'B'C'
  - Y1 = A'B'C
  - Y2 = A'BC'
  - Y3 = A'BC
  - Y4 = AB'C'
  - Y5 = AB'C
  - Y6 = ABC'
  - Y7 = ABC

- Where A', B', and C' are the complements of A, B, and C, respectively.
- A schematic diagram of the 3-8 line decoder using logic gates is shown below:

```
    A ────┐
         ┌┴┐
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         │ │
         └┬┘
    B ────┼────┐
         ┌┴┐  ┌┴┐
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         │ │  │ │
         └┬┘  └┬┘
    C ────┼────┼────┐
         ┌┴┐  ┌┴┐  ┌┴┐
         │ │  │ │  │ │
         │ │  │ │  │ │
         │ │  │ │  │ │
         │

```




# Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A multiplexer (MUX) is a digital device that selects one of the several input signals and forwards it to the output based on some selection logic.
- A 4x1 multiplexer has 4 data inputs, 2 selection lines and one output. A 8x1 multiplexer has 8 data inputs, 3 selection lines and one output.
- A 8x1 multiplexer can be implemented using two 4x1 multiplexers and one 2x1 multiplexer .
- The following steps describe how to implement a 8x1 multiplexer using 4x1 and 2x1 multiplexers:
  - Connect the 8 data inputs (D0 to D7) to the two 4x1 multiplexers (M0 and M1) as shown in the figure below. The data inputs D0 to D3 are connected to M0 and the data inputs D4 to D7 are connected to M1.
  - Connect the two least significant selection lines (S0 and S1) to both M0 and M1. These lines will select one of the four data inputs for each 4x1 multiplexer.
  - Connect the output of M0 and M1 to the inputs of the 2x1 multiplexer (M2). The output of M0 is connected to I0 and the output of M1 is connected to I1 of M2.
  - Connect the most significant selection line (S2) to the selection line of M2. This line will select one of the two outputs of M0 and M1 for the final output of M2.
  - The output of M2 is the output of the 8x1 multiplexer.

8x1 multiplexer using 4x1 and 2x1 multiplexers

- The following table shows the truth table of the 8x1 multiplexer using 4x1 and 2x1 multiplexers:

| S2 | S1 | S0 | Output |
|----|----|----|--------|
| 0  | 0  | 0  | D0     |
| 0  | 0  | 1  | D1     |
| 0  | 1  | 0  | D2     |
| 0  | 1  | 1  | D3     |
| 1  | 0  | 0  | D4     |
| 1  | 0  | 1  | D5     |
| 1  | 1  | 0  | D6     |
| 1  | 1  | 1  | D7     |

- The following expression shows the output function of the 8x1 multiplexer using 4x1 and 2x1 multiplexers:

Output = (S2' * S1' * S0' * D0) + (S2' * S1' * S0 * D1) + (S2' * S1 * S0' * D2) + (S2' * S1 * S0 * D3) + (S2 * S1' * S0' * D4) + (S2 * S1' * S0 * D5) + (S2 * S1 * S0' * D6) + (S2 * S1 * S0 * D7)

where S2', S1' and S0' are the complements of S2, S1 and S0 respectively.



## Verify the excitation tables of various FLIP-FLOPS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A flip-flop is a sequential logic circuit that can store one bit of information. It has two stable states, represented by 0 and 1, and can switch between them in response to input signals.
- The excitation table of a flip-flop shows the required input to the flip-flop to go from the current state to the next state. It is derived from the truth table of the flip-flop, which shows the output for the given combination of inputs and current state.
- There are different types of flip-flops, such as SR, D, JK and T, which have different input signals and excitation tables. The following are the excitation tables of these flip-flops:

### SR flip-flop
- An SR flip-flop has two inputs, S (set) and R (reset), and one output, Q. It can be set to 1 by applying S = 1 and R = 0, reset to 0 by applying S = 0 and R = 1, or hold its current state by applying S = R = 0. Applying S = R = 1 is an invalid input that should be avoided.
- The excitation table of the SR flip-flop is:

| Q(t) | Q(t+1) | S | R |
|------|--------|---|---|
| 0    | 0      | 0 | 0 |
| 0    | 1      | 1 | 0 |
| 1    | 0      | 0 | 1 |
| 1    | 1      | 0 | 0 |

### D flip-flop
- A D flip-flop has one input, D (data), and one output, Q. It can store the value of D by applying a clock pulse. The output Q is equal to the input D at the rising edge of the clock pulse.
- The excitation table of the D flip-flop is:

| Q(t) | Q(t+1) | D |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 0 |
| 1    | 1      | 1 |

### JK flip-flop
- A JK flip-flop has two inputs, J and K, and one output, Q. It can be set to 1 by applying J = 1 and K = 0, reset to 0 by applying J = 0 and K = 1, hold its current state by applying J = K = 0, or toggle its state by applying J = K = 1. The output Q changes at the rising edge of the clock pulse.
- The excitation table of the JK flip-flop is:

| Q(t) | Q(t+1) | J | K |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | 1 | X |
| 1    | 0      | X | 1 |
| 1    | 1      | X | 0 |

- Note: X means don't care, meaning either 0 or 1 can be applied.

### T flip-flop
- A T flip-flop has one input, T (toggle), and one output, Q. It can hold its current state by applying T = 0, or toggle its state by applying T = 1. The output Q changes at the rising edge of the clock pulse.
- The excitation table of the T flip-flop is:

| Q(t) | Q(t+1) | T |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 1 |
| 1    | 1      | 0 |



## Design of an 8-bit Input/ Output system with four 8-bit Internal Registers for the notes of the Computer Organization Lab in the subject of Computer Organization

- An 8-bit input/output system is a system that can read and write 8-bit data from and to external devices, such as keyboards, displays, sensors, etc.
- An 8-bit input/output system typically consists of the following components:
  - An 8-bit data bus that connects the input/output system to the main processor or memory.
  - An 8-bit address bus that specifies the location of the input/output device to be accessed.
  - A control bus that carries signals to control the read and write operations, such as enable, select, strobe, etc.
  - An 8-bit input/output port that interfaces with the external device and provides the data and control signals.
  - An 8-bit input/output controller that manages the input/output operations and communicates with the main processor or memory.
  - Four 8-bit internal registers that store the data and control information for the input/output operations.
- The four 8-bit internal registers are usually named as follows:
  - Data register: holds the 8-bit data to be read from or written to the input/output device.
  - Status register: holds the 8-bit status information of the input/output device, such as ready, busy, error, etc.
  - Command register: holds the 8-bit command code to specify the input/output operation to be performed, such as read, write, reset, etc.
  - Address register: holds the 8-bit address of the input/output device to be accessed.
- The design of an 8-bit input/output system can be illustrated by the following block diagram:

8-bit input/output system block diagram

- The input/output controller can be implemented using a finite state machine (FSM) that responds to the control signals from the main processor or memory and generates the control signals for the input/output port and the internal registers.
- The input/output port can be implemented using a tri-state buffer that allows the data bus to be connected or disconnected from the external device depending on the direction of the data transfer.
- The internal registers can be implemented using D flip-flops that store the data and control information on the rising edge of the clock signal.



# Design of an 8-bit ARITHMETIC LOGIC UNIT

An 8-bit arithmetic logic unit (ALU) is a combinational circuit that performs arithmetic and logic operations on two 8-bit input operands based on control inputs. The ALU is a fundamental component of any computer system, as it performs the basic operations that are required for computation.

The design of an 8-bit ALU can be divided into the following steps:

- Designing a 1-bit full adder, which can perform binary addition of two 1-bit inputs and a carry input, and produce a 1-bit sum output and a carry output.
- Designing an 8-bit adder/subtractor, which can perform binary addition or subtraction of two 8-bit inputs based on a control input, and produce an 8-bit result output and a carry/borrow output. This can be done by cascading eight 1-bit full adders and using a 2's complement circuit for subtraction.
- Designing a 1-bit logic unit, which can perform logic operations such as AND, OR, XOR, and NOT on two 1-bit inputs based on control inputs, and produce a 1-bit output.
- Designing an 8-bit logic unit, which can perform logic operations on two 8-bit inputs based on control inputs, and produce an 8-bit output. This can be done by using eight 1-bit logic units in parallel.
- Designing a multiplexer, which can select one of the two 8-bit inputs based on a control input, and produce an 8-bit output.
- Designing an ALU, which can perform arithmetic or logic operations on two 8-bit inputs based on control inputs, and produce an 8-bit output and a status output. This can be done by using an 8-bit adder/subtractor, an 8-bit logic unit, and a multiplexer, and generating the status output based on the result output and the carry/borrow output.

The following figure shows a block diagram of the 8-bit ALU design:

8-bit ALU block diagram

The ALU has the following inputs and outputs:

- A and B: two 8-bit input operands
- S: a 3-bit control input that selects the operation to be performed
- R: an 8-bit output that shows the result of the operation
- F: a 4-bit status output that shows the flags of the operation, such as zero, sign, overflow, and carry/borrow

The ALU can perform the following operations based on the value of S:

- S = 000: R = A + B, F = {C, V, S, Z}, where C is the carry flag, V is the overflow flag, S is the sign flag, and Z is the zero flag
- S = 001: R = A - B, F = {B, V, S, Z}, where B is the borrow flag
- S = 010: R = A AND B, F = {0, 0, S, Z}
- S = 011: R = A OR B, F = {0, 0, S, Z}
- S = 100: R = A XOR B, F = {0, 0, S, Z}
- S = 101: R = NOT A, F = {0, 0, S, Z}
- S = 110: R = A, F = {0, 0, S, Z}
- S = 111: R = B, F = {0, 0, S, Z}

The following figure shows a schematic diagram of the 8-bit ALU design:

8-bit ALU schematic diagram

The ALU can be implemented using logic gates, such as AND, OR, XOR, and NOT gates, and multiplexers. The following figure shows an example of a 1-bit full adder implementation using logic gates:

1-bit full adder schematic diagram

The following figure shows an example of a 1-bit logic unit implementation using logic gates and multiplexers:

1-bit logic unit schematic diagram

The following figure shows an example of a 2's complement circuit implementation using logic gates:

![2's complement circuit schematic diagram](https://i



# Design the data path of a computer from its register transfer language description

- Register transfer language (RTL) is a system for expressing in symbolic form the microoperation sequences among the registers of a digital module  .
- RTL is also a kind of intermediate representation (IR) that is very close to assembly language, such as that which is used in a compiler .
- RTL can be used to describe data flow at the register-transfer level of an architecture .
- RTL can also be used to facilitate the design process of digital systems.
- To design the data path of a computer from its RTL description, the following steps can be followed:
  - Identify the registers and the data types that they store.
  - Identify the operations and the control signals that are required for each microoperation.
  - Draw the data path diagram that shows the connections among the registers, the functional units, and the multiplexers.
  - Assign the control signals to the multiplexers and the functional units.
  - Write the RTL statements that correspond to each microoperation.
  - Verify the correctness of the data path and the RTL statements by simulating the execution of some instructions.



# Design the control unit of a computer using either hardwiring or microprogramming based on its register transfer language description

- The control unit of a computer is responsible for generating the control signals that direct the execution of instructions by the datapath components.
- The control unit can be designed using either hardwiring or microprogramming techniques, depending on the trade-offs between speed, complexity, and flexibility.
- Hardwiring is a method of implementing the control unit as a combinational circuit that produces the control signals as a function of the current state and the inputs. The state is determined by the instruction register, the condition codes, and the external inputs. The control signals are the outputs of the circuit that activate the micro-operations, such as register transfers, arithmetic operations, memory accesses, etc.
- Microprogramming is a method of implementing the control unit as a programmable device that stores the control signals as words in a special memory called the microprogram store. The control signals are generated by executing a sequence of micro-instructions, each of which specifies a set of micro-operations to be performed in one clock cycle. The micro-instructions are fetched from the microprogram store according to the address specified by a microprogram counter, which can be incremented, decremented, or branched depending on the control logic.
- Register transfer language (RTL) is a notation that describes the behavior of a digital system at the level of register transfers and logic operations. RTL can be used to specify the instruction set architecture (ISA) of a computer, as well as the micro-operations that implement each instruction. RTL can also be used as an intermediate step in the design of the control unit, either by translating it into a hardwired circuit or by encoding it into a microprogram.
- The steps for designing the control unit using either hardwiring or microprogramming based on the RTL description are as follows:

  - Identify the datapath components, such as registers, buses, ALU, memory, etc., and their inputs and outputs.
  - Define the control signals that are needed to activate the micro-operations on the datapath components, such as load, enable, select, read, write, etc.
  - Write the RTL description of each instruction in the ISA, using the control signals and the datapath components. The RTL description should specify the sequence of micro-operations that are performed in each clock cycle to execute the instruction.
  - For hardwiring, translate the RTL description into a state diagram that shows the states and the transitions of the control unit for each instruction. The states correspond to the clock cycles, and the transitions depend on the inputs and the outputs. The outputs are the control signals that are generated in each state. The state diagram can then be converted into a state table, and then into a logic circuit using combinational logic design techniques.
  - For microprogramming, encode the RTL description into a microprogram that consists of a sequence of micro-instructions for each instruction. Each micro-instruction should contain the control signals that are generated in one clock cycle, as well as the next address of the microprogram counter. The micro-instructions can be stored in the microprogram store as words, and the microprogram counter can be implemented as a register that can be manipulated by the control logic. The control logic can be designed using combinational or sequential logic techniques.



## Implement a simple instruction set computer with a control unit and a data path

- A simple instruction set computer (SISC) is a computer that uses a small and simple set of instructions to perform basic operations, such as arithmetic, logic, data transfer, and control flow.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of the instructions by the data path.
- A data path (DP) is a component of the SISC that performs the data processing operations, such as fetching, decoding, executing, and storing the instructions and the operands.
- To implement a SISC with a CU and a DP, the following steps are required:

  - Define the instruction set architecture (ISA) of the SISC, which specifies the format, encoding, and semantics of the instructions, as well as the registers, memory, and addressing modes of the SISC .
  - Design the CU of the SISC, which consists of a finite state machine (FSM) that generates the control signals based on the current state and the instruction opcode. The CU can be implemented using combinational logic circuits, such as multiplexers, decoders, and encoders .
  - Design the DP of the SISC, which consists of the following components  :
    - A program counter (PC) that holds the address of the next instruction to be executed.
    - An instruction memory (IM) that stores the instructions of the SISC program.
    - An instruction register (IR) that holds the current instruction to be decoded and executed.
    - An arithmetic logic unit (ALU) that performs the arithmetic and logic operations on the operands.
    - A data memory (DM) that stores the data values of the SISC program.
    - A set of general-purpose registers (GPRs) that hold the operands and the results of the operations.
    - A set of buses and wires that connect the components and transfer the data and the control signals.
  - Connect the CU and the DP of the SISC using the control signals and the data signals. The CU controls the DP by sending the control signals to the components of the DP, such as the PC, the IM, the IR, the ALU, the DM, and the GPRs. The DP sends the data signals to the CU, such as the instruction opcode, the operands, and the results .
  - Test and verify the functionality and the performance of the SISC using simulation tools, such as Logisim, Verilog, or VHDL. The SISC can be simulated using different input programs and test cases, and the output can be compared with the expected output .

- The following diagram shows an example of a SISC with a CU and a DP:

SISC with CU and DP

- The SISC in the diagram uses a 16-bit ISA, which has four types of instructions: R-type, I-type, J-type, and H-type. The R-type instructions perform arithmetic and logic operations on two registers and store the result in a third register. The I-type instructions perform arithmetic and logic operations on a register and an immediate value and store the result in a register. The J-type instructions perform unconditional jumps to a specified address. The H-type instructions halt the execution of the program. The SISC has eight 16-bit GPRs, numbered from R0 to R7. The SISC has a 16-bit PC, a 16-bit IR, and a 16-bit ALU. The SISC has a 256-word IM and a 256-word DM, each word being 16 bits. The SISC has a 4-bit opcode field, a 3-bit source register field, a 3-bit destination register field, and a 6-bit immediate field. The SISC has the following control signals: PCEn, IMEn, IRLd, ALUOp, ALUSrc, RegDst, RegWr, DMEn, DMLd, and PCSrc.

- The following table shows the format and the encoding of the instructions of the SISC[^1



# Discrete Structure & Logic Lab

Discrete Structure & Logic Lab is a course that covers fundamental concepts of discrete mathematics, such as logic, proofs, sets, relations, functions, counting, and probability, with an emphasis on applications in computer science. The course also involves programming exercises using C and Mapple to implement and explore some of the concepts.

Some of the topics and objectives of the course are:

- To understand and use propositional and predicate logic, and to apply logical reasoning and proof techniques to various problems.
- To learn and apply the basic methods of set theory, such as set operations, cardinality, inclusion-exclusion principle, and power sets.
- To learn and apply the concepts of relations and functions, such as equivalence relations, partial orders, inverse and composite functions, and one-to-one and onto functions.
- To learn and apply the principles of counting and combinatorics, such as permutations, combinations, binomial coefficients, and recurrence relations.
- To learn and apply the basics of probability theory, such as events, sample spaces, conditional probability, Bayes' theorem, and random variables.
- To write programs in C and Mapple to create and manipulate sets, relations, functions, and other discrete structures, and to perform operations and calculations on them.
- To use the Alloy tool to model and analyze logic and relational algebra problems, and to verify properties and specifications of discrete structures.



# Introduction to digital electronics lab- nomenclature of digital ICs, specifications, study of the data sheet, Concept of Vcc and ground, verification of the truth tables of logic gates using TTL ICs

- Digital electronics is the branch of electronics that deals with the manipulation of binary digits (0 and 1) using logic gates, flip-flops, counters, multiplexers, etc.
- Digital ICs (Integrated Circuits) are the basic building blocks of digital systems. They are classified into different families based on their fabrication technology, power consumption, speed, noise immunity, etc. Some of the common families are TTL (Transistor-Transistor Logic), CMOS (Complementary Metal-Oxide Semiconductor), ECL (Emitter-Coupled Logic), etc.
- Nomenclature of digital ICs is the systematic way of naming and identifying the ICs based on their family, function, number of pins, package type, etc. For example, 74LS04 is a TTL IC that has six NOT gates, 14 pins, and a low-power Schottky package.
- Specifications of digital ICs are the technical parameters that describe the performance and characteristics of the ICs, such as supply voltage, operating temperature, propagation delay, fan-out, power dissipation, etc. These specifications are usually given in the data sheet of the ICs, which is a document that provides detailed information about the ICs, such as pin configuration, function table, electrical characteristics, etc.
- Concept of Vcc and ground is the basic principle of providing power supply to the digital ICs. Vcc is the positive terminal of the power supply, which is usually 5V for TTL ICs and 3.3V or 1.8V for CMOS ICs. Ground is the negative terminal of the power supply, which is usually 0V. The ICs must be connected to Vcc and ground properly to function correctly.
- Verification of the truth tables of logic gates using TTL ICs is the experimental procedure of testing the functionality and output of the logic gates using the TTL ICs and a digital trainer. A logic gate is a device that performs a basic logical operation, such as AND, OR, NOT, etc. A truth table is a table that shows the output of a logic gate for all possible combinations of inputs. For example, the truth table of a NOT gate is:

| Input | Output |
| ----- | ------ |
| 0     | 1      |
| 1     | 0      |

To verify the truth table of a NOT gate using a TTL IC, we need to use a 74LS04 IC, which has six NOT gates, and a digital trainer, which is a device that provides power supply, switches, LEDs, etc. for testing digital circuits. The steps are:

1. Connect the Vcc pin (14) of the IC to the +5V terminal of the trainer, and the ground pin (7) of the IC to the 0V terminal of the trainer.
2. Connect the input pin (1) of the first NOT gate of the IC to a switch on the trainer, and the output pin (2) of the first NOT gate of the IC to an LED on the trainer.
3. Turn on the power supply of the trainer, and observe the LED.
4. Toggle the switch, and observe the LED again.
5. Record the input and output values in a table, and compare them with the truth table of the NOT gate.
6. Repeat the steps 2 to 5 for the other five NOT gates of the IC, using different pins and switches.



# Implementation of the given Boolean function using logic gates in both SOP and POS forms

- A Boolean function is a mathematical expression that maps a set of input values to a single output value, where the inputs and outputs are either 0 (false) or 1 (true).
- Logic gates are electronic devices that implement Boolean functions using physical phenomena such as voltage, current, or light.
- SOP (Sum of Products) and POS (Product of Sums) are two standard forms of representing Boolean functions using logic gates.
- SOP form is a Boolean expression that consists of one or more product terms (AND operations) added together (OR operation).
- POS form is a Boolean expression that consists of one or more sum terms (OR operations) multiplied together (AND operation).
- To implement a given Boolean function using logic gates in both SOP and POS forms, the following steps can be followed:

## SOP Implementation

- Write the truth table of the given Boolean function, showing all possible combinations of inputs and the corresponding output.
- Identify the rows in the truth table where the output is 1 (true).
- For each row where the output is 1, write a product term that corresponds to the input values. Use the input variable if it is 1, and use the complement (negation) of the input variable if it is 0.
- OR all the product terms together to obtain the SOP expression of the Boolean function.
- Simplify the SOP expression using Boolean algebra rules or Karnaugh map if possible.
- Draw the logic circuit diagram of the SOP expression using AND gates and OR gates. Use NOT gates for the complements of the input variables if needed.

## POS Implementation

- Write the truth table of the given Boolean function, showing all possible combinations of inputs and the corresponding output.
- Identify the rows in the truth table where the output is 0 (false).
- For each row where the output is 0, write a sum term that corresponds to the input values. Use the complement (negation) of the input variable if it is 1, and use the input variable if it is 0.
- AND all the sum terms together to obtain the POS expression of the Boolean function.
- Simplify the POS expression using Boolean algebra rules or Karnaugh map if possible.
- Draw the logic circuit diagram of the POS expression using OR gates and AND gates. Use NOT gates for the complements of the input variables if needed.

## Example

- Consider the following Boolean function of three inputs A, B, and C:

F(A, B, C) = A'B + BC

- The truth table of this function is:

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

- The SOP implementation of this function is:

F(A, B, C) = A'B + BC

This expression is already in SOP form, so no further simplification is needed.

The logic circuit diagram of this expression is:

SOP circuit

- The POS implementation of this function is:

F(A, B, C) = (A + B' + C')(A' + B' + C)(A' + B + C')

This expression is obtained by writing the sum terms for the rows where the output is 0, and then ANDing them together.

This expression can be simplified using Boolean algebra rules as:

F(A, B, C) = (A + B' + C')(A' + B' + C)(A' + B + C')
= (A + B' + C')(A'B' + A'C + BC + B'C)(A' + B + C')
= (A + B' + C')(A'B'C' + A'B'C + A'BC' + A'BC + AB'C' + AB'C + ABC' + ABC)(A' + B + C')
= (A'B'C' + A'B'C + A'BC' + A'BC + AB'C' + AB'C + ABC' +



# Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is a bistable circuit that can store one bit of information. It has two stable states, represented by 0 and 1, and can switch between them in response to input signals.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a different characteristic equation that defines the output in terms of the input and the previous state.
- RS flip-flop: The output Q depends on the inputs S (set) and R (reset). If S=1 and R=0, Q is set to 1. If S=0 and R=1, Q is reset to 0. If S=0 and R=0, Q remains unchanged. If S=1 and R=1, the output is undefined.
- JK flip-flop: The output Q depends on the inputs J and K, as well as the clock signal CLK. On the rising edge of CLK, if J=1 and K=0, Q is set to 1. If J=0 and K=1, Q is reset to 0. If J=1 and K=1, Q is toggled (complemented). If J=0 and K=0, Q remains unchanged.
- T flip-flop: The output Q depends on the input T (toggle) and the clock signal CLK. On the rising edge of CLK, if T=1, Q is toggled. If T=0, Q remains unchanged.
- D flip-flop: The output Q depends on the input D (data) and the clock signal CLK. On the rising edge of CLK, Q is set to the value of D.

- To verify the state tables of these flip-flops, we can use NAND or NOR gates to implement them. NAND and NOR gates are universal gates, meaning they can be used to construct any other logic gate or circuit.
- RS flip-flop using NAND gates: The circuit diagram and the truth table are shown below.

RS flip-flop using NAND gates

| S | R | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 0 | 1  |
| 1 | 0 | 1 | 0  |
| 1 | 1 | X | X  |

- RS flip-flop using NOR gates: The circuit diagram and the truth table are shown below.

RS flip-flop using NOR gates

| S | R | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 1 | 0  |
| 1 | 0 | 0 | 1  |
| 1 | 1 | X | X  |

- JK flip-flop using NAND gates: The circuit diagram and the truth table are shown below.

JK flip-flop using NAND gates

| J | K | Q(t) | Q(t+1) |
|---|---|------|--------|
| 0 | 0 | 0    | 0      |
| 0 | 0 | 1    | 1      |
| 0 | 1 | 0    | 0      |
| 0 | 1 | 1    | 0      |
| 1 | 0 | 0    | 1      |
| 1 | 0 | 1    | 1      |
| 1 | 1 | 0    | 1      |
| 1 | 1 | 1    | 0      |

- JK flip-flop using NOR gates: The circuit diagram and the truth table are shown below.

JK flip-flop using NOR gates

| J | K | Q(t) | Q(t+1) |
|---|---|------|--------|
| 0 | 0 | 0



## Implementation and verification of Decoder using logic gates

A decoder is a combinational logic circuit that converts a binary code into a corresponding output code. For example, a BCD to seven segment decoder takes a four-bit binary input and produces seven output bits that can be used to display a decimal digit on a seven segment display. A decoder can also generate the minterms of a given input code, which can be used to implement any boolean function using external OR gates.

A decoder can be implemented using logic gates such as AND, OR and NOT. The number of input and output lines of a decoder depends on the type of code it converts. For example, a 3-to-8 decoder has three input lines and eight output lines, and it converts a 3-bit binary code into an 8-bit one-hot code, where only one output line is high for each input combination.

The truth table of a 3-to-8 decoder is shown below:

| Input | Output |
|:-----:|:------:|
| X Y Z | D0 D1 D2 D3 D4 D5 D6 D7 |
| 0 0 0 | 1 0 0 0 0 0 0 0 |
| 0 0 1 | 0 1 0 0 0 0 0 0 |
| 0 1 0 | 0 0 1 0 0 0 0 0 |
| 0 1 1 | 0 0 0 1 0 0 0 0 |
| 1 0 0 | 0 0 0 0 1 0 0 0 |
| 1 0 1 | 0 0 0 0 0 1 0 0 |
| 1 1 0 | 0 0 0 0 0 0 1 0 |
| 1 1 1 | 0 0 0 0 0 0 0 1 |

The logic circuit of a 3-to-8 decoder can be derived from the truth table by using the canonical sum-of-products form of the output functions. For example, the output function for D0 is:

D0 = X' Y' Z'

where X', Y' and Z' are the complements of X, Y and Z respectively. Similarly, the output functions for the other output lines can be obtained. The logic circuit of a 3-to-8 decoder using AND, OR and NOT gates is shown below:

3-to-8 decoder logic circuit

To verify the functionality of the decoder, the input lines can be connected to switches and the output lines can be connected to LEDs. By changing the input switches, the corresponding output LED should light up, indicating the correct conversion of the input code to the output code. Alternatively, the decoder can be simulated using a logic gate calculator or a software tool such as Logisim.



# Implementation and verification of Encoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An encoder is a digital circuit that converts a set of binary inputs into a unique binary code.
- The binary code represents the position of the input and is used to identify the specific input that is active.
- Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.
- There are different types of encoders, such as 4, 8, and 16 encoders, and the truth table of encoders depends upon a particular encoder chosen by the user.
- A simple encoder is a combinational logic circuit that can be used to convert 2^n lines of digital input into n bits of coded binary output.
- However, in a simple encoder, only one of the inputs is considered to be high out of all the 2^n inputs.
- A simple encoder can be implemented using OR gates.
- For example, a 4-bit encoder can be designed as follows:

4-bit encoder using OR gates

- The truth table of the 4-bit encoder is:

| Input | Output |
|:-----:|:------:|
| D0    | 00     |
| D1    | 01     |
| D2    | 10     |
| D3    | 11     |

- The Boolean expressions for the output bits are:

Y0 = D1 + D3

Y1 = D2 + D3

- To verify the encoder using logic gates, we can use a breadboard, LEDs, switches, and OR gate ICs.
- The steps are:

  - Connect the power supply to the breadboard and the OR gate ICs.
  - Connect the switches to the inputs of the OR gate ICs and the LEDs to the outputs of the OR gate ICs.
  - Connect the inputs and outputs of the OR gate ICs according to the circuit diagram.
  - Turn on the power supply and test the encoder by changing the switch positions and observing the LED states.
  - Compare the LED states with the truth table and verify that the encoder works correctly.



# Implementation of 4:1 multiplexer using logic gates

A multiplexer is a combinational circuit that takes multiple inputs and delivers only a single output. It consists of input data lines, selection lines and a single output line. A 4:1 multiplexer has 4 input data lines, 2 selection lines and 1 output line. The output is determined by the values of the selection lines. The truth table for a 4:1 multiplexer is shown below:

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | A0 |
| 0  | 1  | A1 |
| 1  | 0  | A2 |
| 1  | 1  | A3 |

The output Y can be expressed as a Boolean function of the inputs and the selection lines as follows:

Y = A0.S1'.S0' + A1.S1'.S0 + A2.S1.S0' + A3.S1.S0

This function can be implemented using logic gates as shown in the diagram below:

4:1 multiplexer using logic gates

The circuit requires two NOT gates, four AND gates and one OR gate. The NOT gates are used to invert the selection lines S1 and S0. The AND gates are used to perform the product terms of the function. The OR gate is used to perform the sum of the product terms. The output Y is obtained at the output of the OR gate.

The 4:1 multiplexer can be used to implement any logic function of four variables by assigning the input data lines to the appropriate logic values. For example, to implement the function F = A.B + C.D, we can assign A0 = 0, A1 = C, A2 = B, A3 = 1 and connect the variables A and D to the selection lines S1 and S0 respectively. The output Y will then be equal to F.



# Implementation of 1:4 demultiplexer using logic gates

- A demultiplexer is a digital circuit that takes one input signal and distributes it to one of several output signals based on some selection criteria.
- A 1:4 demultiplexer has one input signal (D), two selection lines (S1 and S0) and four output signals (Y0 to Y3).
- The input signal is connected to one of the four output signals depending on the binary value of the selection lines.
- The truth table for a 1:4 demultiplexer is shown below:

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

- A 1:4 demultiplexer can be implemented using logic gates such as AND, NOT and OR gates.
- One possible implementation is shown below:

1:4 demultiplexer using logic gates

- In this implementation, the input signal D is ANDed with the complement of S1 and S0 to get Y0, with the complement of S1 and S0 to get Y1, with S1 and the complement of S0 to get Y2, and with S1 and S0 to get Y3.
- The output signals are ORed together to get the output of the demultiplexer.
- The logic equations for the output signals are:

Y0 = D.(S1'.S0')
Y1 = D.(S1'.S0)
Y2 = D.(S1.S0')
Y3 = D.(S1.S0)

- Where ' denotes the complement of a signal.
- A 1:4 demultiplexer can be used for various applications such as data distribution, memory addressing, control signal generation, etc.



# Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four full adders with a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder by connecting the inputs and outputs as shown below :

7483 IC pin diagram

- The inputs A3, A2, A1, A0 and B3, B2, B1, B0 are the two 4-bit numbers to be added. The outputs S3, S2, S1, S0 are the 4-bit sum and Cout is the carry output. The inputs Cin and GND are connected to ground (logic 0) and the input Vcc is connected to a 5V power supply.
- The truth table for the 4-bit parallel adder using 7483 IC is given below:

7483 IC truth table

- The logic expression for the outputs are:

S0 = A0 ⊕ B0 ⊕ Cin

S1 = A1 ⊕ B1 ⊕ C1

S2 = A2 ⊕ B2 ⊕ C2

S3 = A3 ⊕ B3 ⊕ C3

Cout = G3 + P3G2 + P3P2G1 + P3P2P1C1

where C1, C2, C3 are the internal carry outputs and G1, G2, G3 and P1, P2, P3 are the generate and propagate signals of the full adders, respectively.

- The schematic diagram for the 4-bit parallel adder using 7483 IC is shown below:

7483 IC schematic diagram

- The 7483 IC can also be used to perform subtraction of two 4-bit numbers by using the 2's complement method. This can be done by connecting the inputs A3, A2, A1, A0 to the minuend, the inputs B3, B2, B1, B0 to the 2's complement of the subtrahend, and the input Cin to logic 1. The outputs S3, S2, S1, S0 will give the 2's complement of the difference and Cout will indicate the borrow output.



## Design and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The design and verification steps are as follows:

- Step 1: Choose the type of flip-flop to use. For this example, we will use J-K flip-flops, which have two inputs J and K, and two outputs Q and Q'. The J-K flip-flop can toggle, set, reset, or hold its state depending on the values of J and K. The truth table of the J-K flip-flop is shown below:

| J | K | Q(t+1) | Operation |
|---|---|--------|-----------|
| 0 | 0 | Q(t)   | Hold      |
| 0 | 1 | 0      | Reset     |
| 1 | 0 | 1      | Set       |
| 1 | 1 | Q'(t)  | Toggle    |

- Step 2: Determine the state transition table of the 4-bit counter. The counter has four states, Q3 Q2 Q1 Q0, which represent the binary values from 0 to 15. The next state, Q3(t+1) Q2(t+1) Q1(t+1) Q0(t+1), is obtained by adding 1 to the current state modulo 16. The state transition table is shown below:

| Q3 | Q2 | Q1 | Q0 | Q3(t+1) | Q2(t+1) | Q1(t+1) | Q0(t+1) |
|----|----|----|----|---------|---------|---------|---------|
| 0  | 0  | 0  | 0  | 0       | 0       | 0       | 1       |
| 0  | 0  | 0  | 1  | 0       | 0       | 1       | 0       |
| 0  | 0  | 1  | 0  | 0       | 0       | 1       | 1       |
| 0  | 0  | 1  | 1  | 0       | 1       | 0       | 0       |
| 0  | 1  | 0  | 0  | 0       | 1       | 0       | 1       |
| 0  | 1  | 0  | 1  | 0       | 1       | 1       | 0       |
| 0  | 1  | 1  | 0  | 0       | 1       | 1       | 1       |
| 0  | 1  | 1  | 1  | 1       | 0       | 0       | 0       |
| 1  | 0  | 0  | 0  | 1       | 0       | 0       | 1       |
| 1  | 0  | 0  | 1  | 1       | 0       | 1       | 0       |
| 1  | 0  | 1  | 0  | 1       | 0       | 1       | 1       |
| 1  | 0  | 1  | 1  | 1       | 1       | 0       | 0       |
| 1  | 1  | 0  | 0  | 1       | 1       | 0       | 1       |
| 1  | 1  | 0  | 1  | 1       | 1       | 1       | 0       |
| 1  | 1  | 1  | 0  | 1       | 1       | 1       | 1       |
| 1  | 1  | 1  | 1  | 0       | 0       | 0       | 0       |

- Step 3: Derive the excitation equations for each flip-flop. The excitation equations are the expressions for the J and



# Design and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An asynchronous counter is a type of binary counter that does not use a common clock signal for all the flip-flops in the circuit. Instead, each flip-flop is triggered by the output of the previous one, creating a ripple effect. This makes the counter simpler to design, but also slower and less reliable than a synchronous counter.
- A 4-bit asynchronous counter can count from 0 to 15 (0000 to 1111 in binary) before it resets to 0. It can be implemented using four J-K flip-flops, which are edge-triggered devices that can toggle, set, reset, or hold their output depending on the inputs J and K.
- The design steps of a 4-bit asynchronous counter using J-K flip-flops are as follows:
  - Connect the clock input of the first flip-flop (A) to an external clock source, and the clock inputs of the other flip-flops (B, C, and D) to the Q outputs of the previous flip-flops. This creates a chain of flip-flops that are triggered by the output changes of the previous ones.
  - Connect the J and K inputs of all the flip-flops to logic 1 (HIGH). This ensures that the flip-flops will toggle their output on every negative edge of the clock signal.
  - Connect the Q outputs of the flip-flops to LEDs or other devices to display the count value.
- The circuit diagram of a 4-bit asynchronous counter using J-K flip-flops is shown below:

4-bit asynchronous counter circuit diagram

- The truth table of a 4-bit asynchronous counter using J-K flip-flops is shown below:

| Clock | Q<sub>D</sub> | Q<sub>C</sub> | Q<sub>B</sub> | Q<sub>A</sub> | Count |
| ----- | ------------- | ------------- | ------------- | ------------- | ----- |
| 0     | 0             | 0             | 0             | 0             | 0     |
| 1     | 0             | 0             | 0             | 1             | 1     |
| 0     | 0             | 0             | 1             | 0             | 2     |
| 1     | 0             | 0             | 1             | 1             | 3     |
| 0     | 0             | 1             | 0             | 0             | 4     |
| 1     | 0             | 1             | 0             | 1             | 5     |
| 0     | 0             | 1             | 1             | 0             | 6     |
| 1     | 0             | 1             | 1             | 1             | 7     |
| 0     | 1             | 0             | 0             | 0             | 8     |
| 1     | 1             | 0             | 0             | 1             | 9     |
| 0     | 1             | 0             | 1             | 0             | 10    |
| 1     | 1             | 0             | 1             | 1             | 11    |
| 0     | 1             | 1             | 0             | 0             | 12    |
| 1     | 1             | 1             | 0             | 1             | 13    |
| 0     | 1             | 1             | 1             | 0             | 14    |
| 1     | 1             | 1             | 1             | 1             | 15    |
| 0     | 0             | 0             | 0             | 0             | 0     |

- The verification of a 4-bit asynchronous counter using J-K flip-flops can be done by simulating the circuit using software tools such as Logisim or Proteus, or by building the circuit using hardware components such as ICs, breadboards, and LEDs. The verification steps are as follows:
  - Apply

