# Elementary Data Organization

## Basic Terminology

- **Data**: Data refers to a value or a set of values that represent some information or facts. For example, the name, age, and height of a person are data.
- **Data item**: Data item refers to a single or a group of values within the data. For example, the name of a person is a data item.
- **Data type**: Data type refers to the category or classification of data items based on their values and operations that can be performed on them. For example, integer, float, char, and string are some data types in C.
- **Built-in data type**: Built-in data type refers to the data type that is predefined and supported by the programming language. For example, int, float, char, and double are some built-in data types in C.
- **Derived data type**: Derived data type refers to the data type that is defined by the programmer using the built-in data types and other data structures. For example, array, structure, union, and pointer are some derived data types in C.
- **Data structure**: Data structure refers to a specialized format for organizing and storing data. Data structure is designed to suit a specific purpose and to facilitate the access and manipulation of data. For example, array, file, record, table, tree, and graph are some data structures.
- **Abstract data type (ADT)**: Abstract data type refers to a logical or mathematical model for a particular organization of data and the operations that can be performed on it. ADT hides the implementation details of the data structure and provides an interface to the user. For example, stack, queue, list, and set are some ADTs.

## Elementary Data Organization

- **Elementary data organization** refers to the basic ways of organizing and storing data in memory. It includes the following concepts:
  - **Bit**: Bit is the smallest unit of data that can be stored in memory. It can have only two values: 0 or 1.
  - **Byte**: Byte is a group of 8 bits. It can store one character or a small integer value.
  - **Word**: Word is a group of bytes. The size of a word depends on the architecture of the computer. It can be 16 bits, 32 bits, or 64 bits. It can store a large integer value or a floating-point value.
  - **Address**: Address is a unique identifier for a location in memory. It is usually represented by a hexadecimal number. For example, 0x1234 is an address.
  - **Pointer**: Pointer is a variable that stores the address of another variable or data item. It can be used to access or modify the data item indirectly. For example, int *p = &x; is a pointer declaration in C, where p is a pointer to an integer variable x.
  - **Array**: Array is a derived data type that stores a collection of data items of the same type in a contiguous block of memory. Each data item can be accessed by its index or position in the array. For example, int a[10]; is an array declaration in C, where a is an array of 10 integers.
  - **Structure**: Structure is a derived data type that stores a collection of data items of different types in a single unit. Each data item can be accessed by its name or member. For example, struct student {char name[20]; int roll; float marks;}; is a structure declaration in C, where student is a structure that contains three data items: name, roll, and marks.
  - **Union**: Union is a derived data type that stores a collection of data items of different types in a single unit. However, only one data item can be stored at a time. The size of the union is equal to the size of the largest data item. For example, union data {int x; float y; char z;}; is a union declaration in C, where data is a union that can store either an integer, a float, or a character.