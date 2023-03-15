#### Basic types and operators in Scala

- Scala has a rich set of built-in types, such as `Int`, `Double`, `Boolean`, `String`, etc.
- Scala also supports user-defined types, such as classes, traits, and objects.
- Scala has a unified type system, which means that every value is an object and every operation is a method call.
- Scala has two main categories of types: value types and reference types.
- Value types are stored directly on the stack or embedded in objects, and they include `Byte`, `Short`, `Int`, `Long`, `Char`, `Float`, `Double`, `Boolean`, and `Unit`.
- Reference types are stored on the heap and they include `AnyRef`, `String`, `Array`, `List`, and user-defined types.
- Scala has a special type called `Any`, which is the supertype of all types, and a special type called `Nothing`, which is the subtype of all types.
- Scala has a special type called `Null`, which is the subtype of all reference types, and a special value called `null`, which is the only instance of `Null`.
- Scala has a special type called `AnyVal`, which is the supertype of all value types, and a special type called `Unit`, which is the subtype of `AnyVal` and has a single value `()`.
- Scala has a special type called `Function`, which is the supertype of all function types, such as `Int => String` or `(Int, String) => Boolean`.
- Scala has a rich set of operators, such as `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `!`, `&`, `|`, `^`, `<<`, `>>`, `>>>`, `+=`, `-=`, `*=`, `/=`, `%=`, `++`, `--`, `::`, `:+`, `+:`, `++:`, `:++`, `apply`, `update`, etc.
- Scala operators are actually methods, which means that `a + b` is equivalent to `a.+(b)`, and `a(b)` is equivalent to `a.apply(b)`.
- Scala operators can be overloaded by defining methods with the same name and signature as the operator.
- Scala operators can be infix, prefix, or postfix, depending on their position and arity.
- Scala operators have precedence and associativity rules, which determine the order of evaluation and grouping of operands.
- Scala operators can be used to create custom DSLs (domain-specific languages), such as `a + b * c` or `a :: b :: c`.