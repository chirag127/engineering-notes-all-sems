## Unit 4 - C++ Basics

This unit covers the following topics:

- The structure and syntax of a C++ program
- The basic data types and variables in C++
- The input and output operations using cin and cout
- The arithmetic and logical operators in C++
- The control structures for selection and repetition
- The use of functions and parameters
- The concept of scope and lifetime of variables
- The use of arrays and strings

### The structure and syntax of a C++ program

- A C++ program consists of one or more source files, which are text files that contain the code written by the programmer.
- A source file has the extension .cpp and can include other files using the #include directive.
- A C++ program starts with the main function, which is the entry point of the program. The main function has the following syntax:

```cpp
int main()
{
  // statements
  return 0;
}
```

- The statements in the main function are executed sequentially, from top to bottom. The return 0 statement indicates the successful termination of the program.
- A statement is a complete instruction that performs some action. A statement usually ends with a semicolon (;).
- A comment is a piece of text that is ignored by the compiler and is used to explain or document the code. A comment can be either a single-line comment, which starts with // and ends at the end of the line, or a multi-line comment, which starts with /* and ends with */.
- A C++ program can also define other functions, which are subprograms that perform a specific task. A function has a name, a list of parameters, a return type, and a body. The syntax of a function definition is:

```cpp
return_type function_name(parameter_list)
{
  // statements
  return value;
}
```

- A function can be called by using its name and passing the arguments that match the parameters. The function returns a value of the specified return type.
- A function can be declared before it is defined, using a function prototype, which specifies the name, the parameters, and the return type of the function, but not the body. The syntax of a function prototype is:

```cpp
return_type function_name(parameter_list);
```

- A function prototype allows the compiler to check the validity of the function calls and the function definition. A function prototype should be placed before the first call to the function or in a header file that is included by the source file.