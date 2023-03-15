### Default arguments

- Default arguments are values that are automatically assigned to parameters of a function if the caller does not provide them explicitly.
- Default arguments can be useful to simplify the function call and avoid unnecessary repetition of values.
- Default arguments are specified in the function declaration, after the parameter name, using the assignment operator (=) and a constant expression.
- Default arguments can only be omitted from right to left, meaning that if a parameter has a default argument, all the parameters to its right must also have default arguments.
- Default arguments are evaluated only once, when the function is declared, not every time the function is called. This means that default arguments should not depend on any variable or expression that may change at runtime.
- Example:

```cpp
// Function declaration with default arguments
void printMessage(std::string message, int times = 1, char symbol = '*');

// Function definition
void printMessage(std::string message, int times, char symbol) {
  for (int i = 0; i < times; i++) {
    std::cout << symbol << " " << message << " " << symbol << "\n";
  }
}

// Function calls
printMessage("Hello"); // prints "* Hello *"
printMessage("World", 3); // prints "* World *" three times
printMessage("Bye", 2, '#'); // prints "# Bye #" two times
```