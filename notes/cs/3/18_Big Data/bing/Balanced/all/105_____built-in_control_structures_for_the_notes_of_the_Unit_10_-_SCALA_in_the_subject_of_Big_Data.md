# Built-in Control Structures

Scala has only a handful of built-in control structures. The only control structures are `if`, `while`, `for`, `try`, `match`, and function calls. The reason Scala has so few is that it has included function literals since its inception.

- `if` is an expression that returns a value based on a condition. It can be used with `else` to form an alternative branch. For example:

```scala
val x = 10
val y = if (x > 0) 1 else -1 // y is 1
```

- `while` is a loop that executes a block of code repeatedly as long as a condition is true. It does not return any value. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
```

- `for` is a loop that iterates over a collection or a range of values. It can also be used as an expression that returns a new collection by applying a transformation to each element. For example:

```scala
for (i <- 1 to 10) println(i) // prints 1 to 10
val squares = for (i <- 1 to 10) yield i * i // squares is Vector(1, 4, 9, ..., 100)
```

- `try` is an expression that executes a block of code and catches any exceptions that may occur. It can be used with `catch` to handle different types of exceptions and `finally` to perform some cleanup actions. For example:

```scala
try {
  val n = 10 / 0 // throws ArithmeticException
} catch {
  case e: ArithmeticException => println("Division by zero")
} finally {
  println("Done")
}
```

- `match` is an expression that matches a value against a series of patterns and returns a value based on the first matching pattern. It can be used with `case` to specify the patterns and `=>` to separate the patterns from the values. For example:

```scala
val color = "red"
val result = color match {
  case "red" => "stop"
  case "green" => "go"
  case "yellow" => "slow down"
  case _ => "unknown" // default case
}
// result is "stop"
```

- Function calls are expressions that invoke a function with some arguments and return a value. Functions can be defined with the `def` keyword or as function literals. For example:

```scala
def add(x: Int, y: Int) = x + y // defines a function named add
val f = (x: Int, y: Int) => x + y // defines a function literal and assigns it to f
val z = add(2, 3) // calls the add function and assigns the result to z
val w = f(2, 3) // calls the function literal and assigns the result to w
// z and w are both 5
```