## Unit 5 - C++ Functions

1. **Introduction to Functions:** A function is a block of code that performs a specific task. It can be called multiple times from different parts of the program, reducing code repetition and improving code organization.

2. **Function Declaration and Definition:** A function must be declared before it is used in a program. The declaration specifies the function's name, return type, and parameters. The definition provides the actual code that is executed when the function is called.

3. **Function Parameters and Arguments:** Parameters are the variables that are listed in the function declaration. Arguments are the values that are passed to the function when it is called. The number and type of arguments must match the number and type of parameters.

4. **Return Values:** A function can return a value to the calling code using the `return` statement. The return type must match the type specified in the function declaration.

5. **Function Overloading:** C++ allows multiple functions with the same name but different parameters. This is known as function overloading. The compiler determines which function to call based on the arguments passed.

6. **Default Arguments:** Default arguments can be specified for function parameters. If a value is not provided for a parameter with a default argument when the function is called, the default value is used.

7. **Pass by Value and Pass by Reference:** When a function is called, the arguments can be passed by value or by reference. Pass by value means that a copy of the argument is passed to the function. Pass by reference means that a reference to the argument is passed, allowing the function to modify the original value.

8. **Recursion:** A function can call itself, either directly or indirectly. This is known as recursion. Recursive functions must have a base case to prevent infinite recursion.

9. **Function Templates:** Function templates allow the creation of generic functions that can operate on different data types. The data type is specified when the function is called.

10. **Lambda Functions:** Lambda functions are anonymous functions that can be defined and used inline. They are often used with algorithms that take a function as an argument.