### Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

A linked list is a linear data structure where each element is a separate object with a data part and a reference to the next element. The last element has a reference to null. The entry point into a linked list is called the head of the list. 

There are two ways to implement a linked list: using an array or using pointers.

#### Array Implementation of Linked Lists
In the array implementation, the linked list is stored in an array. Each element of the array contains the data part and the index of the next element. The index of the first element is stored in a separate variable called the head. The main disadvantage of this implementation is that the size of the list is fixed and cannot be changed during runtime.

#### Pointer Implementation of Singly Linked Lists
In the pointer implementation, each element of the list is represented by a node. A node contains the data part and a pointer to the next node. The head is a pointer to the first node. The main advantage of this implementation is that the size of the list can be changed during runtime.

#### Doubly Linked List
A doubly linked list is a linked list where each node has two pointers, one to the next node and one to the previous node. This allows for more efficient traversal in both directions.

#### Circularly Linked List
A circularly linked list is a linked list where the last node points to the first node instead of null. This allows for more efficient traversal and rotation of the list.

#### Operations on a Linked List
The main operations on a linked list are insertion, deletion, and traversal.

##### Insertion
To insert an element into a linked list, a new node is created with the data part set to the value to be inserted. The next pointer of the new node is set to the next pointer of the node before the insertion point. The next pointer of the node before the insertion point is set to the new node.

##### Deletion
To delete an element from a linked list, the next pointer of the node before the deletion point is set to the next pointer of the node to be deleted. The node to be deleted is then removed.

##### Traversal
To traverse a linked list, a pointer is set to the head of the list and then moved along the list by following the next pointers until the end of the list is reached.

#### Polynomial Representation and Addition, Subtraction & Multiplications of Single variable & Two variables Polynomial
A polynomial can be represented as a linked list where each node contains the coefficient and the exponent of a term. Addition, subtraction, and multiplication of polynomials can be performed by traversing the linked lists and performing the corresponding operations on the coefficients and exponents of the terms.