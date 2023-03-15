### Arrays: Array Notation and Representation, Manipulating Array Elements, using Multi Dimensional Arrays. Character Arrays and Strings, Structure, union, Enumerated Data types, Array of Structures, Passing Arrays to Functions.

An array is a collection of elements of the same data type, stored in contiguous memory locations. The elements of an array can be accessed by their index, which is an integer value that starts from 0.

#### Array Notation and Representation
- An array is declared by specifying its data type, followed by its name and the size of the array in square brackets.
- For example, to declare an integer array of size 5: `int myArray[5];`
- The elements of the array can be accessed using the array name and the index of the element in square brackets.
- For example, to access the first element of the array: `myArray[0]`

#### Manipulating Array Elements
- The elements of an array can be assigned values using the assignment operator (=).
- For example, to assign the value 10 to the first element of the array: `myArray[0] = 10;`
- The elements of an array can also be accessed and manipulated using loops.
- For example, to assign the values 1 to 5 to the elements of the array:
```
for (int i = 0; i < 5; i++) {
    myArray[i] = i + 1;
}
```

#### Using Multi Dimensional Arrays
- Arrays can have more than one dimension, such as a two-dimensional array (matrix) or a three-dimensional array (cube).
- A two-dimensional array is declared by specifying the data type, followed by the name of the array and the size of the array in two sets of square brackets.
- For example, to declare a two-dimensional integer array of size 3x3: `int myArray[3][3];`
- The elements of a two-dimensional array can be accessed using the array name and the indices of the element in square brackets.
- For example, to access the element in the first row and first column of the array: `myArray[0][0]`

#### Character Arrays and Strings
- A character array is an array of characters, which can be used to store and manipulate strings.
- A string is a sequence of characters, terminated by a null character (`'\0'`).
- A character array can be declared and initialized using a string literal.
- For example, to declare and initialize a character array with the string "Hello": `char myString[] = "Hello";`
- The elements of a character array can be accessed and manipulated in the same way as any other array.

#### Structure, union, Enumerated Data types
- A structure is a composite data type that groups together variables of different data types under a single name.
- A structure is declared using the `struct` keyword, followed by the name of the structure and the variables it contains in curly braces.
- For example, to declare a structure to represent a point in two-dimensional space:
```
struct Point {
    int x;
    int y;
};
```
- A union is similar to a structure, but all of its members share the same memory location.
- A union is declared using the `union` keyword, followed by the name of the union and the variables it contains in curly braces.
- For example, to declare a union to represent a value that can be either an integer or a float:
```
union IntOrFloat {
    int intValue;
    float floatValue;
};
```
- An enumerated data type is a data type consisting of a set of named values.
- An enumerated data type is declared using the `enum` keyword, followed by the name of the enumerated data type and the named values it contains in curly braces.
- For example, to declare an enumerated data type to represent the days of the week:
```
enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
};
```

#### Array of Structures
- An array of structures is an array where each element is a structure of the same type.
- An array of structures is declared in the same way as any other array, by specifying the data type (in this case, the structure type), followed by the name of the array and the size of the array in square brackets.
- For example, to declare an array of `Point` structures of size 5: `struct Point myPoints[5];`
- The elements of an array of structures can be accessed and manipulated in the same way as any other array.

#### Passing Arrays to Functions
- Arrays