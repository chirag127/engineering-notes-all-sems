### Components of C Language

C language is a structured programming language that consists of various components, such as:

- Standard I/O in C
- Fundamental Data types
- Variables and Memory Locations
- Storage Classes

#### Standard I/O in C

Standard I/O in C refers to the input and output operations that are performed using the standard library functions defined in the header file `<stdio.h>`. Some of the common standard I/O functions are:

- `printf()` : This function is used to print formatted output to the standard output device, usually the screen.
- `scanf()` : This function is used to read formatted input from the standard input device, usually the keyboard.
- `getchar()` : This function is used to read a single character from the standard input device.
- `putchar()` : This function is used to write a single character to the standard output device.
- `gets()` : This function is used to read a string of characters from the standard input device until a newline character is encountered.
- `puts()` : This function is used to write a string of characters to the standard output device followed by a newline character.

#### Fundamental Data types

Fundamental data types are the basic data types that are supported by C language. They are used to store different kinds of values, such as numbers, characters, and logical values. Some of the fundamental data types are:

- `int` : This data type is used to store integer values, such as 1, -5, 0, etc. The size of an `int` is usually 4 bytes, and the range of values is from -2,147,483,648 to 2,147,483,647.
- `char` : This data type is used to store character values, such as 'a', 'Z', '$', etc. The size of a `char` is 1 byte, and the range of values is from -128 to 127.
- `float` : This data type is used to store floating-point values, such as 3.14, -0.5, 1.0e-6, etc. The size of a `float` is usually 4 bytes, and the range of values is from 1.2e-38 to 3.4e38.
- `double` : This data type is used to store double-precision floating-point values, such as 3.14159, -1.23e-10, 6.022e23, etc. The size of a `double` is usually 8 bytes, and the range of values is from 2.3e-308 to 1.7e308.
- `void` : This data type is used to indicate the absence of any data type. It is mainly used to specify the return type of a function that does not return any value, or to declare a pointer that can point to any type of data.

#### Variables and Memory Locations

Variables are the names given to the memory locations that are used to store data values. Variables have three attributes: name, type, and value. The name of a variable is a sequence of letters, digits, and underscores that starts with a letter or an underscore. The type of a variable determines the size and range of values that can be stored in it. The value of a variable is the data that is stored in it at any point of time.

Memory locations are the physical addresses of the memory cells that are allocated to store data values. Memory locations are represented by hexadecimal numbers, such as 0x1234, 0xFFFF, etc. Each memory location can store one byte of data, and the size of a variable is the number of memory locations that are allocated to it.

#### Storage Classes

Storage classes are the keywords that are used to specify the scope, visibility, and lifetime of variables and functions. Scope refers to the region of the program where a variable or function can be accessed. Visibility refers to the ability of a variable or function to be accessed by other parts of the program. Lifetime refers to the duration for which a variable or function exists in the memory. Some of the storage classes are:

- `auto` : This is the default storage class for local variables that are declared inside a function or a block. The scope and visibility of `auto` variables are limited to the function or block where they are declared. The lifetime of `auto` variables is till the end of the function or block where they are declared.
- `extern` : This storage class is used to declare global variables that are defined in another file or outside the current function or block. The scope and visibility of `extern` variables are throughout the program. The lifetime of `extern` variables is till the end of the program.