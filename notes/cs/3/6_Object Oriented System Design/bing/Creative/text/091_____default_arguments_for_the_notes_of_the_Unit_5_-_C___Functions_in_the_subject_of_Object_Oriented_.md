### Default arguments

- Default arguments are arguments that have a predefined value in the function declaration.
- Default arguments are used when the function is called without passing some or all of the arguments.
- Default arguments can simplify the function call and avoid unnecessary repetition of values.
- Default arguments are specified from right to left in the function declaration, meaning that the rightmost argument must have a default value before the leftmost argument can have one.
- Default arguments can be constants, variables, expressions, or function calls, as long as they are compatible with the argument type and can be evaluated at compile time.
- Default arguments can be overridden by passing a different value in the function call.
- Default arguments are part of the function declaration, not the function definition. They should be specified only once, either in the header file or in the source file, but not both.
- Default arguments are not part of the function signature, meaning that they do not affect the function overloading or the function pointer type.

#### Example

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
printMessage("Hello"); // prints * Hello *
printMessage("World", 3); // prints * World * three times
printMessage("Bye", 2, '#'); // prints # Bye # two times
```