### Basic Types and Operators

Scala has a rich set of basic types and operators that can be used to manipulate data and perform computations. Here are some of the main topics covered in this chapter:

- Scala has nine basic types: `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`, `Char`, `Boolean`, and `String`. All of them are objects, not primitives, and inherit from the `AnyVal` class.
- Scala supports both numeric and boolean operators, such as `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `<`, `>`, `&&`, and `||`. These operators can be used in infix notation, such as `a + b`, or in method notation, such as `a.+(b)`.
- Scala also supports unary operators, such as `-`, `+`, `!`, and `~`, which can be used as prefix operators, such as `-a`, or as methods, such as `a.unary_-`.
- Scala has a special operator `:`, which can be used to create user-defined operators that end with a colon, such as `::` or `+:`. These operators are right-associative, meaning that `a :: b` is equivalent to `b.::(a)`.
- Scala has a precedence rule for operators, which determines the order of evaluation based on the first character of the operator. The rule is as follows:

  - (characters not shown below)
  - `*` `/` `%`
  - `+` `-`
  - `:`
  - `<` `>`
  - `=`
  - `!`
  - `&`
  - `^`
  - `|`
  - (all letters, `$`, `_`)

- Scala also has an associativity rule for operators, which determines the grouping of operands based on the last character of the operator. The rule is as follows:

  - If the operator ends with a colon (`:`), it is right-associative, meaning that `a op b op c` is equivalent to `a op (b op c)`.
  - Otherwise, it is left-associative, meaning that `a op b op c` is equivalent to `(a op b) op c`.