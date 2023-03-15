### Simple Functions

In C++, a function is a block of code that performs a specific task. Functions are used to modularize and organize code, making it easier to read, understand, and maintain. In this section, we will discuss simple functions in C++.

1. **Function Declaration:** A function must be declared before it can be used in a program. The declaration specifies the function's name, return type, and any parameters it takes. For example, the following code declares a function named `add` that takes two `int` parameters and returns an `int` value:

```c++
int add(int x, int y);
```

2. **Function Definition:** The function definition specifies the code that will be executed when the function is called. The definition includes the function's return type, name, parameters, and body. For example, the following code defines the `add` function declared above:

```c++
int add(int x, int y) {
    return x + y;
}
```

3. **Function Call:** To use a function, it must be called from another part of the program. The function call specifies the function's name and any arguments that must be passed to it. For example, the following code calls the `add` function with the arguments `3` and `4`:

```c++
int result = add(3, 4);
```

4. **Return Statement:** A function can return a value to the calling code using the `return` statement. The value returned must be of the same type as the function's return type. For example, the `add` function defined above returns the sum of its two arguments.

These are the basics of simple functions in C++. They allow us to write modular, organized, and maintainable code. In the next sections, we will discuss more advanced topics such as function overloading, default arguments, and recursion.