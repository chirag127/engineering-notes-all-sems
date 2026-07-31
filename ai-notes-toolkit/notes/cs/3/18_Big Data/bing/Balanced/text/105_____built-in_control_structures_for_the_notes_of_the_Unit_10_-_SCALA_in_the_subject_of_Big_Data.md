### Built-in Control Structures

Scala has only a handful of built-in control structures. The only control structures are `if`, `while`, `for`, `try`, `match`, and function calls. The reason Scala has so few is that it has included function literals since its inception.

- `if` is an expression that returns a value based on a condition. It can be used as a ternary operator or as a branch statement. For example:

```scala
val x = if (a > b) a else b // x is the maximum of a and b
if (n % 2 == 0) println("even") else println("odd") // prints even or odd
```

- `while` is a loop that executes a block of code repeatedly as long as a condition is true. It is usually used for iterative algorithms or stateful computations. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
```

- `for` is a powerful construct that can express various kinds of iterations, comprehensions, and transformations. It can be used with ranges, collections, generators, filters, and definitions. For example:

```scala
for (i <- 1 to 10) println(i) // prints 1 to 10
for (x <- xs if x > 0) yield x * x // returns a new collection of squares of positive elements
for ((k, v) <- map) println(s"$k -> $v") // prints key-value pairs of a map
```

- `try` is an expression that can handle exceptions using `catch` clauses and perform cleanup actions using `finally` clauses. It can be used for error handling or resource management. For example:

```scala
try {
  val n = input.toInt // may throw NumberFormatException
  println(n)
} catch {
  case e: NumberFormatException => println("invalid input")
} finally {
  input.close() // always close the input
}
```

- `match` is an expression that can pattern match on values and types. It can be used for conditional logic, extraction, or decomposition. For example:

```scala
val x = input match {
  case "yes" => true
  case "no" => false
  case _ => throw new IllegalArgumentException("invalid input")
}

val y = list match {
  case Nil => 0 // empty list
  case head :: tail => head + sum(tail) // non-empty list
}

val z = obj match {
  case s: String => s.length // string
  case i: Int => i * i // integer
  case _ => -1 // anything else
}
```

- Function calls are expressions that invoke a function with some arguments and return a value. They can be used for modularization, abstraction, or higher-order programming. For example:

```scala
def factorial(n: Int): Int = {
  if (n == 0) 1 else n * factorial(n - 1)
}

def map[A, B](f: A => B, xs: List[A]): List[B] = {
  xs match {
    case Nil => Nil
    case head :: tail => f(head) :: map(f, tail)
  }
}

val f = (x: Int) => x + 1 // a function literal
val g = map(f, List(1, 2, 3)) // a higher-order function call
```