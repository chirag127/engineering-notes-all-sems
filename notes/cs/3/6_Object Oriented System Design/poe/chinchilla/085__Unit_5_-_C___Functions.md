## Unit 5 - C++ Functions

Functions are an integral part of C++ programming language. They are a set of instructions that perform a specific task and return a value. In this unit, we will learn about C++ functions, their types, and how to create and use them in our programs.

### Types of Functions

C++ functions are broadly categorized into two types:

1. **Built-in Functions**: These are pre-defined functions that are provided by the C++ standard library. They perform a specific task and can be used by including the appropriate header files.

2. **User-defined Functions**: These are functions that are created by the programmer to perform a specific task. They can be customized according to the requirements of the program.

### Function Syntax

The syntax of a function in C++ is as follows:

```
return_type function_name(parameter_list) {
   // function body
   return value;
}
```

- `return_type`: It is the data type of the value that the function returns. It can be any valid data type in C++.

- `function_name`: It is the name of the function. It should be unique and meaningful.

- `parameter_list`: It is a list of parameters that the function accepts. It can be empty or can have one or more parameters.

- `function body`: It is the set of instructions that perform a specific task.

- `return value`: It is the value that the function returns. It can be of the same data type as the `return_type`.

### Function Overloading

Function overloading is a feature of C++ that allows a programmer to define more than one function with the same name but different parameter lists. The compiler determines which function to call based on the number and type of arguments passed to it.

### Recursion

Recursion is a technique in which a function calls itself. It is useful when a problem can be broken down into smaller sub-problems that can be solved using the same function. However, care must be taken to ensure that the recursion does not result in an infinite loop.

### Conclusion

Functions are an essential feature of C++ programming language. They allow a programmer to modularize the code and make it more readable and reusable. In this unit, we learned about the types of C++ functions, their syntax, function overloading, and recursion. Understanding these concepts is crucial for writing efficient and effective C++ programs.