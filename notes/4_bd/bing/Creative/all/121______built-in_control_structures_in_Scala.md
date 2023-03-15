#### Built-in control structures in Scala

Scala has only a few built-in control structures that are essential for programming. They are:

- **if/else**: This is a conditional expression that evaluates a boolean expression and executes one branch or another depending on the result. For example:

```scala
val x = 10
val y = if (x > 0) "positive" else "negative"
// y is "positive"
```

- **while**: This is a loop that executes a block of code repeatedly as long as a boolean condition is true. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
// prints 0 to 9
```

- **for**: This is a versatile construct that can iterate over collections, ranges, generators, filters, and more. It can also produce a new collection as a result of the iteration. For example:

```scala
val nums = List(1, 2, 3, 4, 5)
val squares = for (n <- nums) yield n * n
// squares is List(1, 4, 9, 16, 25)
```

- **try/catch/finally**: This is a mechanism for handling exceptions that may occur during the execution of a block of code. The try block contains the code that may throw an exception, the catch block contains one or more case clauses that match different types of exceptions and handle them accordingly, and the finally block contains the code that is always executed regardless of whether an exception is thrown or not. For example:

```scala
try {
  val n = 10 / 0 // throws ArithmeticException
} catch {
  case e: ArithmeticException => println("Division by zero")
  case e: Exception => println("Some other exception")
} finally {
  println("This is always executed")
}
// prints "Division by zero" and "This is always executed"
```

- **match**: This is a powerful expression that can match a value against a series of patterns and execute a corresponding block of code for the first matching pattern. It can also extract values from complex data structures and assign them to variables. For example:

```scala
val color = "red"
val message = color match {
  case "red" => "Stop"
  case "green" => "Go"
  case "yellow" => "Slow down"
  case _ => "Invalid color" // default case
}
// message is "Stop"
```

- **function calls**: This is the basic way of invoking a function or a method with some arguments and getting a result. Functions can be defined as named or anonymous, and can be passed as values to other functions. For example:

```scala
def add(a: Int, b: Int): Int = a + b // named function
val mul = (a: Int, b: Int) => a * b // anonymous function
val sum = add(2, 3) // function call
val product = mul(2, 3) // function call
// sum is 5, product is 6
```

These are the built-in control structures in Scala. They are sufficient for most programming tasks, and can be combined with function literals and other features to create more complex and expressive programs.