#### Basic Types and Operators in Scala

- Scala has a rich set of built-in types, including numeric, character, string, and boolean types.
- Scala also supports user-defined types, such as classes, traits, and objects.
- Scala has a unified type system, which means that every value is an object and every operation is a method call.
- Scala operators are actually methods that can be defined or overloaded for any type.
- Scala operators follow a precedence and associativity rule based on the first character of the operator name.

##### Numeric Types

- Scala has four numeric types: Byte, Short, Int, and Long, which are 8-bit, 16-bit, 32-bit, and 64-bit signed integers, respectively.
- Scala also has two floating-point types: Float and Double, which are 32-bit and 64-bit IEEE 754 numbers, respectively.
- Scala does not have an explicit unsigned integer type, but it allows bitwise operations on signed integers as if they were unsigned.
- Scala numeric literals can be written in decimal, hexadecimal, or binary notation, and can have a suffix of L, F, or D to indicate the type.
- Scala numeric types support the usual arithmetic operators, such as +, -, *, /, and %, as well as bitwise operators, such as &, |, ^, and ~, and shift operators, such as <<, >>, and >>>.
- Scala numeric types also have methods for conversion, comparison, and rounding, such as toByte, toShort, toInt, toLong, toFloat, toDouble, max, min, abs, round, ceil, and floor.

##### Character and String Types

- Scala has a character type, Char, which is a 16-bit Unicode code unit.
- Scala has a string type, String, which is a sequence of characters.
- Scala string literals can be written in single or double quotes, and can have escape sequences, such as \n, \t, \b, \r, \f, \\, \', and \".
- Scala string literals can also have interpolation, which allows embedding expressions inside strings using the syntax s"$expr", where expr is any valid Scala expression.
- Scala character and string types support the usual comparison operators, such as ==, !=, <, >, <=, and >=, as well as concatenation operator, +, and indexing operator, (), which returns the character at a given position.
- Scala character and string types also have methods for conversion, manipulation, and extraction, such as toChar, toString, length, isEmpty, trim, substring, replace, split, startsWith, endsWith, contains, indexOf, lastIndexOf, matches, and regex.

##### Boolean Type

- Scala has a boolean type, Boolean, which has two possible values: true and false.
- Scala boolean literals can be written as true or false, and can also be the result of expressions using logical operators, such as !, &&, ||, and ==.
- Scala boolean type supports the usual comparison operators, such as ==, !=, <, >, <=, and >=, as well as logical operators, such as !, &&, ||, and ^, and conditional operator, ?, which returns one of two values based on a condition.
- Scala boolean type also has methods for conversion, such as toBoolean, toString, and asInstanceOf.

##### Operator Precedence and Associativity

- When an expression uses multiple operators, the operators are evaluated based on the priority of the first character of the operator name, from highest to lowest:

  - (all other special characters)
  - * / %
  - + -
  - :
  - < >
  - = !
  - & 
  - ^ 
  - |
  - (all letters, $, _)

- If the operators have the same priority, they are evaluated from left to right, except for operators that end with a colon (:), which are evaluated from right to left.
- For example, the expression 1 + 2 * 3 is evaluated as 1 + (2 * 3), and the expression 1 :: 2 :: 3 is evaluated as 1 :: (2 :: 3).