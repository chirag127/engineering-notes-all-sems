### Default Arguments

- Default arguments are used in C++ functions to provide default values for parameters.
- Default arguments are specified in the function declaration, after the parameter type, using the assignment operator `=`.
- When calling a function with default arguments, the caller can omit the arguments for the parameters with default values.
- If an argument is omitted, the default value is used instead.
- Default arguments must be specified from right to left, meaning that if a default value is provided for a parameter, all parameters to its right must also have default values.
- Default arguments can be any valid C++ expression, including function calls and variables.
- Default arguments can make function calls more concise and easier to read, but they can also make the function's behavior less explicit.
- It is important to use default arguments judiciously and to document their behavior clearly.

Example:
```cpp
#include <iostream>
using namespace std;

void printMessage(string message, int times = 1) {
    for (int i = 0; i < times; i++) {
        cout << message << endl;
    }
}

int main() {
    printMessage("Hello, World!"); // prints "Hello, World!" once
    printMessage("Hello, World!", 3); // prints "Hello, World!" three times
    return 0;
}
```
In the above example, the `printMessage` function has two parameters: `message` and `times`. The `times` parameter has a default value of `1`, so if the caller omits the second argument when calling the function, `times` will be set to `1`. This is demonstrated in the first call to `printMessage` in the `main` function. In the second call to `printMessage`, the caller provides a value for `times`, so the default value is not used.
