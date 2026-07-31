### Call and Return by Reference

- In C++, when a function is called by reference, the parameters passed to the function are references to the original values, rather than copies of the values.
- This means that any changes made to the parameters within the function will affect the original values.
- To call a function by reference, the reference operator (&) is used in the function declaration and definition.
- For example, to call a function `swap` by reference, the function declaration would be `void swap(int &a, int &b)`.
- When calling the function, the arguments passed to the function must be variables, not constants or expressions.
- Returning a value by reference works in a similar way. The function must return a reference to a variable, rather than the value of the variable.
- This allows the function to return a value that can be modified by the calling code.
- For example, a function `getMax` that returns the maximum value of two integers by reference would be declared as `int &getMax(int &a, int &b)`.
- When calling the function, the returned value can be assigned to a variable, which can then be modified.
- It is important to note that the variable being returned by reference must have a lifetime that extends beyond the scope of the function. This means that it cannot be a local variable within the function.
- Call and return by reference can be useful in certain situations, such as when modifying large data structures or when working with classes and objects.
