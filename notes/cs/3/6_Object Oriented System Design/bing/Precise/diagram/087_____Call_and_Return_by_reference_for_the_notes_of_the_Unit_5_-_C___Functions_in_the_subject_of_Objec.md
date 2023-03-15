### Call and Return by Reference

In C++, when a function is called, the arguments are passed to the function by value. This means that the value of the arguments is copied into the function's parameters. Any changes made to the parameters within the function have no effect on the arguments.

However, it is possible to pass arguments to a function by reference. This means that instead of passing the value of the argument, a reference to the argument is passed. Any changes made to the parameter within the function will affect the argument.

To pass an argument by reference, an ampersand (&) is placed after the data type of the parameter in the function declaration and definition. For example:

```c++
void swap(int &x, int &y) {
    int temp = x;
    x = y;
    y = temp;
}
```

In this example, the function `swap` takes two `int` arguments by reference. When the function is called, the values of the arguments are swapped.

It is also possible to return a value by reference from a function. This is done by placing an ampersand (&) after the data type in the function's return type. For example:

```c++
int &max(int &x, int &y) {
    if (x > y)
        return x;
    else
        return y;
}
```

In this example, the function `max` returns a reference to the larger of its two `int` arguments. This allows the caller of the function to modify the value of the larger argument.

Passing arguments by reference can be useful when the function needs to modify the value of the argument or when the argument is a large data structure that would be expensive to copy. However, it should be used with caution as it can make the code more difficult to understand and can introduce subtle bugs if not used correctly.