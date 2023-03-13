#### Basic types and operators in Scala

- Scala has a rich set of built-in types, such as `Int`, `Double`, `Boolean`, `String`, etc.
- Scala also supports user-defined types, such as classes, traits, and objects.
- Scala has a unified type system, which means that every value is an object and every operation is a method call.
- Scala has two main categories of types: value types and reference types.
- Value types are stored directly on the stack or embedded in objects, and they have no identity. Examples of value types are `Int`, `Double`, `Char`, `Boolean`, etc.
- Reference types are stored on the heap and they have an identity. Examples of reference types are `String`, `Array`, `List`, etc.
- Scala has a special type called `Unit`, which represents the absence of a meaningful value. It is similar to `void` in Java, but it is an object. The only value of type `Unit` is `()`.
- Scala has a special type called `Nothing`, which represents the bottom of the type hierarchy. It is a subtype of every other type, but it has no values. It is used to indicate abnormal termination, such as throwing an exception.
- Scala has a special type called `Any`, which represents the top of the type hierarchy. It is a supertype of every other type, and it has two direct subtypes: `AnyVal` and `AnyRef`.
- `AnyVal` is the parent type of all value types, and `AnyRef` is the parent type of all reference types. `AnyRef` is equivalent to `java.lang.Object` in Java.
- Scala has a rich set of operators, which are actually methods defined on types. For example, `+` is a method defined on `Int`, `Double`, `String`, etc.
- Scala allows user-defined operators, which are methods with symbolic names, such as `++`, `::`, `+=`, etc.
- Scala supports operator precedence and associativity, which determine the order of evaluation of operators. For example, `*` has higher precedence than `+`, and `+` is left-associative, which means that `a + b + c` is equivalent to `(a + b) + c`.
- Scala supports infix, prefix, and postfix notation for operators, which are syntactic sugar for method calls. For example, `a + b` is equivalent to `a.+(b)`, `!a` is equivalent to `a.unary_!`, and `a++` is equivalent to `a.++()`.
- Scala supports compound assignment operators, such as `+=`, `-=`, `*=`, etc., which are shorthand for assigning the result of an operation to a variable. For example, `a += b` is equivalent to `a = a + b`.
- Scala supports relational and logical operators, such as `==`, `!=`, `<`, `>`, `&&`, `||`, etc., which are used to compare values and produce boolean results.
- Scala supports bitwise operators, such as `&`, `|`, `^`, `~`, `<<`, `>>`, etc., which are used to manipulate bits of integers.
- Scala supports special operators, such as `??`, `?:`, `->`, `<-`, etc., which are used for various purposes, such as null handling, conditional expressions, tuples, pattern matching, etc.