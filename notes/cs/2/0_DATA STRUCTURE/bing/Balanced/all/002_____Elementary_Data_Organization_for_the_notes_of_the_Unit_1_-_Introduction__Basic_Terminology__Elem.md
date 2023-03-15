# Elementary Data Organization

## Basic Terminology

- Data: A collection of facts or values that can be processed by a computer.
- Data structure: A way of organizing and storing data in a computer memory or disk, such that it can be accessed and modified efficiently.
- Data type: A classification of data that specifies the possible values, operations and representation of the data.
- Primitive data type: A data type that is predefined by the programming language, such as int, char, float, etc.
- Derived data type: A data type that is defined by the programmer using primitive data types or other derived data types, such as array, structure, union, etc.
- Abstract data type (ADT): A data type that is defined by a set of operations and a mathematical model, but not by its implementation. For example, stack, queue, list, etc.

## Elementary Data Organization

- Data item: A single unit of data that has a value and a type.
- Data element: A group of data items that are logically related and can be accessed by a single name. For example, a record, a structure, etc.
- Data object: A collection of data elements that share a common structure and behavior. For example, an array, a list, etc.
- Data structure: A data object that supports a set of operations that can be performed on it. For example, a stack, a queue, etc.

## Built in Data Types in C

- C is a low-level programming language that provides a set of built in data types for storing and manipulating data.
- The built in data types in C are:

  - int: An integer data type that can store whole numbers in the range of -32768 to 32767 (16 bits) or -2147483648 to 2147483647 (32 bits), depending on the compiler and the platform.
  - char: A character data type that can store a single character or a byte (8 bits) of data. It can be used to store ASCII characters, such as 'A', 'a', '0', etc.
  - float: A floating-point data type that can store real numbers with a decimal point, such as 3.14, -0.5, etc. It can store up to 6 digits of precision (32 bits).
  - double: A double-precision floating-point data type that can store real numbers with a higher precision than float. It can store up to 15 digits of precision (64 bits).
  - void: A special data type that indicates the absence of any data. It can be used to specify the return type of a function that does not return any value, or the type of a pointer that can point to any data type.

- C also allows the programmer to define derived data types using the built in data types, such as:

  - array: A collection of data items of the same type that are stored in a contiguous memory location and can be accessed by an index. For example, int a[10] declares an array of 10 integers.
  - structure: A collection of data items of different types that are grouped together under a single name. For example, struct student {int roll; char name[20]; float marks;} declares a structure that can store the information of a student.
  - union: A collection of data items of different types that share the same memory location and can be accessed by a single name. For example, union data {int i; char c; float f;} declares a union that can store an integer, a character or a float value at a time.
  - pointer: A variable that can store the address of another variable or data item. For example, int *p declares a pointer that can point to an integer variable.
  - enum: A user-defined data type that can store a set of named constants. For example, enum week {SUN, MON, TUE, WED, THU, FRI, SAT} declares an enumeration that can store the values of the days of the week.

## Algorithm

- An algorithm is a finite set of instructions or steps that can be followed to solve a problem or perform a task.
- An algorithm has the following characteristics:

  - Input: An algorithm may take zero or more inputs from the user or from another source.
  - Output: An algorithm must produce one or more outputs that are the solution to the problem or the result of the task.
  - Definiteness: An algorithm must have clear and unambiguous instructions that can be executed in a finite amount of time.
  - Finiteness: An algorithm must terminate after a finite number of steps and produce the output.
  - Effectiveness: An algorithm must be feasible and practical to implement using