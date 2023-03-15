### Basic Types and Operators

Scala has a rich set of basic types and operators that can be used to manipulate data and perform computations. Here are some of the main topics covered in this section:

- Scala has nine basic types: `Byte`, `Short`, `Int`, `Long`, `Float`, `Double`, `Char`, `Boolean`, and `String`. All of them are objects, not primitives, and inherit from the `AnyVal` class.
- Scala supports both mutable (`var`) and immutable (`val`) variables. Mutable variables can be reassigned, while immutable variables cannot.
- Scala has a concise syntax for declaring variables and assigning values. For example, `val x = 10` declares an immutable variable `x` of type `Int` and assigns it the value `10`.
- Scala has a rich set of operators that can be used to perform arithmetic, logical, relational, bitwise, and string operations. Operators are actually methods that can be invoked using infix notation. For example, `x + y` is equivalent to `x.+(y)`.
- Scala has operator precedence rules that determine the order of evaluation of expressions. The precedence is based on the first character of the operator. For example, `*` has higher precedence than `+`, so `x + y * z` is equivalent to `x + (y * z)`.
- Scala has operator associativity rules that determine how operators of the same precedence are grouped. The associativity is based on the last character of the operator. For example, `+` and `-` are left-associative, so `x + y - z` is equivalent to `(x + y) - z`. However, `:` is right-associative, so `x :: y :: z` is equivalent to `x :: (y :: z)`.
- Scala has some special operators that have special meanings or syntax. For example, `=` is used for assignment, `==` is used for equality comparison, `()` is used for function invocation, `.` is used for member access, and `;` is used for statement separation.