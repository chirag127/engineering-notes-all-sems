### Unit 10 - SCALA: Built-in Control Structures

Scala has several built-in control structures that allow you to control the flow of your program. These include:

1. **If/else statements:** These allow you to execute different blocks of code depending on whether a condition is true or false.

```scala
if (x > 0) {
  println("x is positive")
} else {
  println("x is not positive")
}
```

2. **While loops:** These allow you to execute a block of code repeatedly while a condition is true.

```scala
while (x > 0) {
  println(x)
  x -= 1
}
```

3. **For loops:** These allow you to iterate over a collection of elements.

```scala
for (x <- 1 to 10) {
  println(x)
}
```

4. **Match expressions:** These allow you to match a value against a series of patterns and execute different blocks of code depending on which pattern is matched.

```scala
x match {
  case 1 => println("x is 1")
  case 2 => println("x is 2")
  case _ => println("x is something else")
}
```

5. **Try/catch/finally expressions:** These allow you to handle exceptions that may be thrown during the execution of your code.

```scala
try {
  val result = 10 / x
} catch {
  case e: ArithmeticException => println("Cannot divide by zero")
} finally {
  println("This code is always executed")
}
```

These are some of the built-in control structures in Scala that you can use to control the flow of your program. They are similar to control structures in other programming languages, but with some differences in syntax and usage. It is important to understand how to use these control structures effectively in order to write efficient and readable code in Scala.