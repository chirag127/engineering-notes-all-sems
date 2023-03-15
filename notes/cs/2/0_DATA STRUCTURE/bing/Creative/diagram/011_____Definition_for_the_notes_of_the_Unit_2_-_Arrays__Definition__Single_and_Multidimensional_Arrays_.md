# Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Definition

- An array is a **linear data structure** that collects elements of the **same data type** and stores them in **contiguous and adjacent memory locations**.
- An array is identified by its **name** and **size**. The size of an array is the **number of elements** it can hold.
- Each element of an array has a unique **index** or **key** that determines its position in the array. The index of an element is usually a **non-negative integer** that ranges from **0** to **n-1**, where **n** is the size of the array.
- An array can be accessed or modified by using its name and index. For example, `A[2]` refers to the third element of the array `A`.
- An array can be **declared** by specifying its name, data type and size. For example, `int A[10]` declares an array of 10 integers named `A`.
- An array can be **initialized** by assigning values to its elements. For example, `A[0] = 5` assigns the value 5 to the first element of the array `A`.
- An array can be **traversed** by using a loop that iterates over its elements. For example, `for (i = 0; i < 10; i++) { print(A[i]); }` prints all the elements of the array `A`.

## Single and Multidimensional Arrays

- A **single-dimensional array** or a **one-dimensional array** is an array that has only one dimension or one level of elements. For example, `int A[10]` is a single-dimensional array of 10 integers.
- A **multidimensional array** is an array that has more than one dimension or more than one level of elements. For example, `int A[3][4]` is a two-dimensional array of 12 integers, arranged in 3 rows and 4 columns.
- A multidimensional array can be visualized as an array of arrays. For example, `A[3][4]` can be seen as an array of 3 elements, each of which is an array of 4 elements.
- A multidimensional array can be accessed or modified by using its name and multiple indices. For example, `A[1][2]` refers to the element in the second row and the third column of the array `A`.
- A multidimensional array can be declared by specifying its name, data type and sizes of each dimension. For example, `int A[3][4][5]` declares a three-dimensional array of 60 integers, arranged in 3 planes, each of which has 4 rows and 5 columns.
- A multidimensional array can be initialized by assigning values to its elements in a nested manner. For example, `A[0][0][0] = 1` assigns the value 1 to the first element of the first row of the first plane of the array `A`.
- A multidimensional array can be traversed by using nested loops that iterate over its elements. For example, `for (i = 0; i < 3; i++) { for (j = 0; j < 4; j++) { for (k = 0; k < 5; k++) { print(A[i][j][k]); } } }` prints all the elements of the array `A`.

## Representation of Arrays: Row Major Order and Column Major Order

- The **representation of arrays** refers to the way the elements of an array are stored in the memory.
- There are two common ways of representing arrays: **row major order** and **column major order**.
- In **row major order**, the elements of an array are stored row by row, starting from the first row. For example, the elements of the two-dimensional array `A[3][4]` are stored as `A[0][0],