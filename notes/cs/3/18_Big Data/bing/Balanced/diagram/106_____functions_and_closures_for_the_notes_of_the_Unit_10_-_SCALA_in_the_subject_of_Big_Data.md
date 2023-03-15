### Functions and Closures in Scala

- A function is a block of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the function name, parameters, return type, and body.
- A function can also be defined as an anonymous function, which is a function without a name, using the `=>` operator.
- A function can be assigned to a variable, passed as an argument to another function, or returned from another function.
- A function can be nested inside another function, which means that the inner function can access the parameters and variables of the outer function.
- A closure is a special type of function that uses one or more free variables, which are variables that are not declared in the function or passed as parameters.
- A closure captures the values of the free variables from the surrounding scope, and can use them in its computation.
- A closure allows a function to access variables outside its immediate lexical scope, which means the scope where the function is defined.
- A closure can be useful for creating functions that can be customized with different values, or for creating functions that can maintain some state between calls.

#### Examples of functions and closures in Scala

- The following code defines a function named `add` that takes two parameters of type `Int` and returns their sum.

```scala
def add(x: Int, y: Int): Int = {
  return x + y
}
```

- The following code defines an anonymous function that takes two parameters of type `Int` and returns their product, and assigns it to a variable named `multiply`.

```scala
val multiply = (x: Int, y: Int) => x * y
```

- The following code defines a function named `square` that takes a parameter of type `Int` and returns its square, and passes it as an argument to another function named `apply` that takes a function and an `Int` as parameters and returns the result of applying the function to the `Int`.

```scala
def square(x: Int): Int = x * x

def apply(f: Int => Int, x: Int): Int = f(x)

val result = apply(square, 5) // result is 25
```

- The following code defines a function named `outer` that takes a parameter of type `Int` and returns another function of type `Int => Int`, which is a closure that uses the parameter of the outer function.

```scala
def outer(x: Int): Int => Int = {
  val y = x + 1 // y is a free variable for the inner function
  def inner(z: Int): Int = y * z // inner is a closure that captures y
  return inner
}

val f = outer(10) // f is a function that multiplies its argument by 11
val result = f(5) // result is 55
```