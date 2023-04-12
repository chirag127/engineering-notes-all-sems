## Unit 5 - C++ Functions

A function is a block of code that performs a specific task. Functions are used to modularize, reuse, and simplify the code. Functions can also improve the readability and maintainability of the code.

Some of the main concepts related to functions are:

- **Function declaration**: A function declaration specifies the name, return type, and parameters of a function. It is also called a function prototype. A function declaration is usually placed at the beginning of the program, before the main function. For example:

```cpp
// A function declaration for a function that adds two integers and returns the result
int add(int a, int b);
```

- **Function definition**: A function definition provides the body of the function, which contains the statements that execute when the function is called. A function definition must match the function declaration in name, return type, and parameters. A function definition can be placed anywhere in the program, but it is usually placed after the main function or in a separate source file. For example:

```cpp
// A function definition for the add function
int add(int a, int b) {
  int result = a + b; // a local variable that stores the sum of a and b
  return result; // return the result to the caller
}
```

- **Function call**: A function call is an expression that invokes a function with some arguments (also called parameters or inputs). A function call evaluates to the value returned by the function. A function call can be used as a statement or as part of another expression. For example:

```cpp
// A function call as a statement
add(3, 4); // calls the add function with 3 and 4 as arguments

// A function call as part of an expression
int x = add(5, 6) * 2; // calls the add function with 5 and 6 as arguments, and multiplies the result by 2
```

- **Function parameter**: A function parameter is a variable that receives a value from the caller when the function is invoked. A function can have zero or more parameters, which are specified in the function declaration and definition. Parameters are also called formal parameters or input parameters. For example:

```cpp
// A function with two parameters: a and b
int add(int a, int b) {
  // ...
}
```

- **Function argument**: A function argument is a value that is passed to the function when the function is called. An argument can be a constant, a variable, or an expression. Arguments are also called actual parameters or input arguments. For example:

```cpp
// A function call with two arguments: 3 and 4
add(3, 4);
```

- **Function return type**: A function return type is the type of the value that the function returns to the caller. A function can have any valid data type as its return type, or it can have the special type void, which means that the function does not return any value. The return type is specified in the function declaration and definition. For example:

```cpp
// A function with an int return type
int add(int a, int b) {
  // ...
}

// A function with a void return type
void printHello() {
  cout << "Hello" << endl; // print Hello to the standard output
}
```

- **Function return statement**: A function return statement is a statement that terminates the execution of the function and returns a value to the caller. A return statement must have an expression that matches the return type of the function, or no expression if the return type is void. A return statement can be placed anywhere in the function body, but it is usually placed at the end. For example:

```cpp
// A function with a return statement that returns the result of adding a and b
int add(int a, int b) {
  int result = a + b;
  return result;
}

// A function with a return statement that does not return any value
void printHello() {
  cout << "Hello" << endl;
  return; // optional
}
```

- **Function scope**: A function scope is the region of the program where the function name and parameters are visible and can be used. A function scope begins at the function declaration and ends at the end of the program. A function name can be used to call the function from any other function in the program. A function parameter can be used only within the function body. For example:

```cpp
// A function declaration that defines the function scope
int add(int a, int b);

// A function call that uses the function name
int x = add(3, 4);

// A function definition

```
