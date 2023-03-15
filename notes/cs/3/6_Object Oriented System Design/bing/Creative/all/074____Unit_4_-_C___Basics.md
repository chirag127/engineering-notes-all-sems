## Unit 4 - C++ Basics

- C++ is a general-purpose, object-oriented, compiled programming language that supports multiple paradigms such as procedural, generic, and functional programming.
- C++ is an extension of the C language, which means that most of the syntax and features of C are also valid in C++. However, C++ also introduces new concepts and keywords that are not present in C, such as classes, inheritance, polymorphism, templates, exceptions, and STL (Standard Template Library).
- C++ programs consist of one or more source files, which are text files that contain the code written by the programmer. The source files have the extension `.cpp` or `.cxx`. The source files are compiled by a compiler, which is a program that translates the code into executable machine code. The executable file has the extension `.exe` on Windows or no extension on Linux or Mac OS.
- A C++ program can also use header files, which are text files that contain declarations of functions, classes, variables, constants, and macros that are used by the source files. The header files have the extension `.h` or `.hpp`. The header files are not compiled by themselves, but are included by the source files using the `#include` directive. For example, `#include <iostream>` includes the header file `iostream`, which provides input and output facilities for C++ programs.
- A C++ program starts its execution from the `main` function, which is a special function that is defined by the programmer. The `main` function can take arguments from the command line, which are passed as an array of strings (`char* argv[]`) and the number of arguments (`int argc`). The `main` function can also return a value to the operating system, which is usually 0 for successful execution or a non-zero value for an error. The `main` function has the following syntax:

```cpp
int main(int argc, char* argv[])
{
    // code
    return 0;
}
```

- A C++ program can use various types of data, such as integers, floating-point numbers, characters, strings, booleans, arrays, pointers, references, and user-defined types. Each type of data has a name, a size, a range of values, and a set of operations that can be performed on it. For example, an `int` is a type of data that represents a whole number, has a size of 4 bytes, a range of values from -2147483648 to 2147483647, and can be used for arithmetic, comparison, and bitwise operations.
- A C++ program can also define variables, which are named locations in memory that store data of a specific type. A variable has a name, a type, a value, and a scope. The name is a sequence of letters, digits, and underscores that starts with a letter or an underscore. The type is the data type of the variable, which determines its size, range, and operations. The value is the data that is stored in the variable, which can be assigned, modified, or retrieved by the program. The scope is the part of the program where the variable is visible and accessible, which depends on where and how the variable is declared. For example, the following code declares a variable named `x` of type `int` with an initial value of 10 and a scope that is the entire program:

```cpp
int x = 10; // global variable
```

- A C++ program can also define constants, which are named values that cannot be changed by the program. A constant has a name, a type, and a value. The name is a sequence of letters, digits, and underscores that starts with a letter or an underscore. The type is the data type of the constant, which determines its size, range, and operations. The value is the data that is assigned to the constant, which can be a literal value, an expression, or a macro. A constant can be declared using the `const` keyword or the `#define` directive. For example, the following code declares a constant named `PI` of type `double` with a value of 3.14159 using the `const` keyword:

```cpp
const double PI = 3.14159; // constant variable
```

- A C++ program can also define functions, which are named blocks of code that perform a specific task and can be reused by the program. A function has a name, a return type, a parameter list, and a body. The name is a sequence of letters, digits, and underscores that starts with a letter or an underscore. The return type is the data type of the value that the function returns to the