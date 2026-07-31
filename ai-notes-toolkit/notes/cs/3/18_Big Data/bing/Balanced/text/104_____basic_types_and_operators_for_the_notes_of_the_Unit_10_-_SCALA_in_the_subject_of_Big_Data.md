### Basic Types and Operators

- Scala has a rich set of basic types, including numeric, boolean, string, and character types.
- Scala also supports operators that can be applied to these types, such as arithmetic, relational, logical, and bitwise operators.
- Scala operators are actually methods that can be invoked using infix notation, such as `a + b` or `a < b`.
- Scala operators have precedence rules based on the first character of the operator name, such as `* / %` having higher precedence than `+ -`.
- Scala operators can also be overloaded or defined for custom types, such as classes or case classes.

Some of the basic types and operators in Scala are:

- **Boolean**: A type that represents a logical value, either `true` or `false`. Boolean values can be compared using the operators `==`, `!=`, `!`, `&&`, and `||`.
- **Int**: A type that represents a 32-bit signed integer. Int values can be manipulated using the operators `+`, `-`, `*`, `/`, `%`, `<<`, `>>`, `>>>`, `&`, `|`, `^`, `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- **Long**: A type that represents a 64-bit signed integer. Long values can be manipulated using the same operators as Int, but with an `L` suffix, such as `1L + 2L`.
- **Short**: A type that represents a 16-bit signed integer. Short values can be manipulated using the same operators as Int, but with an `S` suffix, such as `1S + 2S`.
- **Byte**: A type that represents an 8-bit signed integer. Byte values can be manipulated using the same operators as Int, but with a `B` suffix, such as `1B + 2B`.
- **Double**: A type that represents a 64-bit floating-point number. Double values can be manipulated using the operators `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- **Float**: A type that represents a 32-bit floating-point number. Float values can be manipulated using the same operators as Double, but with an `F` suffix, such as `1F + 2F`.
- **Char**: A type that represents a 16-bit Unicode character. Char values can be compared using the operators `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- **String**: A type that represents a sequence of characters. String values can be concatenated using the `+` operator, and compared using the operators `==`, `!=`, `<`, `>`, `<=`, and `>=`. Strings also have many methods that can be used to manipulate them, such as `length`, `substring`, `trim`, `toUpperCase`, `toLowerCase`, etc.