### Built in Data Types in C

- Data types are the means of specifying the kind of data that can be stored and manipulated by a program.
- C language supports several built in data types, such as int, char, float, double, etc.
- Each data type has a range of values that can be represented and a size in bytes that determines how much memory it occupies.
- The range and size of each data type may vary depending on the compiler and the machine architecture.
- The built in data types in C can be classified into four categories: integer, floating-point, character and void.

#### Integer Data Types

- Integer data types are used to store whole numbers, such as 0, 1, -5, 100, etc.
- C supports four types of integer data types: short int, int, long int and long long int.
- The short int type is used to store small integers, typically 2 bytes in size, with a range of -32768 to 32767.
- The int type is used to store medium-sized integers, typically 4 bytes in size, with a range of -2147483648 to 2147483647.
- The long int type is used to store large integers, typically 4 or 8 bytes in size, with a range of -2147483648 to 2147483647 or -9223372036854775808 to 9223372036854775807.
- The long long int type is used to store very large integers, typically 8 bytes in size, with a range of -9223372036854775808 to 9223372036854775807.
- The integer data types can be modified by using the keywords signed or unsigned, which specify whether the values can be negative or not.
- The signed keyword is the default and can be omitted, while the unsigned keyword indicates that only positive values can be stored.
- For example, unsigned int can store values from 0 to 4294967295, while signed int can store values from -2147483648 to 2147483647.

#### Floating-Point Data Types

- Floating-point data types are used to store real numbers, such as 3.14, -0.5, 1.23e4, etc.
- C supports three types of floating-point data types: float, double and long double.
- The float type is used to store single-precision floating-point numbers, typically 4 bytes in size, with a range of 1.2e-38 to 3.4e38 and a precision of 6 decimal digits.
- The double type is used to store double-precision floating-point numbers, typically 8 bytes in size, with a range of 2.3e-308 to 1.7e308 and a precision of 15 decimal digits.
- The long double type is used to store extended-precision floating-point numbers, typically 10 or 16 bytes in size, with a range and precision that depend on the compiler and the machine architecture.
- The floating-point data types can store both positive and negative values, as well as special values such as infinity and NaN (not a number).

#### Character Data Types

- Character data types are used to store single characters, such as 'a', 'B', '9', etc.
- C supports one type of character data type: char.
- The char type is used to store one byte of data, typically 1 byte in size, with a range of 0 to 255 or -128 to 127, depending on whether it is unsigned or signed.
- The char type can be used to store ASCII characters, which are a set of 128 characters that include letters, digits, punctuation marks, control characters, etc.
- The char type can also be used to store extended ASCII characters, which are a set of 256 characters that include additional symbols, such as accented letters, currency signs, etc.
- The char type can be modified by using the keywords signed or unsigned, which specify whether the values can be negative or not.
- The signed keyword is the default and can be omitted, while the unsigned keyword indicates that only positive values can be stored.
- For example, unsigned char can store values from 0 to 255, while signed char can store values from -128 to 127.

#### Void Data Type

- Void data type is a special type that has no value and no size.
- C supports one type of void data type: void.
- The void type is used to indicate the absence of data or the return type of a function that does not return any value.
- The void type can also be used to create generic pointers, which are pointers that can point to any type of