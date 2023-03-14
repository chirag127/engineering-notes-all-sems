#### Functions and Closures in Scala

- A function is a callable unit of code that can take parameters and return a value. A function can be anonymous or named, and can be assigned to a value or passed as an argument to another function.
- A closure is a function that depends on one or more free variables that are defined outside the function. A closure captures the current state of the free variables and can use them in its body. A closure can be pure or impure, depending on whether the free variables are immutable or mutable.
- Some examples of functions and closures in Scala are:

```scala
// an anonymous function that takes an Int and returns an Int
(number: Int) => number + 1

// a named function that takes two Ints and returns a tuple of Ints
val addOne = (x: Int, y: Int) => (x + 1, y + 1)

// a closure that uses a free variable a
var a = 4
val sum = (b: Int) => b + a

// a closure that uses a free variable name
val sayHello = () => println(s"Hello, $name")
```