# Constants in C++ Basics

Constants are fixed values that do not change during the execution of a program. In C++, there are several ways to define constants:

1. **Literal Constants**: These are fixed values that are inserted directly into the source code. For example, `3.14` is a literal constant of type `double`.

2. **Defined Constants**: These are constants defined using the preprocessor directive `#define`. For example, `#define PI 3.14` defines a constant named `PI` with the value `3.14`.

3. **Constant Variables**: These are variables declared with the `const` keyword. For example, `const double PI = 3.14;` declares a constant variable named `PI` of type `double` with the value `3.14`.

4. **Enumerated Constants**: These are constants defined using the `enum` keyword. For example, `enum {RED, GREEN, BLUE};` defines three constants named `RED`, `GREEN`, and `BLUE` with values `0`, `1`, and `2`, respectively.

Constants are useful for representing values that do not change, such as mathematical constants like `PI`, physical constants like the speed of light, or configuration values like the maximum number of players in a game. Using constants instead of hardcoding values into the source code makes the code more readable and easier to maintain.