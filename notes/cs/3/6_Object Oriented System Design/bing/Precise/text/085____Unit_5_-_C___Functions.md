## Unit 5 - C++ Functions

1. **Introduction:** A function is a block of code that performs a specific task. It can be called multiple times from different parts of the program, reducing code repetition and improving code organization.

2. **Function Declaration:** A function must be declared before it can be used. The declaration specifies the function's name, return type, and parameters. For example: `int add(int a, int b);`

3. **Function Definition:** The function definition contains the actual code that is executed when the function is called. It must match the function declaration. For example:
```
int add(int a, int b) {
    return a + b;
}
```

4. **Function Call:** A function is called by using its name followed by the arguments in parentheses. For example: `int result = add(3, 4);`

5. **Return Values:** A function can return a value to the calling code using the `return` keyword. The return type must match the type specified in the function declaration.

6. **Passing Parameters:** Parameters can be passed to a function by value or by reference. Passing by value means that a copy of the argument is passed to the function, while passing by reference means that the function can modify the original argument.

7. **Overloading Functions:** C++ allows multiple functions with the same name but different parameters. This is called function overloading. The compiler determines which function to call based on the arguments provided.

8. **Default Arguments:** A function can have default values for some or all of its parameters. If an argument is not provided when calling the function, the default value is used.

9. **Inline Functions:** An inline function is a function that is expanded in place by the compiler, rather than being called. This can improve performance by reducing the overhead of a function call.

10. **Recursion:** A function can call itself. This is called recursion. Recursive functions must have a base case to prevent infinite recursion.