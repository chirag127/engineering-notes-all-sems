#### Built-in control structures in Scala

Scala has three main types of built-in control structures: expressions, loops, and exceptions. These are briefly explained below:

- Expressions: Scala is an expression-oriented language, which means that every construct has a value. For example, `if` statements are expressions that return a value based on a condition. Similarly, `match` statements are expressions that return a value based on pattern matching. Expressions can be composed together to form complex expressions that evaluate to a single value.

- Loops: Scala has two main types of loops: `while` and `for`. `while` loops are similar to those in Java or C++, and execute a block of code repeatedly as long as a condition is true. `for` loops are more powerful and flexible, and can iterate over collections, ranges, generators, or filters. `for` loops can also use `yield` to return a new collection based on the loop body.

- Exceptions: Scala supports exceptions as a way of handling errors or abnormal situations. Exceptions are objects that extend the `Throwable` class, and can be thrown and caught using the `throw` and `try-catch-finally` constructs. Scala also has a special type of exception called `scala.util.control.NonFatal`, which covers most common exceptions that are not fatal to the program. Scala encourages the use of `try-catch-finally` over `throw` to avoid breaking the normal flow of the program.