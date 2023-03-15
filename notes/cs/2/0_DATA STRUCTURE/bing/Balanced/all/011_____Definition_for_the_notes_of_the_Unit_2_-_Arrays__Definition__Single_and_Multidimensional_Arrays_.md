# Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Arrays: Definition, Single and Multidimensional Arrays

- An array is a collection of homogeneous elements stored in a contiguous memory location for better access and easier calculation by the system.
- An array is a data structure consisting of a collection of elements, each identified by at least one array index or key.
- An array is an assortment of similar types of data, while a list can include dissimilar data values.
- Array elements can be of any type, including an array type.
- Array types are reference types derived from the abstract base type Array.
- All arrays implement IList, and IEnumerable.
- Single-dimensional arrays also implement IList<T> and IEnumerable<T>.
- An array can be declared as follows:

```csharp
// Single-dimensional array
int[] array1 = new int[5];

// Multidimensional array
int[,] array2 = new int[3,4];

// Array of arrays (jagged array)
int[][] array3 = new int[3][];
array3[0] = new int[5];
array3[1] = new int[4];
array3[2] = new int[2];
```

- A single-dimensional array is an array with one dimension, i.e., one index or key to access the elements.
- A multidimensional array is an array with more than one dimension, i.e., multiple indices or keys to access the elements.
- A jagged array is an array of arrays, where each subarray can have a different length.