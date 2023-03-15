## Unit 5 - C++ Functions

- A function is a block of code that performs a specific task, such as calculating the area of a circle, printing a message, or sorting an array.
- A function can be called by other parts of the program, or by itself, to execute the code inside it.
- A function can have zero or more parameters, which are variables that hold the values passed to the function by the caller.
- A function can also return a value to the caller, or no value at all, using the `return` statement.
- A function can be defined before or after the main function, or in a separate file, as long as it is declared before it is used.
- A function declaration tells the compiler the name, return type, and parameters of the function, but not the body. It ends with a semicolon. For example:

```cpp
// This is a function declaration
double square(double x); // This function takes a double and returns a double
```

- A function definition provides the body of the function, which contains the statements that execute when the function is called. It starts with the same information as the declaration, followed by a block of code enclosed in braces. For example:

```cpp
// This is a function definition
double square(double x) // This function takes a double and returns a double
{
    return x * x; // This statement returns the square of x to the caller
}
```

- A function can be called by using its name, followed by a pair of parentheses that contain the arguments, which are the values passed to the function. The arguments must match the number and type of the parameters in the function declaration. For example:

```cpp
// This is a function call
double y = square(5.0); // This call passes 5.0 as an argument to the square function, and assigns the return value to y
```

- A function can be overloaded, which means that multiple functions can have the same name, as long as they have different parameters. The compiler will choose the appropriate function based on the arguments passed to the function call. For example:

```cpp
// These are overloaded functions
int square(int x) // This function takes an int and returns an int
{
    return x * x;
}

double square(double x) // This function takes a double and returns a double
{
    return x * x;
}

// These are function calls
int a = square(3); // This call invokes the int version of the square function
double b = square(3.0); // This call invokes the double version of the square function
```

- A function can be recursive, which means that it can call itself within its body. This can be useful for solving problems that have a repetitive or recursive nature, such as factorial, Fibonacci, or binary search. A recursive function must have a base case, which is a condition that stops the recursion, and a recursive case, which is a condition that continues the recursion. For example:

```cpp
// This is a recursive function
int factorial(int n) // This function takes an int and returns an int
{
    if (n == 0) // This is the base case, when n is zero, the factorial is one
    {
        return 1;
    }
    else // This is the recursive case, when n is positive, the factorial is n times the factorial of n-1
    {
        return n * factorial(n-1); // This statement calls the function itself with a smaller argument
    }
}

// This is a function call
int c = factorial(5); // This call invokes the factorial function with 5 as an argument, and assigns the return value to c
```

- A function can be passed as an argument to another function, or returned as a value from another function, by using function pointers. A function pointer is a variable that holds the address of a function, and can be used to invoke the function indirectly. A function pointer can be declared by using the same syntax as a function declaration, but with an asterisk (*) before the name. For example:

```cpp
// This is a function pointer declaration
double (*fptr)(double); // This pointer can point to any function that takes a double and returns a double
```

- A function pointer can be assigned the address of a function by using the name of the function without parentheses. For example:

```cpp
// This is a function pointer assignment
fptr = square; // This statement assigns the address of the square function to the fptr pointer
```

- A function pointer can be used to call the function by using the dereference operator (*) before the name, followed by the