### Simple Functions

In C++, a function is a block of code that performs a specific task. Functions are used to modularize and organize code, making it easier to read, understand, and maintain. Here are some key points to remember about simple functions in C++:

1. A function declaration, also known as a function prototype, specifies the function's name, return type, and parameters. For example, `int add(int x, int y);` is a function declaration for a function named `add` that takes two `int` parameters and returns an `int` value.

2. A function definition provides the actual code that implements the function. It includes the function's name, return type, parameters, and the statements that make up the function's body. For example:
```
int add(int x, int y) {
    return x + y;
}
```
This is a function definition for the `add` function declared earlier.

3. To call a function, you use its name followed by parentheses containing any arguments that the function requires. For example, `int sum = add(3, 4);` calls the `add` function with arguments `3` and `4`, and assigns the result to the variable `sum`.

4. Functions can return a value to the caller using the `return` statement. The value returned must be of the same type as the function's return type. For example, the `add` function returns the sum of its two arguments.

5. Functions can also have `void` return type, which means they do not return a value. In this case, the function performs some action but does not return a result to the caller.

6. Functions can have default arguments, which are values that are automatically used if the caller does not provide an argument for that parameter. For example, `int add(int x, int y = 0);` declares a function with a default argument of `0` for the second parameter. If the function is called with only one argument, the second argument will automatically be `0`.

7. Function overloading allows multiple functions with the same name but different parameters to be defined. The compiler determines which function to call based on the number and types of arguments provided. For example, you could define two `add` functions, one that takes two `int` arguments and one that takes two `double` arguments.

These are some of the basic concepts of simple functions in C++. By using functions, you can break down complex tasks into smaller, more manageable pieces, making your code easier to write, read, and maintain.