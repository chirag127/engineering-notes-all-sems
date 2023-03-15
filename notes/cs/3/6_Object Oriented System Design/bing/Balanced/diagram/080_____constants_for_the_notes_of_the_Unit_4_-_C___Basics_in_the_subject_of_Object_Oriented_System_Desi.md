### Constants

Constants are expressions with a fixed value that cannot be modified during the program's execution. They are used to represent values that are known at compile time and do not change. Constants can be of any data type, such as integer, float, character, string, etc.

There are two ways to define constants in C++:

- By using the `const` keyword
- By using the `#define` preprocessor directive

#### Using the `const` keyword

The `const` keyword is used to declare a variable as a constant. The syntax is:

```cpp
const data_type variable_name = value;
```

For example:

```cpp
const int PI = 3.14; // declare a constant integer
const char GENDER = 'M'; // declare a constant character
const string NAME = "Sydney"; // declare a constant string
```

The `const` keyword can also be used to declare constant pointers, references, and parameters.

#### Using the `#define` preprocessor directive

The `#define` preprocessor directive is used to define a macro that can be replaced by a value or an expression. The syntax is:

```cpp
#define macro_name value_or_expression
```

For example:

```cpp
#define PI 3.14 // define a macro for the value of pi
#define AREA(r) (PI * r * r) // define a macro for the area of a circle
```

The `#define` directive does not require a semicolon at the end. It can also be used to define symbolic constants, such as:

```cpp
#define TRUE 1 // define a macro for the boolean value true
#define FALSE 0 // define a macro for the boolean value false
```

The advantage of using the `#define` directive is that it can save memory and execution time, as the macros are replaced by their values at compile time. However, the disadvantage is that it can cause errors and confusion, as the macros are not checked by the compiler and can have unintended side effects.