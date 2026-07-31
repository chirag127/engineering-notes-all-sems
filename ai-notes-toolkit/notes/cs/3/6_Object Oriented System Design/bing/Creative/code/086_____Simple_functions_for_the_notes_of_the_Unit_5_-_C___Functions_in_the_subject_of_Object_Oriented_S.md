# Simple functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

- A function is a block of code that performs a specific task, such as calculating the sum of two numbers, printing a message, or sorting an array.
- A function can be defined using the following syntax:

```cpp
return_type function_name(parameter_list)
{
  // function body
  // statements
  return value; // optional
}
```

- The return_type specifies the data type of the value that the function returns to the caller. If the function does not return any value, the return_type can be void.
- The function_name is an identifier that represents the name of the function. It follows the same naming rules as variables.
- The parameter_list is a comma-separated list of zero or more parameters that the function accepts. Each parameter has a name and a data type, such as int x or string name. Parameters are also called arguments or formal parameters.
- The function body is a block of code enclosed by curly braces that contains the statements that implement the logic of the function. The function body can also declare local variables that are only visible within the function scope.
- The return statement is used to terminate the function and return a value to the caller. If the function has a void return type, the return statement can be omitted or used without a value.

- A function can be called by using its name followed by a pair of parentheses that contain the actual arguments or values that are passed to the function. For example:

```cpp
int sum = add(10, 20); // call the add function with two arguments
cout << "The sum is " << sum << endl; // print the result
```

- The actual arguments or values that are passed to the function are also called actual parameters. They can be constants, variables, expressions, or other functions. The actual parameters are matched with the formal parameters by their position, not by their name. For example, the first actual parameter is assigned to the first formal parameter, the second actual parameter is assigned to the second formal parameter, and so on.
- A function can be declared before it is defined by using a function prototype. A function prototype is a statement that specifies the name, return type, and parameter list of the function, but not its body. For example:

```cpp
int add(int x, int y); // function prototype
```

- A function prototype tells the compiler the signature of the function, which allows the compiler to check the validity of the function calls and the return values. A function prototype can be placed at the beginning of the source file, or in a separate header file that can be included by other source files.
- A function can be defined in the same source file where it is declared, or in a different source file. If the function is defined in a different source file, the source file that contains the function definition must be compiled and linked with the source file that contains the function call. For example, if the add function is defined in add.cpp, and the main function that calls the add function is in main.cpp, then both add.cpp and main.cpp must be compiled and linked together to create the executable program.