#### Built-in Control Structures in Scala

Scala is a multi-paradigm programming language that supports both object-oriented and functional programming. It has a rich set of built-in control structures that allow developers to write concise and expressive code. In this section, we will cover the various built-in control structures in Scala.

##### 1. If-Else Statements

The `if-else` statement is used to conditionally execute a block of code. In Scala, the `if-else` statement can return a value, which makes it very powerful. Here's an example:

```scala
val x = 10
val y = if (x > 5) "greater than 5" else "less than or equal to 5"
```

In this example, `y` will be assigned the value "greater than 5" because the condition `x > 5` is true.

##### 2. For Loops

The `for` loop is used to iterate over a collection of elements. In Scala, the `for` loop can be used with any collection that has an `iterator` method. Here's an example:

```scala
val numbers = List(1, 2, 3, 4, 5)
for (n <- numbers) {
  println(n)
}
```

In this example, the `for` loop iterates over the `numbers` list and prints each element.

##### 3. While Loops

The `while` loop is used to repeatedly execute a block of code while a certain condition is true. Here's an example:

```scala
var i = 0
while (i < 5) {
  println(i)
  i += 1
}
```

In this example, the `while` loop repeatedly prints the value of `i` until it reaches 5.

##### 4. Match Expressions

The `match` expression is used to match a value against a set of patterns and execute a block of code based on the matched pattern. Here's an example:

```scala
val x = 10
val y = x match {
  case 1 => "one"
  case 2 => "two"
  case _ => "many"
}
```

In this example, `x` is matched against the patterns `1`, `2`, and `_` (which matches any value). Since `x` is `10`, it matches the `_` pattern and `y` is assigned the value "many".

##### 5. Try-Catch Expressions

The `try-catch` expression is used to handle exceptions in Scala. Here's an example:

```scala
try {
  // code that might throw an exception
} catch {
  case e: Exception => println(e.getMessage)
} finally {
  // code that will always execute
}
```

In this example, the `try` block contains the code that might throw an exception. If an exception is thrown, the `catch` block will handle it. The `finally` block contains code that will always execute, regardless of whether an exception was thrown or not.

These are some of the most commonly used built-in control structures in Scala. By using these control structures effectively, developers can write concise and expressive code that is easy to read and maintain.