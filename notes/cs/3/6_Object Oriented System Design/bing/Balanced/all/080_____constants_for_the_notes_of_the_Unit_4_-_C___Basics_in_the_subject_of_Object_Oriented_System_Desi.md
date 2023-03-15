# Constants

Constants are expressions with a fixed value that cannot be changed during the program's execution. They are used to represent values that are known at compile time and do not need to be modified by the program. For example, the value of pi (3.14159) or the number of days in a week (7) can be declared as constants.

There are two ways to define constants in C++:

- Using the `#define` preprocessor directive
- Using the `const` keyword

## Using the `#define` preprocessor directive

The `#define` preprocessor directive is used to define a constant as a macro. A macro is a symbolic name that is replaced by the preprocessor with a value or an expression before the compilation. The syntax of the `#define` directive is:

```cpp
#define identifier value
```

where `identifier` is the name of the constant and `value` is the value or expression to be assigned to it. For example:

```cpp
#define PI 3.14159
#define MAX 100
#define MIN(a,b) ((a)<(b)?(a):(b))
```

The advantages of using the `#define` directive are:

- It can be used to define constants of any data type, including user-defined types.
- It can be used to define constants that involve calculations or expressions.
- It can be used to define constants that span multiple lines using the `\` character.

The disadvantages of using the `#define` directive are:

- It does not perform type checking or type conversion, which can lead to errors or unexpected results.
- It can cause name conflicts or collisions with other identifiers in the program or in the libraries.
- It can make debugging difficult, as the debugger does not recognize the macro names.

## Using the `const` keyword

The `const` keyword is used to declare a variable as a constant. A constant variable is a variable whose value cannot be changed after initialization. The syntax of the `const` keyword is:

```cpp
const data_type identifier = value;
```

where `data_type` is the type of the constant, `identifier` is the name of the constant, and `value` is the value to be assigned to it. For example:

```cpp
const double pi = 3.14159;
const int max = 100;
const char letter = 'A';
```

The advantages of using the `const` keyword are:

- It performs type checking and type conversion, which can prevent errors or unexpected results.
- It avoids name conflicts or collisions with other identifiers in the program or in the libraries.
- It can be used with pointers and references to create constant objects or constant views of objects.
- It can be used with classes and functions to create constant members or constant methods.

The disadvantages of using the `const` keyword are:

- It can only be used to define constants of basic or user-defined types, not expressions or calculations.
- It can only be used to define constants that fit in one line, not multiple lines.
- It can cause memory overhead, as the constant variables are stored in the memory.