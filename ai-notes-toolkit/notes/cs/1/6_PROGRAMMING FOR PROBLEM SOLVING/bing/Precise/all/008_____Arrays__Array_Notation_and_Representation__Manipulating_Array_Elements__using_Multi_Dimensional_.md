# Arrays: Array Notation and Representation, Manipulating Array Elements, using Multi Dimensional Arrays. Character Arrays and Strings, Structure, union, Enumerated Data types, Array of Structures, Passing Arrays to Functions.

## Array Notation and Representation
- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- The elements of an array are accessed using an index, which starts from 0.
- The notation for declaring an array is `data_type array_name[array_size]`.
- For example, to declare an integer array of size 5, we write `int arr[5]`.

## Manipulating Array Elements
- Array elements can be accessed and manipulated using the index.
- For example, to access the first element of the array `arr`, we write `arr[0]`.
- To assign a value to the third element of the array, we write `arr[2] = value`.

## Using Multi Dimensional Arrays
- Multi dimensional arrays are arrays of arrays.
- The most common multi dimensional array is the two dimensional array, which can be thought of as a table with rows and columns.
- The notation for declaring a two dimensional array is `data_type array_name[rows][columns]`.
- For example, to declare a two dimensional integer array of 3 rows and 4 columns, we write `int arr[3][4]`.

## Character Arrays and Strings
- A character array is an array of characters.
- A string is a sequence of characters, stored in a character array.
- The notation for declaring a character array is `char array_name[array_size]`.
- For example, to declare a character array of size 6, we write `char arr[6]`.
- To initialize a character array with a string, we write `char arr[] = "string"`.

## Structure, union, Enumerated Data types
- A structure is a collection of variables of different data types, grouped together under a single name.
- The notation for declaring a structure is `struct structure_name {data_type1 variable1; data_type2 variable2; ...};`.
- A union is similar to a structure, but all its members share the same memory location.
- The notation for declaring a union is `union union_name {data_type1 variable1; data_type2 variable2; ...};`.
- An enumerated data type is a user-defined data type, where the values are restricted to a fixed set of values.
- The notation for declaring an enumerated data type is `enum enum_name {value1, value2, ...};`.

## Array of Structures
- An array of structures is an array, where each element is a structure.
- The notation for declaring an array of structures is `struct structure_name array_name[array_size]`.
- For example, to declare an array of 5 structures of type `struct student`, we write `struct student arr[5]`.

## Passing Arrays to Functions
- Arrays can be passed to functions as arguments.
- When an array is passed to a function, the function receives a pointer to the first element of the array.
- The notation for passing an array to a function is `function_name(array_name)`.
- For example, to pass the array `arr` to the function `func`, we write `func(arr)`.