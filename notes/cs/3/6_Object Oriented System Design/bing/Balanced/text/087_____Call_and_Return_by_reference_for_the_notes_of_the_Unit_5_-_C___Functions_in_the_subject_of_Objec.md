### Call and Return by Reference

- Call by reference is a technique of passing arguments to a function in which the actual memory addresses of the arguments are passed to the function.
- This means that any changes made to the parameters inside the function will affect the original variables in the caller function.
- To pass an argument by reference, we use the `&` operator before the parameter name in the function declaration and definition.
- For example, `void swap(int &a, int &b)` is a function that takes two integers by reference and swaps their values.
- Return by reference is a technique of returning a value from a function in which the function returns a reference (or a pointer) to a variable instead of a copy of the variable.
- This means that the caller function can access and modify the returned variable directly, without creating a new variable.
- To return a value by reference, we use the `&` operator before the return type in the function declaration and definition.
- For example, `int &max(int &a, int &b)` is a function that returns a reference to the larger of the two integers passed by reference.
- Call and return by reference are useful for improving the efficiency and flexibility of the code, as they avoid unnecessary copying of large or complex data structures. However, they also introduce some risks, such as dangling references, memory leaks, or unintended side effects. Therefore, they should be used with caution and proper documentation.