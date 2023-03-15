### Typecasting

- Typecasting is the process of converting one data type to another.
- There are two types of typecasting: implicit and explicit.
- Implicit typecasting is done automatically by the compiler when there is no loss of information or precision. For example, converting an int to a double.
- Explicit typecasting is done by the programmer using a cast operator or a constructor. For example, converting a double to an int by using `(int)` or `int()`.
- There are four types of explicit typecasting in C++: static_cast, dynamic_cast, const_cast and reinterpret_cast.
- static_cast is used to convert between compatible types, such as pointers to derived and base classes, or numeric types.
- dynamic_cast is used to perform safe downcasting, which is converting a pointer or reference to a base class to a pointer or reference to a derived class. It checks the type at run-time and returns null or throws an exception if the conversion is invalid.
- const_cast is used to remove the const qualifier from a pointer or reference, allowing to modify a constant object.
- reinterpret_cast is used to convert between unrelated types, such as pointers to different classes, or pointers to integers. It does not check the type or the validity of the conversion, and may result in undefined behavior.