### Operator Overloading

- Operator overloading is a feature in object-oriented programming languages that allows operators to have extended meanings when applied to user-defined data types.
- This is achieved by defining a special function, called an operator function, that specifies the behavior of the operator when applied to objects of a particular class.
- The syntax for defining an operator function varies between languages, but typically involves the keyword `operator` followed by the operator symbol.
- For example, in C++, the addition operator `+` can be overloaded for a class `Complex` representing complex numbers by defining a function with the signature `Complex operator+(const Complex& a, const Complex& b)`.
- This function takes two `Complex` objects as arguments and returns a new `Complex` object representing the sum of the two arguments.
- Once the operator function is defined, the addition operator can be used with `Complex` objects in the same way as with built-in data types, such as `int` or `double`.
- Not all operators can be overloaded in all languages. The set of overloadable operators and the rules for overloading them vary between languages.
- In general, operator overloading can make code more readable and expressive by allowing the use of familiar syntax with user-defined data types.
- However, it is important to use operator overloading judiciously, as overloading operators in non-intuitive ways can make code more difficult to understand and maintain.
