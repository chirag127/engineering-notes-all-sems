# Basic Types and Operators

## Basic Types

- Scala has a rich set of basic types, including `String`, `Int`, `Long`, `Short`, `Byte`, `Float`, `Double`, `Char`, and `Boolean`.
- All basic types are objects, not primitives, and inherit from the class `AnyVal`.
- Basic types can be declared using the `val` or `var` keywords, followed by a colon and the type name.
- For example, `val x: Int = 10` declares a constant integer named `x` with the value `10`.
- Basic types can also be inferred by the compiler, so the type name can be omitted if the value is known.
- For example, `val y = 20` also declares a constant integer named `y` with the value `20`.
- Basic types can be converted to other types using methods like `toInt`, `toLong`, `toFloat`, `toDouble`, etc.
- For example, `val z = x.toDouble` converts the integer `x` to a double named `z`.
- Basic types can also be converted to strings using the `toString` method or the `s` string interpolator.
- For example, `val s = s"The value of x is $x"` creates a string named `s` with the value `"The value of x is 10"`.

## Operators

- Scala supports a variety of operators that can be applied to basic types, such as arithmetic, relational, logical, bitwise, and assignment operators.
- Operators are actually methods that can be invoked using the infix notation, which means placing the operator between the operands.
- For example, `x + y` is equivalent to `x.+(y)`, which invokes the `+` method on the object `x` with the argument `y`.
- Operators can also be invoked using the prefix or postfix notation, which means placing the operator before or after the operand.
- For example, `-x` is equivalent to `x.unary_-`, which invokes the `unary_-` method on the object `x`.
- Operators can also be defined as custom methods on user-defined classes, as long as they follow the naming conventions and precedence rules.
- For example, `class Complex(val re: Double, val im: Double) { def +(that: Complex) = new Complex(this.re + that.re, this.im + that.im) }` defines a class `Complex` that represents complex numbers and a `+` method that adds two complex numbers.
- Operators are evaluated based on the priority of the first character, from highest to lowest: `* / %`, `+ -`, `:`, `< >`, `= !`, `&`, `^`, `|`, `(all letters, $, _)`.
- Operators with the same priority are evaluated from left to right, except for assignment operators, which are evaluated from right to left.
- Operators can be grouped using parentheses to change the order of evaluation.
- For example, `(x + y) * z` evaluates the addition before the multiplication, while `x + (y * z)` evaluates the multiplication before the addition.