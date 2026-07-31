#### Basic Types and Operators in Scala

- Scala has a rich set of basic types, including numeric, character, string, and boolean types.
- Scala also supports operators, which are symbols or words that perform operations on operands, such as arithmetic, relational, logical, bitwise, and assignment operations.
- Scala operators are actually methods that can be defined or overloaded for custom types.
- Scala operators follow a precedence rule based on the first character of the operator, and an associativity rule based on the last character of the operator.
- Scala operators can be used in infix, prefix, or postfix notation, depending on the number and position of the operands.

Some examples of basic types and operators in Scala are:

- Numeric types: `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`, and `BigInt` and `BigDecimal` for arbitrary precision arithmetic.
- Numeric literals: `42`, `0x2A`, `052`, `3.14`, `1.23e4`, `1.23f`, `3L`, `42d`, `0x2aL`, etc.
- Numeric operators: `+`, `-`, `*`, `/`, `%`, `**` (power), `abs`, `max`, `min`, etc.
- Character type: `Char`, which represents a 16-bit Unicode character.
- Character literals: `'a'`, `'\n'`, `'\u0041'`, etc.
- Character operators: `+` (concatenation), `toUpper`, `toLower`, `isDigit`, `isLetter`, etc.
- String type: `String`, which represents a sequence of characters.
- String literals: `"Hello"`, `"""Multi-line string"""`, `s"Interpolated $string"`, `f"Formatted $number%.2f"`, etc.
- String operators: `+` (concatenation), `length`, `charAt`, `substring`, `indexOf`, `startsWith`, `endsWith`, `split`, `trim`, `replace`, etc.
- Boolean type: `Boolean`, which represents a logical value of either `true` or `false`.
- Boolean literals: `true`, `false`.
- Boolean operators: `!` (negation), `&&` (logical and), `||` (logical or), `^` (logical xor), `==` (equality), `!=` (inequality), `<`, `>`, `<=`, `>=` (comparison), etc.
- Bitwise type: `Int`, `Long`, `Byte`, `Short`, which support bitwise operations on their binary representation.
- Bitwise operators: `&` (bitwise and), `|` (bitwise or), `^` (bitwise xor), `~` (bitwise complement), `<<` (left shift), `>>` (right shift), `>>>` (unsigned right shift), etc.
- Assignment type: Any type that supports an assignment operation, which assigns a value to a variable or a field.
- Assignment operators: `=` (simple assignment), `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=` (compound assignment), etc.