### Basic Types and Operators

- Scala has a rich set of basic types, including numeric, boolean, string, and character types.
- Scala also supports operators on these types, which can be used in infix, prefix, or postfix notation.
- Scala operators are actually methods that can be defined or overridden by user-defined types.

#### Numeric Types

- Scala has eight numeric types: `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`, `Char`, and `BigInt`.
- `Byte`, `Short`, `Int`, and `Long` are signed integer types of 8, 16, 32, and 64 bits respectively.
- `Float` and `Double` are floating-point types of 32 and 64 bits respectively.
- `Char` is an unsigned 16-bit type that represents a Unicode character.
- `BigInt` is an arbitrary-precision integer type that can hold any integer value.
- Scala supports the following arithmetic operators on numeric types: `+`, `-`, `*`, `/`, and `%`.
- Scala also supports the following bitwise operators on integer types: `&`, `|`, `^`, `~`, `<<`, `>>`, and `>>>`.
- Scala also supports the following comparison operators on numeric types: `<`, `<=`, `>`, `>=`, `==`, and `!=`.
- Scala also supports the following unary operators on numeric types: `+`, `-`, and `!`.
- Scala also supports implicit conversions between numeric types, such as widening and narrowing conversions.

#### Boolean Type

- Scala has a boolean type, `Boolean`, that can have two values: `true` and `false`.
- Scala supports the following logical operators on boolean values: `&&`, `||`, and `!`.
- Scala also supports the following comparison operators on boolean values: `==` and `!=`.

#### String Type

- Scala has a string type, `String`, that represents a sequence of characters.
- Scala supports the following operators on strings: `+`, which concatenates two strings, and `*`, which repeats a string a given number of times.
- Scala also supports the following methods on strings: `length`, which returns the number of characters in a string, `charAt`, which returns the character at a given index, `substring`, which returns a part of a string, `indexOf`, which returns the first occurrence of a character or a substring, `lastIndexOf`, which returns the last occurrence of a character or a substring, `startsWith`, which checks if a string starts with a given prefix, `endsWith`, which checks if a string ends with a given suffix, `toLowerCase`, which converts a string to lower case, `toUpperCase`, which converts a string to upper case, `trim`, which removes leading and trailing whitespace, `split`, which splits a string by a given delimiter, `replace`, which replaces all occurrences of a character or a substring with another, `format`, which formats a string with given arguments, and `interpolate`, which inserts values of variables or expressions into a string.
- Scala also supports string interpolation, which allows embedding expressions inside strings using the `s` prefix, such as `s"Hello, $name!"`.
- Scala also supports multi-line strings, which are enclosed by triple quotes, such as `"""This is a multi-line string"""`.

#### Character Type

- Scala has a character type, `Char`, that represents a single Unicode character.
- Scala supports the following operators on characters: `+`, which adds the numeric value of a character to another character or an integer, and `-`, which subtracts the numeric value of a character from another character or an integer.
- Scala also supports the following methods on characters: `isDigit`, which checks if a character is a digit, `isLetter`, which checks if a character is a letter, `isLower`, which checks if a character is a lower case letter, `isUpper`, which checks if a character is an upper case letter, `isWhitespace`, which checks if a character is a whitespace, `toLower`, which converts a character to lower case, and `toUpper`, which converts a character to upper case.
- Scala also supports escape sequences for special characters, such as `\n` for newline, `\t` for tab, `\\` for backslash, `\"` for double quote, and `\'` for single quote.