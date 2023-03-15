### Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

- A linked list is a linear data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
- A linked list can be implemented using either an array or a pointer-based approach.
- In the array implementation, a fixed-size array is used to store the nodes of the linked list. Each node has an index and a next field that stores the index of the next node. The first node has index 0 and the last node has a next field of -1 or null to indicate the end of the list. The array implementation has the advantage of random access and efficient memory allocation, but the disadvantage of limited size and difficulty in insertion and deletion operations.
- In the pointer implementation, each node is a dynamic memory object that contains some data and a pointer to the next node. The pointer implementation has the advantage of flexibility and ease of insertion and deletion operations, but the disadvantage of memory overhead and sequential access.
- A singly linked list is a linked list where each node has only one pointer to the next node. A singly linked list can be traversed in one direction only, from the head node to the tail node.
- A doubly linked list is a linked list where each node has two pointers, one to the next node and one to the previous node. A doubly linked list can be traversed in both directions, from the head node to the tail node or vice versa.
- A circularly linked list is a linked list where the last node points to the first node, forming a loop. A circularly linked list has no head or tail node, and can be traversed indefinitely in either direction.
- Some common operations on a linked list are:
  - Insertion: adding a new node to the list at a specified position.
  - Deletion: removing an existing node from the list at a specified position.
  - Traversal: visiting each node in the list and performing some action on the data or the node.
  - Search: finding a node in the list that matches a given criterion or value.
  - Sort: rearranging the nodes in the list according to some order or comparison function.
  - Reverse: reversing the order of the nodes in the list.
- A polynomial is an algebraic expression that consists of one or more terms, each term being a product of a constant coefficient and a variable raised to a non-negative integer power. For example, 3x^2 + 2x - 5 is a polynomial of degree 2 in the variable x.
- A polynomial can be represented using a linked list, where each node contains the coefficient and the exponent of a term, and the nodes are arranged in descending order of the exponents. For example, the polynomial 3x^2 + 2x - 5 can be represented by the linked list:

| Coefficient | Exponent | Next |
| ----------- | -------- | ---- |
| 3           | 2        | ->   |
| 2           | 1        | ->   |
| -5          | 0        | null |

- A polynomial can also be represented using an array, where each element of the array stores the coefficient of a term, and the index of the element corresponds to the exponent of the term. For example, the polynomial 3x^2 + 2x - 5 can be represented by the array:

| Index | 0  | 1 | 2  |
| ----- | -- | - | -- |
| Value | -5 | 2 | 3  |

- The array representation has the advantage of random access and efficient memory allocation, but the disadvantage of limited size and difficulty in handling sparse polynomials (polynomials with many zero coefficients).
- The linked list representation has the advantage of flexibility and ease of handling sparse polynomials, but the disadvantage of memory overhead and sequential access.
- Some common operations on polynomials are:
  - Addition: adding two polynomials by adding the coefficients of the corresponding terms and creating a new polynomial with the resulting coefficients and exponents. For example, (3x^2 + 2x - 5) + (4x^3 - x + 1) = (4x^3 + 3x^2 + x - 4).
  - Subtraction: subtracting two polynomials by subtracting the coefficients of the corresponding terms and creating a new polynomial with the resulting coefficients and exponents. For example, (3x^2 + 2x -