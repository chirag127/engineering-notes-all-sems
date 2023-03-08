### Call and Return by reference

In C++, we are allowed to pass arguments to functions using both call by value and call by reference. Similarly, we can also return values from a function using call by value or call by reference. In this section, we will discuss call and return by reference.

#### Call by Reference

When we pass an argument by reference, we pass the address of the variable instead of its value. This means that any changes made to the variable inside the function will affect the original variable in the calling function. 

The syntax for passing an argument by reference is as follows:

```cpp
void someFunction(int& x) {
    // function body
}
```

In the above example, `x` is a reference to an integer.

Advantages of Call by Reference:
- It allows us to modify the original variable inside the function.
- It is more efficient than call by value since no copy of the variable is made.

Disadvantages of Call by Reference:
- It can sometimes cause unintended changes to the original variable.
- It can be difficult to read and understand the code.

#### Return by Reference

When we return a value by reference, we return a reference to a variable instead of its value. This means that any changes made to the returned variable outside the function will affect the original variable inside the function.

The syntax for returning a value by reference is as follows:

```cpp
int& someFunction() {
    // function body
}
```

In the above example, `someFunction` returns a reference to an integer.

Advantages of Return by Reference:
- It allows us to modify the original variable outside the function.
- It is more efficient than returning by value since no copy of the variable is made.

Disadvantages of Return by Reference:
- It can sometimes cause unintended changes to the original variable.
- It can be difficult to read and understand the code.

Overall, call and return by reference can be useful in certain situations where we want to modify the original variable inside or outside the function. However, it should be used with caution to avoid unintended consequences.