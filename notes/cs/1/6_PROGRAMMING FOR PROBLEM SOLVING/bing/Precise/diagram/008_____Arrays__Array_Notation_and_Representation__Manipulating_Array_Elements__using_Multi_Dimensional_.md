### Arrays: Array Notation and Representation, Manipulating Array Elements, using Multi Dimensional Arrays. Character Arrays and Strings, Structure, union, Enumerated Data types, Array of Structures, Passing Arrays to Functions.

An array is a collection of elements of the same data type, stored in contiguous memory locations. The elements of an array can be accessed by their index, which is an integer value starting from 0.

#### Array Notation and Representation
- An array is declared by specifying its data type, followed by its name and the number of elements in square brackets.
- For example, to declare an integer array of size 10: `int myArray[10];`
- The elements of the array can be accessed using the array name and the index of the element in square brackets.
- For example, to access the first element of the array: `myArray[0]`

#### Manipulating Array Elements
- The elements of an array can be assigned values using the assignment operator (=).
- For example, to assign the value 5 to the first element of the array: `myArray[0] = 5;`
- The elements of an array can also be accessed and manipulated using loops.
- For example, to assign the values 0 to 9 to the elements of the array:
```
for (int i = 0; i < 10; i++) {
    myArray[i] = i;
}
```

#### Using Multi Dimensional Arrays
- Arrays can have more than one dimension, such as a two-dimensional array representing a matrix.
- A two-dimensional array is declared by specifying the data type, followed by the array name and the number of rows and columns in square brackets.
- For example, to declare a two-dimensional integer array of size 3x3: `int myArray[3][3];`
- The elements of a two-dimensional array can be accessed using the array name and the row and column indices in square brackets.
- For example, to access the element in the first row and first column of the array: `myArray[0][0]`

#### Character Arrays and Strings
- A character array is an array of characters, which can be used to represent a string.
- A string is a sequence of characters, terminated by a null character (`'\0'`).
- A character array can be declared and initialized using a string literal.
- For example, to declare and initialize a character array with the string "Hello": `char myString[] = "Hello";`
- The elements of a character array can be accessed and manipulated in the same way as any other array.

#### Structure, union, Enumerated Data types
- A structure is a composite data type that groups together variables of different data types under a single name.
- A structure is declared using the `struct` keyword, followed by the structure name and the variables within curly braces.
- For example, to declare a structure representing a point in two-dimensional space:
```
struct Point {
    int x;
    int y;
};
```
- A union is similar to a structure, but all of its members share the same memory location.
- A union is declared using the `union` keyword, followed by the union name and the variables within curly braces.
- For example, to declare a union representing a data value that can be either an integer or a float:
```
union Data {
    int intValue;
    float floatValue;
};
```
- An enumerated data type is a data type consisting of a set of named values.
- An enumerated data type is declared using the `enum` keyword, followed by the enumeration name and the values within curly braces.
- For example, to declare an enumerated data type representing the days of the week:
```
enum Weekday {
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
- An array of structures is declared in the same way as any other array, by specifying the data type (in this case, the structure type), followed by the array name and the number of elements in square brackets.
- For example, to declare an array of 10 `Point` structures: `struct Point points[10];`
- The elements of an array of structures can be accessed and manipulated in the same way as any other array.

#### Passing Arrays to Functions
- Arrays can be passed to functions as arguments.
- When an array is passed to a function, the function receives a pointer to the first element of the array.
- The size of the array is not passed to