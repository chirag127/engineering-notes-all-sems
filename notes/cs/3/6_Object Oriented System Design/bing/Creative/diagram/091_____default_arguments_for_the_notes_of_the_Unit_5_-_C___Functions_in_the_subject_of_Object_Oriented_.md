Hello, I am Sydney, your AI assistant. I can help you with your notes on C++ functions. Here is some information on default arguments:

### Default arguments

- Default arguments are arguments that have a predefined value in the function declaration.
- Default arguments can be used to simplify the function call when some arguments are optional or have a common value.
- Default arguments are specified by assigning a value to the parameter name in the function declaration, for example:

```cpp
// A function that calculates the area of a rectangle
// The third parameter has a default value of 1
double area(double length, double width, double height = 1) {
  return length * width * height;
}
```

- When calling a function with default arguments, the caller can omit the arguments that have default values, for example:

```cpp
// Calling the area function with three arguments
double a1 = area(2, 3, 4); // a1 = 24

// Calling the area function with two arguments
// The third argument is assumed to be 1
double a2 = area(2, 3); // a2 = 6
```

- Default arguments can be omitted from right to left, meaning that the last argument can be omitted first, then the second last, and so on.
- Default arguments cannot be omitted from left to right, meaning that if an argument is omitted, all the arguments to its right must also be omitted, for example:

```cpp
// A function that prints a message with a prefix and a suffix
// The second and third parameters have default values
void printMessage(string message, string prefix = "Hello", string suffix = "!") {
  cout << prefix << " " << message << suffix << endl;
}

// Calling the printMessage function with three arguments
printMessage("World", "Hi", "."); // Hi World.

// Calling the printMessage function with two arguments
// The third argument is assumed to be "!"
printMessage("World", "Hi"); // Hi World!

// Calling the printMessage function with one argument
// The second and third arguments are assumed to be "Hello" and "!"
printMessage("World"); // Hello World!

// Calling the printMessage function with no arguments
// This is invalid and will cause a compilation error
printMessage(); // error: too few arguments to function
```

- Default arguments can be expressions that involve other parameters, constants, or global variables, as long as they can be evaluated at the time of the function call, for example:

```cpp
// A function that calculates the power of a number
// The second parameter has a default value of 2
double power(double base, int exponent = 2) {
  double result = 1;
  for (int i = 0; i < exponent; i++) {
    result *= base;
  }
  return result;
}

// A constant value that can be used as a default argument
const double PI = 3.14;

// A global variable that can be used as a default argument
double g = 9.8;

// A function that calculates the kinetic energy of an object
// The second parameter has a default value of g
double kineticEnergy(double mass, double acceleration = g) {
  return 0.5 * mass * power(acceleration);
}

// Calling the power function with two arguments
double p1 = power(2, 3); // p1 = 8

// Calling the power function with one argument
// The second argument is assumed to be 2
double p2 = power(2); // p2 = 4

// Calling the kineticEnergy function with two arguments
double k1 = kineticEnergy(10, 5); // k1 = 125

// Calling the kineticEnergy function with one argument
// The second argument is assumed to be g
double k2 = kineticEnergy(10); // k2 = 490
```