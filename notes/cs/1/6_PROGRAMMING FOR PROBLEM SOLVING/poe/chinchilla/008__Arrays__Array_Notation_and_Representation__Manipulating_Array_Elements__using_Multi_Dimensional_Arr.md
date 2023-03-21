### Arrays

Arrays are a collection of data items of the same type, stored in contiguous memory locations. Arrays provide a convenient way to store and manipulate large amounts of data.

#### Array Notation and Representation

An array is declared using the following syntax:

```
data_type array_name[array_size];
```

Here, `data_type` is the type of data to be stored in the array, `array_name` is the name of the array, and `array_size` is the number of elements in the array. The index of the first element in the array is 0.

#### Manipulating Array Elements

Arrays can be accessed and manipulated using their index. The syntax for accessing an element in an array is as follows:

```
array_name[index];
```

To assign a value to an element in an array, use the following syntax:

```
array_name[index] = value;
```

#### Using Multi Dimensional Arrays

Multi dimensional arrays are arrays that have more than one dimension. They are often used to represent matrices or tables. The syntax for declaring a multi dimensional array is as follows:

```
data_type array_name[size1][size2]...[sizeN];
```

Here, `size1`, `size2`, ..., `sizeN` are the sizes of each dimension of the array. The first dimension corresponds to the rows, and the second dimension corresponds to the columns.

#### Character Arrays and Strings

Character arrays are arrays of characters. They are often used to represent strings. Strings are sequences of characters terminated by a null character (`'\0'`). The syntax for declaring a character array is as follows:

```
char array_name[size];
```

Here, `size` is the size of the array.

#### Structure, union, Enumerated Data types

Structures, unions, and enumerated data types are user-defined data types in C programming. Structures are used to group related data items of different types into a single entity. Unions are similar to structures, but they only allow one member to be active at a time. Enumerated data types are used to define a set of named constants.

The syntax for declaring a structure is as follows:

```
struct structure_name {
    type1 member1;
    type2 member2;
    ...
    typeN memberN;
};
```

Here, `structure_name` is the name of the structure, and `member1`, `member2`, ..., `memberN` are the members of the structure.

The syntax for declaring a union is as follows:

```
union union_name {
    type1 member1;
    type2 member2;
    ...
    typeN memberN;
};
```

Here, `union_name` is the name of the union, and `member1`, `member2`, ..., `memberN` are the members of the union.

The syntax for declaring an enumerated data type is as follows:

```
enum enum_name {
    constant1,
    constant2,
    ...
    constantN
};
```

Here, `enum_name` is the name of the enumerated data type, and `constant1`, `constant2`, ..., `constantN` are the named constants.

#### Array of Structures

An array of structures is an array in which each element is a structure. The syntax for declaring an array of structures is as follows:

```
struct structure_name array_name[size];
```

Here, `structure_name` is the name of the structure, `array_name` is the name of the array, and `size` is the size of the array.

#### Passing Arrays to Functions

Arrays can be passed to functions as arguments. When an array is passed to a function, a pointer to the first element of the array is passed. The syntax for passing an array to a function is as follows:

```
return_type function_name(data_type array_name[], int size) {
    ...
}
```

Here, `return_type` is the type of data returned by the function, `function_name` is the name of the function, `data_type` is the type of data stored in the array, `array_name` is the name of the array, and `size` is the size of the array.