# Functions and Closures in Scala

- A function is a block of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the function name, parameters, return type, and body.
- A function can also be defined as an anonymous function, which is a function without a name, using the `=>` operator.
- A function can be assigned to a variable, passed as an argument to another function, or returned from another function.
- A function can be nested inside another function, creating a local scope for the inner function.
- A function can be a higher-order function, which is a function that can take another function as a parameter or return another function as a result.
- A closure is a special type of function that uses one or more free variables, which are variables that are not declared in the function or its parameters.
- A closure captures the values of the free variables from the surrounding scope, creating a referencing environment for them.
- A closure allows a function to access variables outside its immediate lexical scope, even if they are modified or out of scope.
- A closure can be used to create partially applied functions, which are functions that have some of their parameters fixed by the closure.
- A closure can also be used to create curried functions, which are functions that return another function that takes the remaining parameters.

Some examples of functions and closures in Scala are:

```scala
// A function that takes two integers and returns their sum
def add(x: Int, y: Int): Int = x + y

// An anonymous function that takes two integers and returns their product
val multiply = (x: Int, y: Int) => x * y

// A higher-order function that takes a function and an integer and applies the function twice
def twice(f: Int => Int, x: Int): Int = f(f(x))

// A nested function that calculates the factorial of a number
def factorial(n: Int): Int = {
  def loop(acc: Int, n: Int): Int = {
    if (n == 0) acc
    else loop(acc * n, n - 1)
  }
  loop(1, n)
}

// A free variable that is used by a closure
var factor = 10

// A closure that multiplies an integer by the factor
val multiplier = (x: Int) => x * factor

// A partially applied function that adds 5 to an integer
val addFive = add(5, _: Int)

// A curried function that takes two integers and returns their sum
def curriedAdd(x: Int)(y: Int): Int = x + y

// A closure that returns a function that adds 5 to an integer
val addFiveCurried = curriedAdd(5) _
```