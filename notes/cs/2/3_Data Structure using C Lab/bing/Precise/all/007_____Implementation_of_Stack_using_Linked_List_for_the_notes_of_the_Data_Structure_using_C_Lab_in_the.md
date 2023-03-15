### Implementation of Stack using Linked List

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array or a linked list. In this section, we will discuss the implementation of a stack using a linked list.

#### Advantages of using a linked list to implement a stack
- Dynamic size: The size of the stack can grow or shrink as needed, without the need to specify the maximum size beforehand.
- Ease of insertion and deletion: Insertion and deletion of elements in a stack implemented using a linked list is easier compared to an array-based implementation.

#### Steps to implement a stack using a linked list
1. Define a `Node` structure to represent a node in the linked list. The `Node` structure should contain two fields: `data` to store the value of the node and `next` to store the address of the next node in the list.
2. Define a `Stack` structure to represent the stack. The `Stack` structure should contain a `top` field to keep track of the top element of the stack.
3. Initialize the `top` field of the `Stack` structure to `NULL` to represent an empty stack.
4. To push an element onto the stack, create a new node with the given value and insert it at the beginning of the linked list. Update the `top` field of the `Stack` structure to point to the new node.
5. To pop an element from the stack, check if the stack is empty. If the stack is not empty, remove the first node from the linked list and update the `top` field of the `Stack` structure to point to the next node. Return the value of the removed node.
6. To check if the stack is empty, check if the `top` field of the `Stack` structure is `NULL`.

This is a brief overview of how to implement a stack using a linked list in the C programming language. You can use this information as a starting point to write your own implementation of a stack using a linked list for your Data Structure using C Lab.