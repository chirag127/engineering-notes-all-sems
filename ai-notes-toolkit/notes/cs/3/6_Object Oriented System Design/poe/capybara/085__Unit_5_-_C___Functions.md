## Unit 5 - C++ Functions

Functions are an essential part of programming in C++. They allow you to break down a program into smaller, more manageable pieces of code that can be reused throughout the program. Here are some important points to keep in mind when working with C++ functions:

- **Function Declaration:** A function declaration tells the compiler about the function name, return type, and parameters. It is defined using a function prototype, which has the syntax `return_type function_name(parameter_list);`.

- **Function Definition:** A function definition provides the actual implementation of the function. It includes the function body, which contains the statements that are executed when the function is called. The syntax for a function definition is `return_type function_name(parameter_list) { function_body }`.

- **Function Parameters:** Parameters are input values that are passed to a function when it is called. They are enclosed in parentheses after the function name in both the function declaration and definition. You can pass parameters by value, reference, or pointer.

- **Return Type:** The return type specifies the type of value that the function returns. If the function does not return a value, its return type is `void`.

- **Function Overloading:** Function overloading allows you to create multiple functions with the same name but different parameter lists. The compiler determines which function to call based on the number, order, and types of the arguments passed to it.

- **Recursion:** Recursion is a technique where a function calls itself. It is useful for solving problems that can be broken down into smaller sub-problems. However, recursion can be inefficient and may cause stack overflow if not used properly.

- **Inline Functions:** Inline functions are small functions that are inserted directly into the code at the point where they are called. They are used to improve program performance by reducing the overhead of function calls.

- **Function Templates:** Function templates allow you to create a generic function that can be used with different data types. The syntax for a function template is `template <class T> return_type function_name(T parameter_list) { function_body }`.

By mastering the concepts of C++ functions, you can write more efficient, reusable, and maintainable code.