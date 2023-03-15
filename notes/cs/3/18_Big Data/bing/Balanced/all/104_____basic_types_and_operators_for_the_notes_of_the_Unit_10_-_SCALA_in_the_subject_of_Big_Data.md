# Basic Types and Operators

## Basic Types

- Scala has a rich set of basic types, including `String`, `Int`, `Long`, `Short`, `Byte`, `Float`, `Double`, `Char`, and `Boolean`.
- All basic types are objects, not primitives, and inherit from the class `AnyVal`.
- Basic types can be declared with the `val` or `var` keyword, followed by a colon and the type name.
- For example, `val x: Int = 10` declares a constant integer named `x` with the value `10`.
- Basic types can also be inferred by the compiler, so the type name can be omitted if the value is known.
- For example, `val y = 20` also declares a constant integer named `y` with the value `20`.
- Basic types have methods and properties that can be accessed with the dot notation, such as `x.toBinaryString` or `y.max(100)`.
- Basic types can also be converted to other types with methods such as `x.toDouble` or `y.toString`.

## Operators

- Scala has a rich set of operators that can be applied to basic types, such as arithmetic, relational, logical, bitwise, and assignment operators.
- Operators are actually methods that can be invoked with the infix notation, such as `x + y` or `x < y`.
- Operators can also be invoked with the dot notation, such as `x.+(y)` or `x.<(y)`.
- Operators are evaluated based on the priority of the first character, from highest to lowest: `* / %`, `+ -`, `:`, `< >`, `= !`, `&`, `^`, `|`, `(all letters, $, _)`.
- For example, `x + y * z` is equivalent to `x + (y * z)`, not `(x + y) * z`.
- Operators can be overloaded by defining methods with the same name as the operator, such as `def +(other: Int): Int = ...`.
- Operators can also be defined with symbolic names, such as `def ++(other: Int): Int = ...`.
- Operators can be used to create custom data types, such as vectors, matrices, fractions, etc.