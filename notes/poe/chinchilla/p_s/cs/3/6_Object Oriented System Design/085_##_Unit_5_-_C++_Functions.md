## Unit 5 - C++ Functions

Functions are an essential feature of programming languages, and C++ is no exception. A function is a block of code that performs a specific task. It is like a subprogram that can be called from any part of the program. 

### Syntax of a Function

A function in C++ has the following syntax:

```
return_type function_name(parameter list) {
   // Body of the function
   return value;
}
```

- The return type is the data type of the value returned by the function. If the function does not return any value, the return type is void.
- The function name is a unique identifier for the function.
- The parameter list contains the data types and names of the parameters passed to the function. If the function does not take any parameters, the parameter list is empty.
- The body of the function contains the statements that are executed when the function is called.
- The return statement returns a value from the function.

### Types of Functions

There are two types of functions in C++:

1. Library functions - These are the functions that are provided by the C++ library. They are pre-defined and can be used directly in the program. For example, the `printf()` function is a library function.

2. User-defined functions - These are the functions that are created by the user. They are defined by the user and can be used in the program. 

### Advantages of Functions

Functions have the following advantages:

- Code reuse: Functions allow you to reuse code, which reduces the amount of code you need to write.

- Modular programming: Functions allow you to break up a large program into smaller, more manageable modules.

- Abstraction: Functions allow you to hide the details of how a particular task is performed, which makes the code more readable and easier to understand.

### Disadvantages of Functions

Functions have the following disadvantages:

- Overhead: Functions have some overhead in terms of memory usage and CPU time.

- Complexity: Functions can make a program more complex if they are not designed properly.

### Examples of Functions

Here is an example of a user-defined function that adds two numbers:

```
int add(int x, int y) {
   int sum = x + y;
   return sum;
}
```

Here is an example of calling the `add()` function:

```
int a = 5;
int b = 10;
int c = add(a, b);
```

In this example, the `add()` function takes two integer parameters and returns their sum.

### Applications of Functions

Functions are used in a variety of applications, including:

- Mathematical calculations
- Input/output operations
- File handling
- Database operations

Functions are an essential part of programming in C++. Understanding how to create and use functions is critical to becoming a proficient C++ programmer.