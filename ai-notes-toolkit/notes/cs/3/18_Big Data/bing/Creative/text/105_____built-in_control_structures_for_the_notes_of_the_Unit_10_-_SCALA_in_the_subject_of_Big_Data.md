### Built-in Control Structures

Scala has only a handful of built-in control structures  . The only control structures are **if**, **while**, **for**, **try**, **match**, and **function calls**. The reason Scala has so few is that it has included **function literals** since its inception.

- **if**: The if control structure is used to execute a block of code conditionally. It can be used as an expression that returns a value, or as a statement that performs a side effect. The syntax of if is similar to other languages, except that the parentheses around the condition are optional, and the else branch is mandatory if the if is used as an expression .

  Example:

  ```scala
  // if as a statement
  val x = 10
  if (x > 0) println("Positive") else println("Non-positive")

  // if as an expression
  val y = if (x > 0) 1 else -1
  ```

- **while**: The while control structure is used to execute a block of code repeatedly while a condition is true. It can only be used as a statement that performs a side effect, and does not return a value .

  Example:

  ```scala
  // while as a statement
  var i = 0
  while (i < 10) {
    println(i)
    i += 1
  }
  ```

- **for**: The for control structure is used to iterate over collections, ranges, or generators. It can be used as an expression that returns a new collection, or as a statement that performs a side effect. The syntax of for is different from other languages, and uses **<-** to denote a generator, **;** to separate multiple generators, and **yield** to produce a new collection .

  Example:

  ```scala
  // for as a statement
  for (i <- 1 to 10) println(i)

  // for as an expression
  val squares = for (i <- 1 to 10) yield i * i
  ```

- **try**: The try control structure is used to handle exceptions. It can be used as an expression that returns a value, or as a statement that performs a side effect. The syntax of try is similar to other languages, except that the catch clause uses a **match** expression to handle different types of exceptions, and the finally clause is optional .

  Example:

  ```scala
  // try as a statement
  try {
    val n = 10 / 0
  } catch {
    case e: ArithmeticException => println("Division by zero")
    case e: Exception => println("Unknown exception")
  } finally {
    println("Done")
  }

  // try as an expression
  val result = try {
    10 / 0
  } catch {
    case e: ArithmeticException => 0
    case e: Exception => -1
  }
  ```

- **match**: The match control structure is used to match a value against a series of patterns. It can be used as an expression that returns a value, or as a statement that performs a side effect. The syntax of match is similar to a switch statement in other languages, except that the cases are separated by **=>**, the break statement is not needed, and the patterns can be complex expressions .

  Example:

  ```scala
  // match as a statement
  val color = "red"
  color match {
    case "red" => println("Stop")
    case "green" => println("Go")
    case "yellow" => println("Slow down")
    case _ => println("Invalid color")
  }

  // match as an expression
  val message = color match {
    case "red" => "Stop"
    case "green" => "Go"
    case "yellow" => "Slow down"
    case _ => "Invalid color"
  }
  ```

- **function calls**: The function call control structure is used to invoke a function with arguments. It can be used as an expression that returns a value, or as a statement that performs a side effect. The syntax of function calls is similar to other languages, except that the parentheses around the arguments are optional for functions with one argument, and the