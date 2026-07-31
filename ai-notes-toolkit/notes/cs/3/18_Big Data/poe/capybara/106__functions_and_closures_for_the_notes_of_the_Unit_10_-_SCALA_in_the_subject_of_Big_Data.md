### Functions and Closures

Scala has a powerful system for defining functions and closures, which are essential for programming in a functional style. Here are some important points to keep in mind:

- In Scala, functions are first-class citizens. This means that they can be treated like any other value, such as an integer or a string. You can pass functions as arguments to other functions, return them as values, and store them in variables.

- Functions can be defined using the `def` keyword, followed by the function name, parameter list, and return type. For example, the following function takes two integers and returns their sum:

  ```scala
  def add(x: Int, y: Int): Int = {
    x + y
  }
  ```

- Functions can also be defined anonymously using the `=>` symbol. These are called closures, and they can capture values from their surrounding environment. For example, the following closure takes an integer `x` and returns a function that adds `x` to its argument:

  ```scala
  val addX = (x: Int) => (y: Int) => x + y
  ```

- Closures can be used to create higher-order functions, which are functions that take other functions as arguments or return functions as values. For example, the following function takes a function `f` and an integer `n`, and applies `f` to `n` times to an initial value `x`:

  ```scala
  def repeat(f: Int => Int, n: Int, x: Int): Int = {
    if (n == 0) x
    else repeat(f, n - 1, f(x))
  }
  ```

- Scala provides several built-in higher-order functions, such as `map`, `filter`, and `reduce`. These functions operate on collections (such as lists or arrays) and apply a function to each element or combine the elements in some way. For example, the following code uses `map` to square each element of a list:

  ```scala
  val list = List(1, 2, 3, 4, 5)
  val squares = list.map(x => x * x)
  ```

- In Scala, functions can have multiple parameter lists. This can be useful for currying, which is the process of transforming a function that takes multiple arguments into a chain of functions that each take a single argument. For example, the following function takes two integers and returns a function that takes a third integer and returns their sum:

  ```scala
  def addCurried(x: Int)(y: Int)(z: Int): Int = {
    x + y + z
  }
  ```

- Functions in Scala are also objects, which means they can have methods and fields just like any other object. For example, the following function defines a field `name` and a method `greet`:

  ```scala
  val sayHello = (name: String) => {
    val greeting = "Hello"
    def greet() = s"$greeting, $name!"
    greet
  }
  val helloBob = sayHello("Bob")
  helloBob() // returns "Hello, Bob!"
  ```