### Components of C Language

#### Standard I/O in C
- C language provides a set of built-in functions to perform input and output operations.
- These functions are part of the standard library and are declared in the header file `stdio.h`.
- Some common standard I/O functions include `printf()`, `scanf()`, `getchar()`, `putchar()`, `gets()`, and `puts()`.

#### Fundamental Data types
- C language has several fundamental data types, including `int`, `char`, `float`, and `double`.
- These data types define the type of data that a variable can hold, as well as the amount of memory that will be allocated for the variable.
- The size of these data types can vary depending on the system and compiler, but typically an `int` is 4 bytes, a `char` is 1 byte, a `float` is 4 bytes, and a `double` is 8 bytes.

#### Variables and Memory Locations
- A variable is a named location in memory that can store a value of a specific data type.
- The value of a variable can be changed during the execution of a program.
- Each variable has a unique memory address, which is used to access and manipulate the value stored in the variable.

#### Storage Classes
- Storage classes in C language define the scope and lifetime of a variable.
- There are four storage classes in C: `auto`, `register`, `static`, and `extern`.
- The `auto` storage class is the default for local variables and specifies that the variable has automatic storage duration.
- The `register` storage class is used to request that the compiler store the variable in a CPU register for faster access.
- The `static` storage class specifies that the variable has static storage duration, meaning that it is allocated for the lifetime of the program.
- The `extern` storage class is used to declare a variable that is defined in another source file. It allows the variable to be accessed across multiple source files.