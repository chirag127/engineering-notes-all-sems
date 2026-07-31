#### Built-in control structures in Scala

- Scala has only a handful of built-in control structures: **if, while, for, try, match, and function calls**  .
- The reason Scala has so few is that it has included **function literals** since its inception . A function literal is a function that is not defined by a name, but by its parameters and body, such as `(a:Int, b:Int) => a + b`.
- Scala's control structures are closer to the **functional style** than the imperative style. This means that they are expressions that return a value, rather than statements that perform side effects.
- Some examples of Scala's control structures are:

  - **if/else**: This is a conditional expression that evaluates a condition and returns one value if it is true, and another value if it is false. For example:

    ```scala
    val x = 10
    val y = if (x > 0) "positive" else "negative"
    // y is "positive"
    ```

  - **while**: This is a loop that executes a block of code repeatedly as long as a condition is true. For example:

    ```scala
    var i = 0
    while (i < 10) {
      println(i)
      i += 1
    }
    // prints 0 to 9
    ```

  - **for**: This is a loop that iterates over a collection or a range of values, and optionally applies a filter or a transformation. For example:

    ```scala
    for (i <- 1 to 10 if i % 2 == 0) {
      println(i)
    }
    // prints 2, 4, 6, 8, 10
    ```

  - **try/catch/finally**: This is a way to handle exceptions that may occur during the execution of a block of code. The try block contains the code that may throw an exception, the catch block contains the code that handles the exception, and the finally block contains the code that is always executed regardless of the exception. For example:

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

  - **match**: This is a way to pattern match on a value and execute different code depending on the case. The match expression has a value to match on, and a series of cases that specify a pattern and a corresponding value or action. For example:

    ```scala
    val x = 10
    val y = x match {
      case 0 => "zero"
      case 1 => "one"
      case _ => "other" // default case
    }
    // y is "other"
    ```

  - **function calls**: This is a way to invoke a function with some arguments and get a result. A function can be defined by a name, or by a function literal. For example:

    ```scala
    def add(a: Int, b: Int): Int = a + b // named function
    val mul = (a: Int, b: Int) => a * b // function literal
    val x = add(2, 3) // function call
    val y = mul(2, 3) // function call
    // x is 5, y is 6
    ```