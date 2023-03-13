#### Built-in control structures in Scala

Scala has several built-in control structures that can be used to write concise and expressive code. Some of the most common ones are:

- **if-else**: This is a conditional expression that evaluates a boolean condition and executes one of two branches depending on whether the condition is true or false. For example:

```scala
val x = 10
val y = if (x > 0) "positive" else "negative" // y is "positive"
```

- **while**: This is a loop that executes a block of code repeatedly as long as a boolean condition is true. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
```

- **for**: This is a loop that iterates over a collection or a range of values and executes a block of code for each element. For example:

```scala
for (i <- 1 to 10) {
  println(i)
}
```

- **match**: This is a pattern matching expression that compares a value with a series of cases and executes the first case that matches. For example:

```scala
val x = 10
val y = x match {
  case 0 => "zero"
  case 1 => "one"
  case _ => "other" // default case
} // y is "other"
```

- **try-catch-finally**: This is an exception handling expression that tries to execute a block of code and catches any exceptions that may occur. It can also execute a block of code regardless of whether an exception occurs or not. For example:

```scala
try {
  val x = 10 / 0 // throws an ArithmeticException
} catch {
  case e: ArithmeticException => println("Cannot divide by zero")
} finally {
  println("This is always executed")
}
```

Some of the advantages of using these built-in control structures are:

- They are concise and expressive, avoiding unnecessary boilerplate code.
- They are consistent and uniform, following the same syntax and semantics as other expressions in Scala.
- They are functional and immutable, returning values instead of modifying variables or performing side effects.

Some of the disadvantages of using these built-in control structures are:

- They may not be familiar to programmers coming from other languages that use different syntax or semantics for control structures.
- They may not cover all the possible scenarios or use cases that require more complex or custom logic.

Some of the mnemonics and learning tricks for these built-in control structures are:

- **if-else**: Remember that it is an expression that returns a value, not a statement that performs an action. Think of it as a ternary operator in other languages.
- **while**: Remember that it is a loop that checks the condition before executing the block of code. Think of it as a "pre-test" loop.
- **for**: Remember that it is a loop that iterates over a collection or a range of values. Think of it as a "foreach" loop or a "for-in" loop in other languages.
- **match**: Remember that it is a pattern matching expression that compares a value with a series of cases. Think of it as a "switch" statement or a "case" statement in other languages, but more powerful and flexible.
- **try-catch-finally**: Remember that it is an exception handling expression that tries to execute a block of code and catches any exceptions that may occur. Think of it as a "try-except-finally" statement or a "try-catch-finally" statement in other languages.