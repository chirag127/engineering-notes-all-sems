### Default Arguments

- Default arguments are used in C++ functions to provide default values for parameters.
- These default values are used when the function is called without providing a value for that specific parameter.
- Default arguments are specified in the function declaration, after the parameter type, using the assignment operator (=).
- When calling a function with default arguments, the arguments can be omitted from the function call, and the default values will be used instead.
- Default arguments can be used to make a function more flexible and easier to use.
- Default arguments must be specified from right to left, meaning that if a default value is provided for a parameter, all parameters to the right of that parameter must also have default values.
- Default arguments can be any valid C++ expression, including function calls and calculations.
- Default arguments can be used to provide backward compatibility for existing code, by adding new parameters to a function without changing the way the function is called in existing code.

Example:
```c++
#include <iostream>
using namespace std;

void display(char c = '*', int n = 10) {
    for (int i = 0; i < n; i++) {
        cout << c;
    }
    cout << endl;
}

int main() {
    display();
    display('#');
    display('#', 5);
    return 0;
}
```

In the above example, the `display` function has two parameters, `c` and `n`, with default values of `'*'` and `10`, respectively. When the function is called without any arguments, as in the first call in the `main` function, the default values are used. In the second call, only the first argument is provided, so the default value for `n` is used. In the third call, both arguments are provided, so the default values are not used. The output of the program is:
```
**********
##########
#####
```