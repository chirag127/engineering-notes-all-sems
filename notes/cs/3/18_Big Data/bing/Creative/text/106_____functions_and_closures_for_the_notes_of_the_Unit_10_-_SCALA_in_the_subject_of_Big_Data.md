### Functions and Closures in Scala

- A function is a block of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the function name, parameters, return type, and body.
- A function can also be defined as an anonymous function, which is a function without a name, using the `=>` operator.
- A function can be assigned to a variable, passed as an argument to another function, or returned from another function.
- A function can be nested inside another function, creating a local scope for the inner function.
- A closure is a special type of function that uses one or more free variables, which are variables that are not defined in the function parameters or body.
- A closure captures the values of the free variables from the surrounding environment, creating a referencing environment for them.
- A closure allows a function to access variables outside its immediate lexical scope, which is the scope where the function is defined.
- A closure can be used to create partially applied functions, which are functions that have some of their parameters fixed by the closure.
- A closure can also be used to create higher-order functions, which are functions that take other functions as arguments or return other functions as results.
- A closure can be defined using the same syntax as an anonymous function, or using a function literal, which is a shorthand notation for an anonymous function.
- A closure can be assigned to a variable, passed as an argument to another function, or returned from another function, just like a normal function.

Some examples of functions and closures in Scala are:

```scala
// A function that takes two integers and returns their sum
def add(x: Int, y: Int): Int = {
  x + y
}

// An anonymous function that takes two integers and returns their product
val multiply = (x: Int, y: Int) => x * y

// A function that takes a function and an integer and applies the function twice to the integer
def twice(f: Int => Int, x: Int): Int = {
  f(f(x))
}

// A closure that uses a free variable z, which is defined outside the closure
val z = 10
val addZ = (x: Int) => x + z

// A closure that returns a partially applied function that adds a fixed value to its argument
def addX(x: Int) = (y: Int) => x + y
val add5 = addX(5) // add5 is a function that adds 5 to its argument

// A closure that returns a higher-order function that takes a function and applies it to its argument
def apply(f: Int => Int) = (x: Int) => f(x)
val square = (x: Int) => x * x
val applySquare = apply(square) // applySquare is a function that squares its argument
```