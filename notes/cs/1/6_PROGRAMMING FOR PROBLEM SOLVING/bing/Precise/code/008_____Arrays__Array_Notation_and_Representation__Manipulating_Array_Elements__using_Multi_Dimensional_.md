### Arrays: Array Notation and Representation, Manipulating Array Elements, using Multi Dimensional Arrays. Character Arrays and Strings, Structure, union, Enumerated Data types, Array of Structures, Passing Arrays to Functions.

An array is a collection of elements of the same data type, stored in contiguous memory locations. The elements of an array can be accessed by their index, which is an integer value that starts from 0.

#### Array Notation and Representation
- An array is declared using the following syntax: `data_type array_name[size];`
- The size of the array must be a constant integer value.
- The elements of the array can be accessed using the following syntax: `array_name[index]`
- The index of the first element of the array is 0, and the index of the last element is size-1.

#### Manipulating Array Elements
- The elements of an array can be assigned values using the following syntax: `array_name[index] = value;`
- The elements of an array can be accessed and manipulated using a loop. For example, to print all the elements of an array, we can use the following code:
```
for(int i=0; i<size; i++)
{
    printf("%d ", array_name[i]);
}
```

#### Using Multi Dimensional Arrays
- A multi dimensional array is an array of arrays.
- A two dimensional array can be declared using the following syntax: `data_type array_name[rows][columns];`
- The elements of a two dimensional array can be accessed using the following syntax: `array_name[row_index][column_index]`

#### Character Arrays and Strings
- A character array is an array of characters.
- A string is a character array that is terminated by a null character (`'\0'`).
- A string can be declared and initialized using the following syntax: `char string_name[] = "string value";`

#### Structure, union, Enumerated Data types
- A structure is a collection of variables of different data types, grouped together under a single name.
- A structure can be declared using the `struct` keyword, followed by the structure name and the variables enclosed in curly braces.
- A union is similar to a structure, but all the variables share the same memory location.
- An enumerated data type is a user-defined data type that consists of a set of named integer constants.

#### Array of Structures
- An array of structures is an array where each element is a structure.
- An array of structures can be declared using the following syntax: `struct structure_name array_name[size];`

#### Passing Arrays to Functions
- An array can be passed to a function as an argument.
- When an array is passed to a function, the function receives a pointer to the first element of the array.
- The size of the array must also be passed to the function, as the function cannot determine the size of the array from the pointer alone.
