### Built in Data Types in C

- Data types are the means of specifying the kind of data that can be stored and manipulated by a program.
- C language supports several built in data types, such as int, char, float, double, etc.
- Each data type has a range of values that it can represent, and a size in bytes that it occupies in memory.
- The range and size of a data type may vary depending on the compiler and the platform.
- The built in data types in C can be classified into four categories: integer, floating-point, character, and derived.

#### Integer Data Types

- Integer data types are used to store whole numbers, such as 0, 1, -5, 42, etc.
- C supports four integer data types: char, short, int, and long.
- The char data type is used to store a single character, such as 'a', '9', or '#'. It can also be used to store small integers, such as 0 to 127, or -128 to 127, depending on whether it is signed or unsigned. The size of char is 1 byte.
- The short data type is used to store small integers, such as -32768 to 32767, or 0 to 65535, depending on whether it is signed or unsigned. The size of short is 2 bytes.
- The int data type is used to store medium-sized integers, such as -2147483648 to 2147483647, or 0 to 4294967295, depending on whether it is signed or unsigned. The size of int is usually 4 bytes, but it may vary depending on the compiler and the platform.
- The long data type is used to store large integers, such as -9223372036854775808 to 9223372036854775807, or 0 to 18446744073709551615, depending on whether it is signed or unsigned. The size of long is usually 8 bytes, but it may vary depending on the compiler and the platform.
- The integer data types can be modified by using the keywords signed, unsigned, short, and long, to specify the range and size of the data type. For example, unsigned long int is a data type that can store positive integers up to 18446744073709551615, and has a size of 8 bytes.

#### Floating-Point Data Types

- Floating-point data types are used to store real numbers, such as 3.14, -0.001, 6.022e23, etc.
- C supports two floating-point data types: float and double.
- The float data type is used to store single-precision floating-point numbers, which have a decimal point and a fractional part. The range of float is approximately -3.4e38 to 3.4e38, and the precision is about 6 to 7 digits. The size of float is 4 bytes.
- The double data type is used to store double-precision floating-point numbers, which have a decimal point and a fractional part. The range of double is approximately -1.7e308 to 1.7e308, and the precision is about 15 to 16 digits. The size of double is 8 bytes.
- The floating-point data types can be modified by using the keyword long, to specify a higher precision and range. For example, long double is a data type that can store extended-precision floating-point numbers, which have a decimal point and a fractional part. The range and precision of long double may vary depending on the compiler and the platform, but it is usually greater than double. The size of long double is usually 10 or 16 bytes.

#### Character Data Types

- Character data types are used to store characters, such as letters, digits, symbols, etc.
- C supports one character data type: char.
- The char data type is used to store a single character, such as 'a', '9', or '#'. It can also be used to store small integers, such as 0 to 127, or -128 to 127, depending on whether it is signed or unsigned. The size of char is 1 byte.
- The char data type can be modified by using the keywords signed and unsigned, to specify the range of the data type. For example, unsigned char is a data type that can store positive integers from 0 to 255, and has a size of 1 byte.
- The char data type can also be used to store strings, which are sequences of characters, such as "Hello", "C", or "Data Structure". Strings are stored as arrays of char, and are terminated by a special