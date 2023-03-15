### Default Arguments

- Default arguments are used in C++ functions to provide default values for parameters.
- These default values are used when the function is called without providing a value for that specific parameter.
- Default arguments are specified in the function declaration, after the parameter type, using the assignment operator (=).
- The default value must be a constant expression.
- Default arguments can be used for any parameter, but once a default argument is used, all subsequent parameters must also have default arguments.
- Default arguments can make function calls more concise and easier to read, as the caller does not need to provide values for all parameters.
- However, default arguments can also make the code more difficult to understand, as the behavior of the function may change depending on the arguments provided.
- It is important to use default arguments judiciously and to document their behavior clearly.

Example:
```c++
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
In the above example, the `printMessage` function has two parameters: `message` and `times`. The `times` parameter has a default value of `1`, so if the function is called without providing a value for `times`, it will default to `1`. This allows the function to be called with either one or two arguments.