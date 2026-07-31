### File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments

File handling is the process of manipulating files in a computer system using a programming language. Files are containers that store data in a persistent and organized way. In C, file handling is done using the standard input/output (I/O) library functions.

#### File I/O Functions

Some of the common file I/O functions in C are:

- `fopen()` - opens a file and returns a pointer to the file stream
- `fclose()` - closes a file stream and releases the resources associated with it
- `fread()` - reads a specified number of bytes from a file stream and stores them in a buffer
- `fwrite()` - writes a specified number of bytes from a buffer to a file stream
- `fseek()` - moves the file position indicator to a specified location in a file stream
- `ftell()` - returns the current position of the file position indicator in a file stream
- `feof()` - tests whether the end-of-file indicator is set for a file stream
- `ferror()` - tests whether an error has occurred in a file stream
- `fprintf()` - writes formatted data to a file stream
- `fscanf()` - reads formatted data from a file stream

#### Standard C Preprocessors

Preprocessors are directives that instruct the compiler to perform certain tasks before compiling the source code. Some of the standard C preprocessors are:

- `#include` - inserts the contents of another file into the source code
- `#define` - defines a macro or a constant
- `#undef` - undefines a macro or a constant
- `#if`, `#elif`, `#else`, `#endif` - controls conditional compilation
- `#ifdef`, `#ifndef` - tests whether a macro is defined or not
- `#error` - generates an error message and stops compilation
- `#pragma` - provides additional information or instructions to the compiler

#### Defining and Calling Macros

Macros are symbolic names that represent a piece of code or a constant value. They are defined using the `#define` preprocessor directive. For example:

```c
#define PI 3.14 // defines a constant macro
#define SQUARE(x) ((x) * (x)) // defines a function-like macro
```

Macros are called by using their names in the source code. For example:

```c
double area = PI * SQUARE(radius); // calls the macros PI and SQUARE
```

Macros are useful for avoiding repetition, improving readability, and simplifying maintenance of the code.

#### Command-Line Arguments

Command-line arguments are parameters that are passed to a program when it is executed from the command line. They are stored in an array of strings called `argv`, and the number of arguments is stored in an integer variable called `argc`. For example, if a program is executed as:

```bash
./program arg1 arg2 arg3
```

Then, `argc` will be 4, and `argv` will be:

```c
argv[0] = "./program"
argv[1] = "arg1"
argv[2] = "arg2"
argv[3] = "arg3"
```

Command-line arguments can be accessed and manipulated in the program using the `argv` and `argc` variables. They are useful for passing input data, options, or flags to the program.