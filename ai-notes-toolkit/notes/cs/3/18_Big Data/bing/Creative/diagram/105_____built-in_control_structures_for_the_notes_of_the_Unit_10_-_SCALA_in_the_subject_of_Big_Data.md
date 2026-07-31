### Built-in Control Structures

Scala has only a few built-in control structures, which are:

- `if` expressions: These are used to evaluate a condition and return a value based on whether the condition is true or false. For example:

```scala
val x = 10
val y = if (x > 0) "positive" else "negative"
// y is "positive"
```

- `while` loops: These are used to execute a block of code repeatedly as long as a condition is true. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
// prints 0 to 9
```

- `for` loops and expressions: These are used to iterate over collections, ranges, or generators, and optionally apply filters or transformations. For example:

```scala
for (i <- 1 to 5) {
  println(i)
}
// prints 1 to 5

val squares = for (i <- 1 to 10) yield i * i
// squares is Vector(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

- `try` expressions: These are used to handle exceptions that may occur during the execution of a block of code. For example:

```scala
try {
  val n = 10 / 0 // throws ArithmeticException
} catch {
  case e: ArithmeticException => println("Cannot divide by zero")
} finally {
  println("This is always executed")
}
// prints "Cannot divide by zero" and "This is always executed"
```

- `match` expressions: These are used to match a value against a series of patterns and execute a corresponding block of code. For example:

```scala
val color = "red"
val message = color match {
  case "red" => "Stop"
  case "green" => "Go"
  case "yellow" => "Slow down"
  case _ => "Invalid color"
}
// message is "Stop"
```

- Function calls: These are used to invoke a function with some arguments and return a value. For example:

```scala
def add(x: Int, y: Int): Int = x + y
val z = add(2, 3)
// z is 5
```

The reason Scala has so few built-in control structures is that it has included function literals (also known as anonymous functions or lambdas) since its inception. Function literals allow the creation of new control structures by passing functions as arguments to other functions. For example, the `foreach` method of collections takes a function literal as an argument and applies it to each element of the collection. For example:

```scala
val numbers = List(1, 2, 3, 4, 5)
numbers.foreach(n => println(n * 2))
// prints 2, 4, 6, 8, 10
```

This way, Scala can achieve the same functionality as other languages with more built-in control structures, but with less syntax and more flexibility.