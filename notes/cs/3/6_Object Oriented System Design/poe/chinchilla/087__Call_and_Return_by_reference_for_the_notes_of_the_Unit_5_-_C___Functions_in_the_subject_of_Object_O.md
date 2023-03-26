### Call and Return by reference for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

In C++, it is possible to pass parameters to a function by reference, which allows the function to modify the original value of the parameter. Similarly, it is also possible to return values from a function by reference.

#### Call by reference

When a parameter is passed to a function by reference, the function receives a reference to the original variable, rather than a copy of it. This means that any modifications made to the parameter inside the function will also affect the original variable outside the function.

To pass a parameter by reference, the parameter must be preceded by an ampersand (&) in the function definition.

```
void myFunction(int& x) {
  x = x + 1;
}

int main() {
  int a = 5;
  myFunction(a);
  cout << a; // Output: 6
  return 0;
}
```

#### Return by reference

Similarly, it is also possible to return a value from a function by reference. This can be useful when we want to modify the value of a variable outside the function.

To return a value by reference, the function must return a reference to the variable, rather than the variable itself. The variable must also be declared as static or global, to ensure that it exists even after the function call.

```
int& myFunction() {
  static int x = 5;
  return x;
}

int main() {
  myFunction() = 10;
  cout << myFunction(); // Output: 10
  return 0;
}
```

#### Advantages of Call and Return by reference

- Passing parameters by reference can be more efficient than passing parameters by value, especially for large objects.
- Returning values by reference can be useful for functions that modify the value of a variable outside the function.
- Call and Return by reference can help to reduce code redundancy and improve code readability.

#### Disadvantages of Call and Return by reference

- Call and Return by reference can make the code more difficult to understand and debug.
- Care must be taken to ensure that the original variable is not inadvertently modified by the function.