### Overloading of functions for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design

Function overloading is a feature in C++ where two or more functions can have the same name but different parameters. Function overloading can be considered as an example of polymorphism feature in C++.

The following conditions must be met to overload a function in C++:
- The function must have the same name.
- The function must have a different number of parameters or the parameters must have different types or the parameters must be in a different order.

When a function is overloaded, the compiler determines which function to use based on the arguments passed to the function. This process is known as function resolution.

Here is an example of function overloading in C++:
```c++
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}

int main() {
    int x = 5, y = 10;
    double p = 5.5, q = 10.5;
    cout << add(x, y) << endl;
    cout << add(p, q) << endl;
    return 0;
}
```
In the above example, the `add` function is overloaded with two different versions: one that takes two `int` arguments and another that takes two `double` arguments. When the `add` function is called with `int` arguments, the first version of the `add` function is called. When the `add` function is called with `double` arguments, the second version of the `add` function is called.

Function overloading is useful when you want to perform the same operation on different types of data. It allows you to write more readable and maintainable code. However, it is important to use function overloading judiciously and not overload functions unnecessarily.