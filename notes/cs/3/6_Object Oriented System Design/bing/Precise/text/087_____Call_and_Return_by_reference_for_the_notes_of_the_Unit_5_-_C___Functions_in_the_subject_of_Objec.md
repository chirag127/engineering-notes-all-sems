### Call and Return by Reference

- In C++, a function can return a value to the calling function in two ways: by value and by reference.
- When a function returns a value by reference, it returns a reference to the variable rather than a copy of the variable's value.
- This allows the calling function to directly access and modify the original variable, rather than working with a copy of its value.
- To return a value by reference, the function's return type must be a reference type, indicated by an ampersand (&) following the data type in the function declaration.
- For example, to return an integer by reference, the function's return type would be `int&`.
- When calling a function that returns a value by reference, the returned reference can be assigned to a reference variable or used to directly modify the original variable.
- It is important to note that returning a reference to a local variable from a function is dangerous, as the local variable will be destroyed when the function exits, leaving the reference pointing to an invalid memory location.
- Returning a reference to a static or global variable, or to a variable passed to the function by reference, is safe as these variables will still exist after the function exits.
