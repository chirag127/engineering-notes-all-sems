# Unit 4 - Functions: Introduction, Types of Functions, Functions with Array, Passing Parameters to Functions, Call by Value, Call by Reference, Recursive Functions.

## Introduction
- A function is a block of code that performs a specific task or a related task  .
- A function can be used repeatedly throughout a program, making the code more efficient, easier to read, and elegant .
- A function can take in data, process it, and return a result to the main program.
- A function can also perform a task without returning any value, such as printing a message or drawing a shape.
- A function has a name, a list of parameters, and a body that contains the statements to execute.
- A function can be defined by the programmer or built-in by the programming language.
- A function can be called by using its name and passing the arguments that match the parameters.

## Types of Functions
- There are different types of functions depending on the number and type of parameters and the return value.
- Some common types of functions are:
  - **Void functions**: These are functions that do not return any value. They are used to perform a task without expecting a result. For example, a function that prints a message or draws a shape on the screen is a void function.
  - **Value-returning functions**: These are functions that return a value after performing some computation or operation. They are used to get a result from a function that can be used in the main program or another function. For example, a function that calculates the area of a circle or the factorial of a number is a value-returning function.
  - **Parameterless functions**: These are functions that do not take any arguments. They are used to perform a task that does not depend on any input. For example, a function that generates a random number or returns the current time is a parameterless function.
  - **Parameterized functions**: These are functions that take one or more arguments. They are used to perform a task that depends on some input. For example, a function that adds two numbers or checks if a number is prime is a parameterized function.

## Functions with Array
- An array is a collection of data elements of the same type that are stored in contiguous memory locations.
- A function can take an array as a parameter or return an array as a result.
- To pass an array to a function, the name of the array and the size of the array are required.
- To return an array from a function, the function must declare the array as a static or global variable, or use dynamic memory allocation.
- A function can access and modify the elements of an array that is passed as a parameter, as the array is passed by reference (see below).
- A function can perform various operations on an array, such as sorting, searching, reversing, etc.

## Passing Parameters to Functions
- A parameter is a variable that is declared in the function definition and receives the value of the argument that is passed to the function when it is called.
- An argument is a value or an expression that is passed to the function when it is called.
- There are two ways of passing parameters to functions: call by value and call by reference.

## Call by Value
- Call by value is the method of passing parameters to functions where the value of the argument is copied to the parameter.
- In this method, the parameter and the argument are two separate variables that have the same value but different memory locations.
- Any changes made to the parameter inside the function do not affect the argument in the main program.
- Call by value is the default method of passing parameters in most programming languages, such as C, C++, Java, Python, etc.

## Call by Reference
- Call by reference is the method of passing parameters to functions where the address of the argument is copied to the parameter.
- In this method, the parameter and the argument are two different names for the same variable that share the same memory location.
- Any changes made to the parameter inside the function affect the argument in the main program.
- Call by reference is the method of passing parameters for arrays and other complex data types, such as structures, classes, etc.
- Call by reference can also be achieved by using pointers or references in some programming languages, such as C, C++, etc.

## Recursive Functions
- A recursive function is a function that calls itself within its body.
- A recursive function must have a base case that terminates the recursion and a recursive case that reduces the problem to a