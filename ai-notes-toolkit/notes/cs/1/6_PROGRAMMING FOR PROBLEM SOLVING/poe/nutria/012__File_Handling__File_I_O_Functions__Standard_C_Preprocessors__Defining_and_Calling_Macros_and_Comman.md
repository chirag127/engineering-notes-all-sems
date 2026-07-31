
### File Handling: File I/O Functions

File I/O functions are used to perform operations on files such as opening, reading, writing, and closing them. These functions are defined in the `stdio.h` header file.

- `fopen()`: This function is used to open a file. It takes two arguments: the name of the file and the mode in which the file is to be opened (read, write, append, etc.).
- `fclose()`: This function is used to close an open file. It takes one argument: the file pointer.
- `fgetc()`: This function is used to read a single character from a file. It takes one argument: the file pointer.
- `fputc()`: This function is used to write a single character to a file. It takes two arguments: the character to be written and the file pointer.
- `fread()`: This function is used to read a block of data from a file. It takes four arguments: the pointer to the buffer where the data is to be stored, the size of each element, the number of elements, and the file pointer.
- `fwrite()`: This function is used to write a block of data to a file. It takes four arguments: the pointer to the buffer containing the data, the size of each element, the number of elements, and the file pointer.

### Standard C Preprocessors

C preprocessors are used to modify the source code before it is compiled. They are invoked by the compiler and can be used to define constants, macros, and include files.

- `#define`: This directive is used to define constants and macros.
- `#include`: This directive is used to include other source files.
- `#ifdef`: This directive is used to check if a macro is defined.
- `#ifndef`: This directive is used to check if a macro is not defined.
- `#undef`: This directive is used to undefine a macro.

### Defining and Calling Macros

Macros are used to define reusable pieces of code that can be called multiple times. They are defined using the `#define` directive.

To define a macro, use the following syntax:

`#define MACRO_NAME macro_body`

To call a macro, use the following syntax:

`MACRO_NAME(arg1, arg2, ...)`

### Command-Line Arguments

Command-line arguments are used to pass parameters to a program when it is executed. They are passed as strings and can be accessed using the `argv` array. The first argument (`argv[0]`) is the name of the program.