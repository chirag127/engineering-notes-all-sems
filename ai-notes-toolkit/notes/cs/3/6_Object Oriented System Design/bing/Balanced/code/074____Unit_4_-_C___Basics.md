## Unit 4 - C++ Basics

This unit covers the following topics:

- The structure and syntax of a C++ program
- The basic data types and variables in C++
- The input and output operations using cin and cout
- The arithmetic and logical operators in C++
- The control structures for selection and repetition
- The use of comments and indentation to improve readability

### The structure and syntax of a C++ program

- A C++ program consists of one or more source files, which have the extension .cpp
- A source file contains a sequence of statements, which are instructions for the computer to execute
- A statement usually ends with a semicolon (;)
- A C++ program must have a main function, which is the starting point of the program execution
- The main function has the following form:

```cpp
int main()
{
    // statements
    return 0;
}
```

- The int keyword indicates that the main function returns an integer value, which is usually 0 to indicate successful termination
- The curly braces ({ and }) enclose the body of the main function, which contains the statements to be executed
- The return statement specifies the value to be returned by the main function
- A C++ program can also have other functions, which are subprograms that perform specific tasks
- A function has a name, a return type, and a list of parameters, which are variables that receive values from the caller
- A function has the following form:

```cpp
return_type function_name(parameter_list)
{
    // statements
    return value;
}
```

- The return_type keyword indicates the type of value that the function returns, which can be int, double, char, string, bool, or void (no value)
- The function_name is an identifier that follows the naming rules of C++
- The parameter_list is a comma-separated list of parameters, each with a type and a name
- The return statement specifies the value to be returned by the function, which must match the return type
- A function can be called by using its name and passing the arguments, which are the values for the parameters
- A function call has the following form:

```cpp
function_name(argument_list);
```

- The argument_list is a comma-separated list of arguments, which must match the types and order of the parameters
- A function can also be defined before or after the main function, or in a separate source file
- A function must be declared before it is used, which means specifying its name, return type, and parameter list
- A function declaration has the following form:

```cpp
return_type function_name(parameter_list);
```

- A function declaration is also called a function prototype, and it is usually placed at the beginning of the source file or in a header file
- A header file is a file that contains declarations of functions, variables, constants, or classes that can be used by other source files
- A header file has the extension .h
- A header file can be included in a source file by using the #include directive, which has the following form:

```cpp
#include "header_file.h"
```

- The header file name is enclosed in double quotes ("") if it is a user-defined header file, or in angle brackets (<>) if it is a system header file
- A system header file is a file that is provided by the C++ standard library or the operating system, and it contains predefined functions, variables, constants, or classes that can be used by any C++ program
- Some examples of system header files are:

```cpp
#include <iostream> // for input and output operations
#include <cmath> // for mathematical functions
#include <string> // for string manipulation
#include <vector> // for dynamic arrays
#include <algorithm> // for sorting and searching algorithms
```

- A C++ program can also use comments, which are notes or explanations that are ignored by the compiler
- Comments can be used to document the purpose, functionality, or logic of the program or its parts
- Comments can also be used to temporarily disable some statements for testing or debugging purposes
- Comments can be single-line or multi-line
- A single-line comment starts with two slashes (//) and ends at the end of the line
- A multi-line comment starts with a slash and an asterisk (/*) and ends with an asterisk and a slash (*/)
- Comments can be nested, which means that a comment can contain another comment
- Some examples of comments are:

```cpp
// This is a single-line comment
/* This is a multi-line comment
   that spans several lines */
/* This is a nested comment
/* This is another comment inside the comment */
*/
```