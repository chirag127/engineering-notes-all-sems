#### Built-in control structures in Scala

Scala has several built-in control structures that can be used to write concise and expressive code. Some of the most common ones are:

- `if-else`: This is a conditional expression that evaluates a boolean condition and returns one of two values depending on whether the condition is true or false. For example:

```scala
val x = 10
val y = if (x > 0) "positive" else "negative"
// y is "positive"
```

- `while`: This is a loop that executes a block of code repeatedly as long as a boolean condition is true. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
// prints 0 to 9
```

- `for`: This is a loop that iterates over a collection or a range of values and executes a block of code for each element. For example:

```scala
for (i <- 1 to 5) {
  println(i * i)
}
// prints 1, 4, 9, 16, 25
```

- `match`: This is a pattern matching expression that compares a value with a series of cases and returns the value associated with the first matching case. For example:

```scala
val color = "red"
val message = color match {
  case "red" => "stop"
  case "green" => "go"
  case "yellow" => "slow down"
  case _ => "unknown color"
}
// message is "stop"
```

- `try-catch-finally`: This is a way of handling exceptions that may occur during the execution of a block of code. The `try` block contains the code that may throw an exception, the `catch` block contains the code that handles the exception, and the `finally` block contains the code that is always executed regardless of whether an exception occurs or not. For example:

```scala
try {
  val n = 10 / 0 // throws an ArithmeticException
  println(n)
} catch {
  case e: ArithmeticException => println("cannot divide by zero")
} finally {
  println("this is always executed")
}
// prints "cannot divide by zero" and "this is always executed"
```