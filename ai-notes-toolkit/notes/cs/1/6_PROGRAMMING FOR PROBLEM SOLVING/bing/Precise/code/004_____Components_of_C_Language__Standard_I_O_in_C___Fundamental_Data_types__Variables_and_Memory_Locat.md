### Components of C Language

#### Standard I/O in C
- Standard I/O refers to the standard input/output library in C.
- It provides functions for reading and writing data to the standard input and output streams.
- The standard input stream is typically the keyboard, while the standard output stream is typically the screen.
- Some common functions in the standard I/O library include `printf`, `scanf`, `getchar`, and `putchar`.

#### Fundamental Data types
- C has several fundamental data types, including `char`, `int`, `float`, and `double`.
- The `char` data type is used to store characters, while `int` is used to store integers.
- The `float` and `double` data types are used to store floating-point numbers, with `double` providing more precision than `float`.
- The size of these data types can vary depending on the system, but they are generally 1 byte for `char`, 4 bytes for `int`, 4 bytes for `float`, and 8 bytes for `double`.

#### Variables and Memory Locations
- A variable is a named location in memory that can store a value of a particular data type.
- The value of a variable can be changed during the execution of a program.
- The memory location of a variable is determined by the compiler, and the programmer can access the value stored in that location using the variable's name.

#### Storage Classes
- Storage classes in C determine the scope and lifetime of a variable.
- There are four storage classes in C: `auto`, `register`, `static`, and `extern`.
- The `auto` storage class is the default for local variables and specifies that the variable has automatic storage duration.
- The `register` storage class specifies that the variable should be stored in a CPU register if possible, for faster access.
- The `static` storage class specifies that the variable has static storage duration, meaning that it retains its value between function calls.
- The `extern` storage class specifies that the variable is defined in another source file and can be accessed from the current file.