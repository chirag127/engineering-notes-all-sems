#### Functions and Closures in Scala

- A function is a block of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the function name, parameters, return type, and body.
- A function can also be defined as an anonymous function, or a function literal, using the `=>` syntax.
- A function can be assigned to a variable, passed as an argument to another function, or returned from a function.
- A closure is a special type of function that can access variables that are defined outside its scope.
- A closure captures the values of the free variables at the time of its creation, and can use them in its body.
- A closure can be useful to create functions that depend on some context or state.
- A closure can also be used to implement higher-order functions, such as map, filter, reduce, etc.

Example of a function:

```scala
// A function that takes two integers and returns their sum
def add(x: Int, y: Int): Int = {
  x + y
}
```

Example of a closure:

```scala
// A variable that holds a value
var factor = 3

// A closure that takes an integer and returns its product with the factor
val multiplier = (i: Int) => i * factor

// The closure can access the factor variable, even though it is not a parameter
println(multiplier(10)) // 30

// The closure can also reflect the changes in the factor variable
factor = 5
println(multiplier(10)) // 50
```