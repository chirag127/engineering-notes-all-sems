# Built-in Control Structures

Scala has only a handful of built-in control structures. The only control structures are **if, while, for, try, match, and function calls** . The reason Scala has so few is that it has included **function literals** since its inception. Function literals are expressions that represent functions, and they can be passed as arguments to other functions or returned as results. This allows Scala to support **higher-order functions**, which are functions that take other functions as parameters or return them as results. Higher-order functions can be used to implement many common control structures as library functions, such as map, filter, reduce, etc.

Some of the built-in control structures in Scala are:

- **if** expressions: Scala's if is an expression that results in a value. The value can be assigned to a variable or used in other expressions. For example:

```scala
val fileName = if (!args.isEmpty) args(0) else "default.txt"
```

This assigns the first argument to fileName if it exists, or "default.txt" otherwise.

- **while** loops: Scala's while is similar to Java's while, except that it does not return a value. It is used for side effects, such as printing or updating variables. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
```

This prints the numbers from 0 to 9.

- **for** loops and expressions: Scala's for is more powerful and expressive than Java's for. It can iterate over collections, ranges, generators, filters, and definitions. It can also yield a value for each iteration, creating a new collection. For example:

```scala
val nums = List(1, 2, 3, 4, 5)
val squares = for (n <- nums) yield n * n
```

This creates a new list of squares from the original list of numbers .

- **try** expressions: Scala's try is similar to Java's try, except that it is also an expression that returns a value. It can be used with catch clauses to handle exceptions, and with finally clauses to execute some code regardless of the outcome. For example:

```scala
val url = try {
  new URL("https://www.scala-lang.org")
} catch {
  case e: MalformedURLException => new URL("https://www.example.com")
} finally {
  println("Done")
}
```

This tries to create a URL from a string, and returns a default URL if it fails. It also prints "Done" at the end.

- **match** expressions: Scala's match is similar to Java's switch, except that it is more general and powerful. It can match on any type of value, including numbers, strings, booleans, case classes, tuples, etc. It can also use patterns, guards, and variables to match on different conditions. It returns a value for each case. For example:

```scala
val color = "red"
val message = color match {
  case "red" => "Stop"
  case "green" => "Go"
  case "yellow" => "Slow down"
  case _ => "Invalid color"
}
```

This matches the color variable to a string and returns a corresponding message .

- **function calls**: Scala's function calls are similar to Java's method calls, except that they can also use infix notation, named arguments, default arguments, and variable arguments. For example:

```scala
def add(x: Int, y: Int = 0): Int = x + y
val sum1 = add(1, 2) // normal call
val sum2 = add(x = 1, y = 2) // named arguments
val sum3 = add(1) // default argument
val sum4 = 1 + 2 // infix notation
def printAll(args: String*): Unit = args.foreach(println)
printAll("Hello", "World") // variable arguments
```

These are some examples of function calls in Scala .