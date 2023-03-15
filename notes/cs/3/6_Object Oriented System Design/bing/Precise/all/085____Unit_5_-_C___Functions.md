## Unit 5 - C++ Functions

1. **Introduction:** A function is a block of code that performs a specific task. It can be called multiple times from different parts of the program, reducing code repetition and improving code organization.

2. **Function Declaration:** A function must be declared before it can be used. The declaration specifies the function's name, return type, and parameters. For example: `int add(int a, int b);`

3. **Function Definition:** The function definition specifies the code that will be executed when the function is called. It includes the function's return type, name, parameters, and body. For example:
```
int add(int a, int b) {
    return a + b;
}
```

4. **Function Call:** A function is called by specifying its name and providing values for its parameters. The values are passed to the function, and the function's code is executed. For example: `int result = add(3, 4);`

5. **Return Values:** A function can return a value to the code that called it. The return value is specified using the `return` keyword. The function's return type must match the type of the value being returned.

6. **Passing Parameters:** Parameters can be passed to a function by value or by reference. When passed by value, a copy of the value is passed to the function. When passed by reference, the function can modify the original value.

7. **Default Arguments:** A function can have default values for its parameters. If a value is not provided for a parameter when the function is called, the default value is used.

8. **Function Overloading:** C++ allows multiple functions with the same name but different parameters. This is known as function overloading. The correct function is called based on the arguments provided when the function is called.

9. **Recursion:** A function can call itself. This is known as recursion. Recursion can be used to solve problems that can be broken down into smaller, similar problems.

10. **Summary:** Functions are an important part of C++ programming. They allow code to be organized, reused, and tested more easily. Functions can have parameters, return values, and can be overloaded and called recursively.