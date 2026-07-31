### Constants

Constants are expressions with a fixed value that cannot be changed during the program's execution. They are used to represent values that are known at compile time and do not need to be modified by the program. Constants can improve the readability, maintainability and performance of the code.

There are two ways to define constants in C++:

- Using the `#define` preprocessor directive
- Using the `const` keyword

#### Using the `#define` preprocessor directive

The `#define` preprocessor directive is used to define a constant as a macro. A macro is a symbolic name that is replaced by the preprocessor with a value or an expression before the compilation. The syntax of the `#define` directive is:

```cpp
#define identifier value
```

For example:

```cpp
#define PI 3.14
#define MAX 100
#define MESSAGE "Hello World"
```

The advantages of using the `#define` directive are:

- It can be used to define constants of any data type, including user-defined types.
- It can be used to define constants that involve calculations or expressions.
- It can be used to define constants that span multiple lines using the `\` character.

The disadvantages of using the `#define` directive are:

- It does not perform type checking or scope checking, which can lead to errors or conflicts.
- It can cause problems with debugging, as the debugger does not recognize the macro names.
- It can cause side effects or unexpected results if the macro name is used as part of another identifier or expression.

#### Using the `const` keyword

The `const` keyword is used to declare a variable as a constant. A constant variable is a variable whose value cannot be changed after initialization. The syntax of the `const` keyword is:

```cpp
const data_type identifier = value;
```

For example:

```cpp
const double PI = 3.14;
const int MAX = 100;
const char MESSAGE[] = "Hello World";
```

The advantages of using the `const` keyword are:

- It performs type checking and scope checking, which can prevent errors or conflicts.
- It can be used with pointers and references to create constant objects or constant views of objects.
- It can be used with functions to indicate that the function does not modify its parameters or the object it belongs to.

The disadvantages of using the `const` keyword are:

- It can only be used to define constants of basic data types, not user-defined types.
- It cannot be used to define constants that involve calculations or expressions, unless they are evaluated at compile time.
- It cannot be used to define constants that span multiple lines.