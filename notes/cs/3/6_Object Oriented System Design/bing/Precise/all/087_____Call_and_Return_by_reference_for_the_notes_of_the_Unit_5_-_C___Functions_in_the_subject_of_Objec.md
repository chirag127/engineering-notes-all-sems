### Call and Return by Reference

In C++, when a function is called, the arguments are passed by value, meaning that a copy of the value is passed to the function. This means that any changes made to the value within the function do not affect the original value outside of the function.

However, there is a way to pass arguments to a function in such a way that changes made to the value within the function do affect the original value outside of the function. This is known as passing by reference.

To pass an argument by reference, the reference operator (&) is used in the function declaration and definition. For example, consider the following function that swaps the values of two integers:

```c++
void swap(int &x, int &y) {
    int temp = x;
    x = y;
    y = temp;
}
```

In this example, the arguments `x` and `y` are passed by reference. This means that when the function is called, the values of the variables passed as arguments are swapped.

Similarly, a function can also return a value by reference. This allows the function to return a reference to a variable, which can then be used to directly modify the value of the variable. To return a value by reference, the reference operator (&) is used in the function declaration and definition.

Here is an example of a function that returns a reference to the larger of two integers:

```c++
int &max(int &x, int &y) {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
```

In this example, the function `max` returns a reference to the larger of the two integers passed as arguments. This means that the value of the larger integer can be directly modified using the returned reference.

In summary, passing and returning by reference allows a function to directly modify the values of variables passed as arguments or returned by the function. This can be useful in certain situations, but it is important to use this feature with caution, as it can make the code more difficult to understand and maintain.