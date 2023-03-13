 Here is the content in markdown format for the topic #### basic types and operators in Scala:

#### Basic Types and Operators in Scala

Scala has the following basic types:

- Int: 32-bit or 64-bit signed integer. Range from -2^31 to 2^31-1 or -2^63 to 2^63-1 respectively.
- Long: 64-bit signed integer. Range from -2^63 to 2^63-1.
- Float: 32-bit IEEE-754 single-precision float.
- Double: 64-bit IEEE-754 double-precision float.
- Char: 16-bit Unicode character.
- Boolean: true or false.
- Unit: equivalent to void in Java. Indicates an expression that performs some side effect but has no meaningful value.

Basic operators in Scala are:

- Arithmetic operators: +, -, *, /, %
- Relational operators: <, >, <=, >=
- Equality operators: ==, !=
- Logical operators: &&, ||, !
- Bitwise operators: &, |, ^, ~, <<, >>

Some mnemonics and learning tricks for basic Scala types:

- Int is for integer, Long for longer integer
- Float floats, Double doubles the precision
- Char is character, Boolean is true/false
- Unit is useless, meant for side-effects

Some examples of basic types and operators:

val x = 5     // Int
val y = 5.6   // Double
val z = 'a'   // Char
val w = true  // Boolean

val addition = x + y   // 10.6
val subtraction = x - y // -1.6
val multiplication = x * y // 28
val division = x / y  // 0
val modulus = x % y   // 5

/* Other operators and comparisons can be tried out similarly. */

Advantages of Scala types:

- Static typing avoids type-related bugs and catches errors early.
- Types inferencing frees from explicitly declaring types in most cases.
- Rich standard library of types.
- Interoperability with Java allows usage of Java APIs.

Disadvantages of Scala types:

- The complex type system has a steep learning curve.
- Explicit type annotations may be needed at times leading to verbosity.
- Int and Long overflow can occur if not handled properly.

Applications of Scala types and operators:

- Scala types and operators form the basic building blocks for any Scala program.
- They are used to define variables, expressions, functions, classes, etc.
- The rich set of types and operators enable Scala to be a powerful language for both imperative and functional programming.
- The interoperability with Java makes the Java APIs accessible to Scala programs.