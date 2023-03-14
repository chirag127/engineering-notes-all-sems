Scala has a rich set of basic types and operators that can be used to manipulate them. The basic types are:

- Byte: an 8-bit signed integer, ranging from -128 to 127
- Short: a 16-bit signed integer, ranging from -32768 to 32767
- Int: a 32-bit signed integer, ranging from -2147483648 to 2147483647
- Long: a 64-bit signed integer, ranging from -9223372036854775808 to 9223372036854775807
- Float: a 32-bit floating-point number, ranging from -3.4028235E38 to 3.4028235E38
- Double: a 64-bit floating-point number, ranging from -1.7976931348623157E308 to 1.7976931348623157E308
- Char: a 16-bit unsigned character, ranging from 0 to 65535
- String: a sequence of characters, enclosed in double quotes
- Boolean: a logical value, either true or false

The operators that can be used on these types are:

- Arithmetic operators: +, -, *, /, %, ** (exponentiation)
- Relational operators: ==, !=, <, >, <=, >=
- Logical operators: &&, ||, ! (and, or, not)
- Bitwise operators: &, |, ^, ~, <<, >>, >>> (and, or, xor, complement, left shift, right shift, unsigned right shift)
- Assignment operators: =, +=, -=, *=, /=, %=, **=, &=, |=, ^=, <<=, >>=, >>>=
- Unary operators: +, -, !, ~ (positive, negative, not, complement)

The following diagram illustrates the basic types and operators in Scala:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Numeric     |    |    Boolean     |    |    String      |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    Byte        |    |    true        |    |    "Hello"     |
|    Short       |    |    false       |    |    "World"     |
|    Int         |    |                |    |                |
|    Long        |    +----------------+    +----------------+
|    Float       |    |                |    |                |
|    Double      |    |    && || !     |    |    + *         |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    + - * / %   |    |                |    |                |
|    **          |    +----------------+    +----------------+
|                |    |                |    |                |
|    == != < >   |    |    Bitwise     |    |    == !=       |
|    <= >=       |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    = += -=     |    |    & | ^ ~     |    |    = +=        |
|    *= /= %=    |    |    << >> >>>   |    |                |
|    **=         |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|    + -         |    |                |    |                |
|    ! ~         |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```