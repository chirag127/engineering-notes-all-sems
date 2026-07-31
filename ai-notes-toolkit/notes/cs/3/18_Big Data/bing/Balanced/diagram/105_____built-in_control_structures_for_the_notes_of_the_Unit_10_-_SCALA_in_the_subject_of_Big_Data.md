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

- `for` loops and expressions: These are used to iterate over collections, ranges, or generators. They can also be used to create new collections by applying a transformation or a filter to each element. For example:

```scala
for (i <- 1 to 5) {
  println(i)
}
// prints 1 to 5

val squares = for (i <- 1 to 5) yield i * i
// squares is Vector(1, 4, 9, 16, 25)
```

- `try` expressions: These are used to handle exceptions that may occur during the execution of a block of code. They can also be used to ensure that some code is executed regardless of whether an exception is thrown or not. For example:

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

- `match` expressions: These are used to match a value against a series of patterns and execute a corresponding block of code. They can also be used to extract values from complex data structures. For example:

```scala
val color = "red"
val message = color match {
  case "red" => "Stop"
  case "green" => "Go"
  case "yellow" => "Slow down"
  case _ => "Invalid color"
}
// message is "Stop"

val person = ("Alice", 25)
val greeting = person match {
  case (name, age) => s"Hello, $name. You are $age years old."
  case _ => "Who are you?"
}
// greeting is "Hello, Alice. You are 25 years old."
```

- Function calls: These are used to invoke a function with some arguments and return a value. Functions can be defined using the `def` keyword or as anonymous function literals. For example:

```scala
def add(x: Int, y: Int): Int = x + y
// add is a function that takes two Ints and returns an Int

val multiply = (x: Int, y: Int) => x * y
// multiply is a function literal that takes two Ints and returns an Int

val sum = add(2, 3)
// sum is 5

val product = multiply(2, 3)
// product is 6
```