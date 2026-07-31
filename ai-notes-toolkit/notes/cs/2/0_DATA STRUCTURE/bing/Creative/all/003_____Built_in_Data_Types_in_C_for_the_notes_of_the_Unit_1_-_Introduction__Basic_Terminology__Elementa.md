# Built in Data Types in C

- Built in data types (also called fundamental types) are specified by the C language standard and are built into the compiler.
- Built in data types are not defined in any header file.
- Built in data types determine the size and range of values that can be stored in a variable, as well as the operations that can be performed on it .
- The C language provides the four basic arithmetic type specifiers: `char`, `int`, `float` and `double`, and the modifiers `signed`, `unsigned`, `short`, and `long`.
- The following table summarizes some commonly used built in data types in C along with their description, size and range   .

| Data Type | Description | Size (in bytes) | Range |
| --- | --- | --- | --- |
| `char` | Character or small integer | 1 | -128 to 127 or 0 to 255 |
| `unsigned char` | Unsigned character or small integer | 1 | 0 to 255 |
| `signed char` | Signed character or small integer | 1 | -128 to 127 |
| `int` | Integer | 2 or 4 | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 |
| `unsigned int` | Unsigned integer | 2 or 4 | 0 to 65,535 or 0 to 4,294,967,295 |
| `short` | Short integer | 2 | -32,768 to 32,767 |
| `unsigned short` | Unsigned short integer | 2 | 0 to 65,535 |
| `long` | Long integer | 4 or 8 | -2,147,483,648 to 2,147,483,647 or -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `unsigned long` | Unsigned long integer | 4 or 8 | 0 to 4,294,967,295 or 0 to 18,446,744,073,709,551,615 |
| `float` | Single precision floating point | 4 | +/- 3.4e +/- 38 (~7 digits) |
| `double` | Double precision floating point | 8 | +/- 1.7e +/- 308 (~15 digits) |
| `long double` | Extended precision floating point | 10 | +/- 3.4e +/- 4932 (~19 digits) |
| `void` | Valueless special purpose | - | - |

- The exact sizes and ranges of values for the built in data types are implementation dependent , meaning they may vary depending on the compiler and the system architecture.
- The `sizeof` operator can be used to determine the size of a data type or a variable in bytes .
- For example, `sizeof(int)` returns the size of an `int` data type, and `sizeof(x)` returns the size of the variable `x`.
- The `void` data type is a special type that has no value and is used to indicate an empty set of parameters or return type for a function   .
- For example, `void func(void)` is a function that takes no parameters and returns nothing.